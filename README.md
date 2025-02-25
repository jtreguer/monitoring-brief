# Introduction au monitoring d'application

## Outils

Nous proposons d'utiliser Prometheus, Grafana et l'Alert Manager de Prometheus pour cette introduction :

    * Prometheus : collecte des métriques depuis l'application (dans nos exemples une application Flask)
    * Alertmanager : gère les alertes relevés par Prometheus en fonction de rgèles pré-définies et Handles alerts triggered by Prometheus based on predefined rules.
    Grafana : Visualizes metrics and can display alerts.

En amont, Prometheus peut recueillir des métriques de frameworks web (liste non exhaustive) et de bases de données :
* Python : Flask, Django, FastAPI,...
* Node.js
* Go
* Ruby
* PHP
* Java : Spring Boot, Quarkus, Vert.x
BDD :
* MySQL/MariaDB
* PostgreSQL

Et aussi :
* Docker / Kubernetes
* Azure / AWS / Google Cloud

Note : on peut aussi utiliser OpenTelemetry entre l'application et Prometheus pour collecter les métriques.

En aval, Prometheus peut alimenter des backends :
- de visualisation, comme Grafana, Kibana, Chronograph, Datadog...
- d'alertes, comme Alertmanager (intégré à Prometheus), Grafana OnCall, Zabbix, Nagios...
- de stockage de données (pour conserver les métriques), comme TSDB (intégré à Prometheus), Thanos, Cortex, ElasticSearch...
- d'interopérabilité, pour échanger avec d'autres systèmes, comme OpenMetrics, Prometheus Federation...

![Prometheus architecture](./prometheus-architecture.png)

## Les métriques

Différentes catégories :
    Counter : A cumulative metric that only increases (e.g., total requests, errors).
    Gauge : A metric that can increase or decrease (e.g., current number of active users).
    Histogram : Used to measure the distribution of values (e.g., request latencies).
    Summary : Similar to Histogram but calculates quantiles (e.g., 95th percentile latency).

Prédéfinies

Personalisées 
     

## Exemples

Avec prometheus_flask_exporter
1- Flask seul (/sample-signals)
2- Flask + Gunicorn (/sample-signals-gunicorn)
3- Flask + Gunicorn + Alerter (/sample-signals-gunicorn-alerter)
Avec prometheus_client
4 - Flask + Gunicorn (/prometheus-client-example)
    Manip Prometheus et dans Grafana (data source / dashboard)

**Petit rendu :**
* Copier le répertoire de l'exemple 4
* 
* Ajouter une nouvelle route ou modifier une route existante dans l'app pour qu'elle réponde aléatoirement avec un code 200 (OK), 500 (pas de réponse serveur) ou 404 (fichier non trouvé)
* Enrichir le dashboard grafana pour suivre les occurrences de codes d'erreur
* Ajouter une ou plusieurs règles d'alertes pour les codes d'erreur
* BONUS : créer une métrique personnalisée dans l'appli flask à transmettre à Prometheus

**Pour aller plus loin :**

Des collections d'alertes :
    - https://www.squadcast.com/blog/prometheus-sample-alert-rules#prometheus-sample-alert-rules
    - https://samber.github.io/awesome-prometheus-alerts/rules.html
