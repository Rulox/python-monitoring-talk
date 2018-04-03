import random

from flask import Flask, Response, abort
from prometheus_client import Counter, generate_latest


CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

app = Flask(__name__)

# Flask routes

index_requests = Counter("n_requests_index", "Number of requests to the Index / endpoint")
@app.route("/")
def hello():
    index_requests.inc()
    return "It works! You're visiting /"


# With Labels
server_requests = Counter('my_requests_total', 'HTTP Requests', ['status', 'endpoint'])
@app.route("/labels")
def labels():
    """
    This function tries to mimmic a normal http server. It will return randomly
    200/403/404/500 status codes with the responses to test the CounterVec with
    Labels from prometheus.
    """
    status = [200, 403, 404, 500]
    code = random.choice(status)
    server_requests.labels(status=code, endpoint="/labels").inc()
    if code == 200:
        return "OK"
    else:
        abort(code)

@app.route('/metrics/')
def metrics():
    """
    We need to add an endpoint of our flask server to expose the metrics so
    Prometheus can fetch all. See Note1 in main() for more info.
    """
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    # start_http_server(9888) Note: You would normally use this in a regular sync python app.
    app.run(debug=True, host="0.0.0.0", port=5000)
