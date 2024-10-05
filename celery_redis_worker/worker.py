from celery import Celery

app = Celery('my_worker', broker='redis://redis:6379/0')

app.conf.update(
    result_backend='redis://redis:6379/0',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)

@app.task
def add(x, y):
    return x + y
