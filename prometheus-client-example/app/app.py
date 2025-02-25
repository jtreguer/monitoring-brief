from flask import Flask
from prometheus_client import Counter, make_wsgi_app #, generate_latest, Gauge, Histogram, Summary
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Prometheus metrics
requests = Counter('requests', 'Number of requests served', ['method', 'endpoint'])

# Custom metrics
# Define a Counter
# REQUEST_COUNT = Counter('flask_requests_total', 'Total number of HTTP requests', ['method', 'endpoint'])
# # Define a Gauge
# ACTIVE_USERS = Gauge('flask_active_users', 'Number of active users')
# # Define a Histogram for request latencies
# REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Request latency in seconds', buckets=[0.1, 0.5, 1.0, 2.0])
# # Define a Summary for response sizes
# RESPONSE_SIZE = Summary('flask_response_size_bytes', 'Response size in bytes')

@app.route('/')
def hello():
    requests.labels(method='GET', endpoint='/').inc()
    # Increment the request counter
   #  REQUEST_COUNT.labels(method=request.method, endpoint='/').inc()
    # Simulate latency
   #  with REQUEST_LATENCY.time():
   #      return "Welcome to the Flask App

# @app.route('/metrics')
# def metrics():
#     # Expose the metrics to Prometheus
#     return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# @app.route('/active_users/<int:count>')
# def update_active_users(count):
#     # Update the active users gauge
#     ACTIVE_USERS.set(count)
#     return f"Active users set to {count}"

# @app.route('/response/<int:size>')
# def response_size(size):
#     # Record response size
#     data = "A" * size
#     RESPONSE_SIZE.observe(len(data))
#     return data

# Mount Prometheus metrics endpoint
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)