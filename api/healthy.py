from flask import jsonify
from datetime import datetime

# Made in love by developer Maxwell
#For educational purposes only

def handler(request):
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'IP Lookup API'
    })
