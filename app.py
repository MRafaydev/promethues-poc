from flask import Flask
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest, CONTENT_TYPE_LATEST
from flask import Response

app = Flask(__name__)

REQUEST_COUNT = Counter('flask_app_request_count', 'Flask App Request Count', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('flask_app_request_latency_seconds', 'Flask App Request Latency', ['method', 'endpoint'])
REQUEST_GAUGE = Gauge('flask_app_request_gauge', 'Flask App Request Gauge', ['method', 'endpoint'])

@app.route("/")
def hello():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():
        # Your code here
        time.sleep(1)
    REQUEST_GAUGE.labels(method='GET', endpoint='/').set(42)
    return "Hello World!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
