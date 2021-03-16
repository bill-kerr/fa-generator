import logging

from fastapi import FastAPI, BackgroundTasks

from worker.celery import worker

log = logging.getLogger(__name__)

app = FastAPI(title='Force Account Generator API', docs_url='/docs')


def celery_on_message(body):
    log.warn(body)


def background_on_message(task):
    log.warn(task.get(on_message=celery_on_message, propogate=False))


@app.get('/{word}')
async def root(word: str, background_task: BackgroundTasks):
    task = worker.send_task('worker.tasks.test_celery', args=[word])
    print(task)
    background_task.add_task(background_on_message, task)

    return {'message': word}
