import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/ifsc", methods=["GET"])
def ifsc_lookup():
    ifsc = request.args.get("ifsc")

    if not ifsc:
        return jsonify({
            "error": "Use ?ifsc=<IFSC Code>",
            "developer": "@istgrehu"
        }), 400

    try:
        api_url = f"https://ifsc.razorpay.com/{ifsc.strip()}"
        r = requests.get(api_url)

        # If not found
        if r.status_code != 200:
            return jsonify({
                "error": "Invalid IFSC code or not found",
                "developer": "@istgrehu"
            }), 404

        data = r.json()

        # Add developer tag in success response
        data["developer"] = "@istgrehu"

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": "Something went wrong",
            "detail": str(e),
            "developer": "@istgrehu"
        }), 500


def handler(request, *args, **kwargs):
    with app.test_request_context(
        path=request.path,
        method=request.method,
        query_string=request.query_string
    ):
        return app.full_dispatch_request()
