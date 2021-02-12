from celery import Celery

import labs
from celery_tasks import celeryconfig

celery_app = Celery("async_lab")
celery_app.config_from_object(celeryconfig)
celery_app.autodiscover_tasks(["labs"])
