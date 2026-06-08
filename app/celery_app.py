from celery import Celery
from app.config import settings

celery_app = Celery(
    "bob_tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Thimphu",  # Bank of Bhutan timezone
    enable_utc=True,
    task_track_started=True,
)

# Discover tasks from app.tasks
celery_app.autodiscover_tasks(["app"])
