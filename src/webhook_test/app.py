'''
Flask app for testing webhooks. Prints details about requests, including
pretty-printing JSON when received in POST requests.
'''

import json, os

from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

app = Flask("webhook")

@app.route('/', methods=['GET', 'POST'])
def handler():
    
    print(f"{request.method}")
    
    headers_dict = dict(request.headers)
    for k in headers_dict:
        v = headers_dict[k]
        print(f"\t{k}: {v}")
    
    if request.method == 'POST' and headers_dict.get("Content-Type", "").startswith("application/json"):
        body = request.get_json()
        print(json.dumps(body, sort_keys=True, indent=2, separators=(',', ': ')))
        
    return jsonify({ 'success': True })
        
def run():
    app.run(
        host=os.getenv('APP_HOST', 'localhost'),
        port=int(os.getenv('APP_PORT', '8080'))
    )