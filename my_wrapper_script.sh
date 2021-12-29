#!/bin/bash

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 content_aggregator.wsgi:application &

# Start retrieving new feed and insert into firestore
python manage.py startjobs &

# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?