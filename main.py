import uvicorn
from fastapi import FastAPI

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_world():
    return {
        "message": "Hello World!",
    }


@app.get("/hello")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}p!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
