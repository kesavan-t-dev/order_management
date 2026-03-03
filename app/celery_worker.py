# from celery import Celery
# import os
# from celery import Celery

# broker_url = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
# backend_url = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# celery_app = Celery(
#     "tasks",
#     broker=broker_url,
#     backend=backend_url
# )

# Configure Celery to use Redis as broker and backend
# celery_app = Celery(
#     "tasks",
#     broker="redis://localhost:6379/0",  # Redis broker
#     backend="redis://localhost:6379/0"  # Optional: store task results
# )

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
 #in product_worker i have post and patch endpoints 