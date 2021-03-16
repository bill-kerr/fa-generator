from time import sleep

from celery import current_task

from worker.celery import worker


@worker.task(acks_late=True)
def test_celery(word: str) -> str:
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS', meta={'process_percent': i*10})
    return f'Test task return {word}'
