from fastapi import FastAPI
import uvicorn

from conf.cf import CONFIG

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run(app, host=CONFIG.APP_HOST, port=CONFIG.APP_PORT)
