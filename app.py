from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def my_api():
    value = 0
    # your logic to update value goes here
    return f'The current value is {value}'

if __name__ == '__main__':
    app.run()