# 🌍 Free IP Geolocation API (No API Key) — Open Source

**Free IP geolocation API with VPN detection, ASN lookup, ISP intelligence, and batch IP analysis.**

Convert any IP address into structured intelligence instantly — no authentication required.

```bash
curl https://your-domain.vercel.app/api/lookup?ip=8.8.8.8
```

Returns:

* country
* region
* city
* coordinates
* ISP provider
* ASN number
* hostname
* VPN / proxy detection
* infrastructure metadata

---

# 🚀 Quick Start

### Single Lookup

```bash
curl https://your-domain.vercel.app/api/lookup?ip=8.8.8.8
```

### Batch Lookup

```bash
curl -X POST https://your-domain.vercel.app/api/lookup/batch \
  -H "Content-Type: application/json" \
  -d '{"ips": ["8.8.8.8","1.1.1.1"]}'
```

---

# 📡 API Endpoints

## GET /api/lookup

Lookup a single IP address.

Example:

```http
GET /api/lookup?ip=8.8.8.8
```

---

## POST /api/lookup/batch

Lookup multiple IP addresses.

```json
{
  "ips": ["8.8.8.8","1.1.1.1"]
}
```

---

## GET /api/health

Health status endpoint.

```http
GET /api/health
```

---

# 🌍 Example Response

```json
{
  "success": true,
  "query": {
    "ip": "8.8.8.8"
  },
  "ip_details": {
    "isp": "Google LLC",
    "asn": "AS15169",
    "hostname": "dns.google",
    "location": {
      "country": "United States",
      "city": "Mountain View",
      "coordinates": {
        "latitude": 37.4056,
        "longitude": -122.0775
      }
    }
  },
  "metadata": {
    "is_vpn": false
  }
}
```

---

# ✨ Features

| Feature                 | Supported |
| ----------------------- | --------- |
| Free IP geolocation API | ✅         |
| VPN detection API       | ✅         |
| ASN lookup API          | ✅         |
| ISP intelligence        | ✅         |
| Reverse hostname lookup | ✅         |
| Batch lookup            | ✅         |
| No API key required     | ✅         |
| Open source             | ✅         |

---

# ⚡ Performance

| Metric              | Value     |
| ------------------- | --------- |
| Response time       | <500ms    |
| Batch size          | 10 IPs    |
| Requests/minute     | 45        |
| Concurrent requests | Unlimited |
| Uptime              | 99.9%     |

---

# 🧠 Use Cases

### Fraud Detection

```python
if ip_data["metadata"]["is_vpn"]:
    block_request()
```

### Geo Targeting

```python
if country == "United States":
    show_us_content()
```

### Analytics Enrichment

```python
log["isp"] = ip_data["ip_details"]["isp"]
```

---

# 🌎 Global Coverage

Supports IP intelligence across:

* North America
* Europe
* Asia Pacific
* Latin America
* Africa
* Middle East

---

# 🔐 Privacy Friendly

This API:

* does NOT store lookups
* does NOT track users
* requires NO authentication
* uses HTTPS only
* supports GDPR-friendly workflows

---

# 🛠 Local Development

```bash
git clone https://github.com/yourusername/ip-lookup-api.git
cd ip-lookup-api

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python api/lookup.py
```

---

# 📚 Parameters

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| ip        | string | Yes      |

---

# ❗ Error Codes

| Code | Meaning             |
| ---- | ------------------- |
| 200  | Success             |
| 400  | Invalid IP          |
| 429  | Rate limit exceeded |
| 500  | Server error        |

---

# ❓ FAQ — Free IP Geolocation API

## What is a free IP geolocation API?

A free IP geolocation API converts an IP address into structured geographic data such as country, region, city, ISP, ASN, and coordinates without requiring authentication.

---

## Does this IP lookup API require an API key?

No. This API works instantly without signup or API credentials.

---

## Can this API detect VPN and proxy traffic?

Yes. It includes infrastructure intelligence signals that identify VPN and proxy IP ranges.

---

## What information does the API return?

The API returns:

* country
* region
* city
* coordinates
* ISP
* ASN
* hostname
* VPN detection metadata

---

## Is this API suitable for production use?

This API is designed primarily for educational use, experimentation, and developer research workflows. Production users should evaluate availability and compliance requirements independently.

---

## Can I deploy my own instance?

Yes.

Deploy instantly:

https://vercel.com/new/clone?repository-url=https://github.com/yourusername/ip-lookup-api

---

# ⚠️ Educational Use Notice

This project aggregates publicly available IP intelligence data and is intended strictly for:

* educational purposes
* research experimentation
* infrastructure learning
* prototype security tooling
* API development practice

It should not be relied upon as a sole source of truth for compliance-critical production systems.

---

# 🔍 SEO Keywords Covered

This repository targets:

* free IP geolocation API
* IP lookup API free
* IP to location API free
* VPN detection API free
* IP intelligence API
* reverse IP lookup API
* batch IP lookup API
* geolocation API without API key

---

# 📄 License

MIT License © 2026
