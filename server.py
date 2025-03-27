import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/browseruse-relay', methods=['POST'])
def relay():
    try:
        data = request.get_json()
        api_key = os.getenv('BROWSERUSE_API_KEY')
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Host": "agent.browseruse.com"  # <-- Explicitly set Host header
        }

        response = requests.post(
            "https://agent.browseruse.com/v1/query",
            headers=headers,
            json=data,
            verify=False  # <-- Disable SSL verification temporarily
        )

        return jsonify(response.json
