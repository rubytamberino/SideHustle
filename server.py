from flask import Flask, request, jsonify
import os
import traceback
import requests

app = Flask(__name__)

@app.route("/browseruse-relay", methods=["POST"])
def relay():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Missing 'prompt' in request"}), 400

        api_key = os.getenv("BROWSERUSE_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment")

        response = requests.post(
            "https://agent.browseruse.com/v1/query",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={"prompt": prompt},
            timeout=30
        )

        response.raise_for_status()
        return jsonify(response.json())

    except Exception as e:
        print("🛑 An error occurred:")
        traceback.print_exc()
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
