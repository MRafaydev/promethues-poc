from flask import Flask, Response
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define your metrics
c = Counter('my_counter', 'Description of my counter')
g = Gauge('my_gauge', 'Description of my gauge')
h = Histogram('my_histogram', 'Description of my histogram')

@app.route('/')
def hello_world():
    # Increment the counter
    c.inc()

    # Set the gauge
    g.set(42)

    # Record the histogram
    h.observe(0.5)

    return 'Hello, World!'

# Expose the Prometheus client HTTP server endpoint
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
