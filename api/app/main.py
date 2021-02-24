from fastapi import FastAPI


app = FastAPI(title='Force Account Generator', docs_url='/docs')


@app.get('/')
def hello_world():
    return {"message": "hello world!"}
