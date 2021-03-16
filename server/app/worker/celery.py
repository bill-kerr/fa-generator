import os
from celery import Celery


worker = Celery(
    'worker',
    backend=os.getenv('DB_URI', 'db+mysql://generator:password123@db:3306/generator'),
    broker=os.getenv('BROKER_URI', 'redis://password123@redis:6379/0')
)
