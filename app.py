from flask import Flask
from prometheus_client import Counter, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Prometheus metrics
requests = Counter('requests', 'Number of requests served', ['method', 'endpoint'])

@app.route('/')
def hello():
    requests.labels(method='GET', endpoint='/').inc()
    return 'Hello, World!'

# Mount Prometheus metrics endpoint
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)