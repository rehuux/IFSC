import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "IFSC Lookup API",
        "usage": "/api/ifsc?ifsc=XXXX",
        "developer": "@istgrehu"
    })

@app.route("/api/ifsc", methods=["GET"])
def ifsc_lookup():
    ifsc = request.args.get("ifsc")

    if not ifsc:
        return jsonify({
            "error": "Use ?ifsc=<IFSC Code>",
            "developer": "@istgrehu"
        }), 400

    try:
        url = f"https://ifsc.razorpay.com/{ifsc.strip()}"
        res = requests.get(url)

        if res.status_code != 200:
            return jsonify({
                "error": "Invalid IFSC",
                "developer": "@istgrehu"
            }), 404

        data = res.json()
        data["developer"] = "@istgrehu"
        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": "Server error",
            "detail": str(e),
            "developer": "@istgrehu"
        }), 500
