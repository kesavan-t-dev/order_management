import os
from celery import Celery
broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
backend_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery_app = Celery(
    "background_tasks",
    broker=broker_url,
    backend=backend_url
)

# Auto-discover tasks from these modules
celery_app.autodiscover_tasks([
   "app.product_worker",
   "app.customer_worker",
   "app.order_worker"
])
