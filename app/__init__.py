from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    # routes
    from app.users import router as users_router
    app.include_router(users_router, tags=["User Router"])

    @app.get("/", tags=["Default"])
    async def root():
        return {"message": "Server is up !!"}

    return app
