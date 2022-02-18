import uvicorn

from app import create_app

app = create_app()
celery = app.celery_app

if __name__ == "__main__":
    uvicorn.run("main:app")
