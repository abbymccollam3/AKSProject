from flask import Flask
import time
import logging
from ddtrace import patch_all, tracer

patch_all()

# Configure logging format to include Datadog trace correlation attributes
FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s '
          'dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT, level=logging.INFO)
log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def hello():
    log.info('Handling request to / endpoint')
    time.sleep(0.1)
    log.info('Returning response from / endpoint')
    return "Hello from Datadog-traced Flask app!"

@app.route("/checkout")
def checkout():
    log.info('Handling request to /checkout endpoint')
    time.sleep(0.3)
    log.info('Checkout process completed')
    return "Checkout complete"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)