#!/bin/bash
export FLASK_APP="."
echo "Flask environment variables set"
gunicorn -w 1 --timeout 6000 -b 0.0.0.0:5000 wsgi:app
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]