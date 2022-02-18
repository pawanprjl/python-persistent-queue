from celery import shared_task


@shared_task
def update_active_status(user_id: int):
    import time
    from app.db import SessionLocal
    from app.users import crud

    db = SessionLocal()
    time.sleep(20)

    user = crud.get_user_by_id(db, user_id)
    user.is_active = True
    result = crud.update_user(db, user)
    db.close()

    return user_id
