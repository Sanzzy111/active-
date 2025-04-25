from flask import Flask
import requests
import os

app = Flask(__name__)

# Ganti dengan URL bot Replit kamu
REPLIT_URL = "https://2e11e93e-5882-4e5f-84a5-046cb70de076-00-156kht34tm5io.janeway.replit.dev"

@app.route('/')
def home():
    try:
        requests.get(REPLIT_URL)
        return "Pinged your Replit bot!"
    except Exception as e:
        return f"Failed to ping Replit bot: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
