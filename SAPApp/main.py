from typing import Optional
from fastapi import Depends, FastAPI
from datetime import datetime
from sqlalchemy.orm import Session
# from . import crud, models, schemas
import crud
import models
import schemas
from database import SessionLocal, engine
from typing import List
import uvicorn

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/status")
def read_root():
    return {"status": "alive"}


@app.post("/synchronize")
def create_record(request: schemas.RecordCreate, db: Session = Depends(get_db)):
    print(request)
    crud.create_record(db, record=request)
    return {
        "is_success": True
    }


@app.get("/synchronize", response_model=List[schemas.Record])
def get_records(db: Session = Depends(get_db)):
    return crud.get_records(db)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
