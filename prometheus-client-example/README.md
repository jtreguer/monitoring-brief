Other example using prometheus_client instead of prometheus_flask_exporter

Add the following queries in Prometheus

requests_total

sum(requests_total) by (method)

rate(requests_total[1m])

In Grafana, add a data source specifying this address: http://prometheus:9090
(and NOT http://localhost:9090)