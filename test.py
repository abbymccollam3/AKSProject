from flask import Flask
import time
from ddtrace import patch_all, tracer

patch_all()

app = Flask(__name__)

@app.route("/")
def hello():
    time.sleep(0.1)
    return "Hello from Datadog-traced Flask app!"

@app.route("/checkout")
def checkout():
    time.sleep(0.3)
    return "Checkout complete"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)