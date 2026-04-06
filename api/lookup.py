from curl_cffi import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def clean_coordinate(coord_str):
    """Extract just the numeric value from coordinate strings"""
    if not coord_str:
        return None
    match = re.search(r'([-\d.]+)', coord_str)
    return float(match.group(1)) if match else None

def get_whatismyip_data(ip_address):
    """
    Get clean, organized JSON from whatismyipaddress.com
    """
    session = requests.Session(impersonate="chrome120")
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    session.headers.update(headers)
    
    try:
        # Visit homepage first
        session.get('https://whatismyipaddress.com/', timeout=15)
        
        # Get IP data
        url = f'https://whatismyipaddress.com/ip/{ip_address}'
        response = session.get(url, timeout=15)
        
        if response.status_code != 200:
            return {'error': f'Failed with status {response.status_code}'}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract raw data
        raw_data = {}
        info_items = soup.find_all('p', class_='information')
        
        for item in info_items:
            spans = item.find_all('span')
            if len(spans) >= 2:
                key = spans[0].text.strip().rstrip(':')
                value = spans[1].text.strip()
                raw_data[key] = value
        
        # Extract user comments
        comments = []
        comment_spans = soup.find_all('span', style='font-size:16px;')
        for span in comment_spans:
            comment_text = span.get_text(strip=True)
            if comment_text and len(comment_text) > 10:
                date_elem = span.find_next('em')
                date = date_elem.get_text(strip=True) if date_elem else None
                comments.append({
                    'text': comment_text,
                    'date': date
                })
        
        # Create clean, organized JSON
        clean_data = {
            "success": True,
            "query": {
                "ip": ip_address,
                "timestamp": datetime.now().isoformat(),
                "source": "whatismyipaddress.com"
            },
            "ip_details": {
                "decimal": raw_data.get("Decimal"),
                "hostname": raw_data.get("Hostname"),
                "asn": raw_data.get("ASN"),
                "isp": raw_data.get("ISP"),
                "services": raw_data.get("Services", "").split(", ") if raw_data.get("Services") else [],
                "location": {
                    "country": raw_data.get("Country"),
                    "state_region": raw_data.get("State/Region"),
                    "city": raw_data.get("City"),
                    "coordinates": {
                        "latitude": clean_coordinate(raw_data.get("Latitude", "")),
                        "longitude": clean_coordinate(raw_data.get("Longitude", ""))
                    }
                }
            },
            "user_comments": comments[:10],  # Limit to 10 comments
            "metadata": {
                "is_vpn": "VPN" in raw_data.get("Services", ""),
                "has_comments": len(comments) > 0,
                "comment_count": len(comments)
            }
        }
        
        return clean_data
        
    except Exception as e:
        return {'success': False, 'error': str(e)}

@app.route('/api/lookup', methods=['GET'])
def lookup_ip():
    """Lookup IP address information"""
    ip = request.args.get('ip')
    
    if not ip:
        return jsonify({
            'success': False,
            'error': 'Missing ip parameter',
            'usage': '/api/lookup?ip=8.8.8.8'
        }), 400
    
    # Validate IP format (simple validation)
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if not ip_pattern.match(ip):
        return jsonify({
            'success': False,
            'error': 'Invalid IP address format'
        }), 400
    
    result = get_whatismyip_data(ip)
    
    if result.get('success'):
        return jsonify(result)
    else:
        return jsonify(result), 500

@app.route('/api/lookup/batch', methods=['POST'])
def lookup_batch():
    """Lookup multiple IP addresses"""
    data = request.get_json()
    
    if not data or 'ips' not in data:
        return jsonify({
            'success': False,
            'error': 'Missing ips array in request body',
            'usage': 'POST /api/lookup/batch with {"ips": ["8.8.8.8", "1.1.1.1"]}'
        }), 400
    
    ips = data.get('ips', [])
    
    if not isinstance(ips, list):
        return jsonify({
            'success': False,
            'error': 'ips must be an array'
        }), 400
    
    if len(ips) > 10:
        return jsonify({
            'success': False,
            'error': 'Maximum 10 IPs per batch request'
        }), 400
    
    results = []
    for ip in ips:
        result = get_whatismyip_data(ip)
        results.append(result)
    
    return jsonify({
        'success': True,
        'total': len(results),
        'timestamp': datetime.now().isoformat(),
        'results': results
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'IP Lookup API'
    })


app = app

if __name__ == '__main__':
    app.run(debug=True, port=5000)
