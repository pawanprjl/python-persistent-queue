from fastapi import FastAPI

from app.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    # configure celery with app
    app.celery_app = create_celery()

    # routes
    from app.users import router as users_router
    app.include_router(users_router, tags=["User Router"])

    @app.get("/", tags=["Default"])
    async def root():
        return {"message": "Server is up !!"}

    return app
