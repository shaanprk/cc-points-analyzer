from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab # Import crontab for scheduling

# Set default Django settings module for 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

# Use settings defined in Django's settings file
app.config_from_object('django.conf:settings', namespace='CELERY')

# Fix deprecated warning
app.conf.broker_connection_retry_on_startup = True

# Auto-discover tasks from installed apps
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-scrapers-daily': {
        'task': 'scraper.tasks.run_scrapers', # Task to run daily
        'schedule': crontab(hour=0, minute=0),  # Run once a day at midnight
    },
}

# Optiona timezone setting
app.conf.timezone = 'PST'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
