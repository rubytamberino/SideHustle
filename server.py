from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
BROWSERUSE_API_KEY = os.getenv("BROWSERUSE_API_KEY")

@app.route("/browseruse-relay", methods=["POST"])
def relay_request():
    try:
        prompt = request.json.get("prompt")
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400

        response = requests.post(
            "https://agent.browseruse.com/v1/query",
            headers={
                "Authorization": f"Bearer {BROWSERUSE_API_KEY}",
                "Content-Type": "application/json"
            },
            json={"prompt": prompt}
        )

        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
