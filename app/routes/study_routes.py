from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.study_schema import StudyCreate, StudyUpdate, Study
from app.services.study_service import StudyService
from app.repositories.study_repository import StudyRepository
from app.repositories.tag_repository import TagRepository
from app.database import get_db
from app.logger import logger
router = APIRouter()

study_service = StudyService(study_repository=StudyRepository(), tag_repository=TagRepository())

@router.get("/", response_model=List[Study])
def read_studies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return study_service.get_studies(db, skip, limit)

@router.get("/{study_id}", response_model=Study)
def read_study(study_id: int, db: Session = Depends(get_db)):
    db_study = study_service.get_study(db, study_id)
    if not db_study:
        raise HTTPException(status_code=404, detail="Study not found")
    return db_study

@router.post("/", response_model=Study)
def create_study(study: StudyCreate, db: Session = Depends(get_db)):
    try:
        logger.info(study)
        return study_service.create_study(db, study)
    except:
        raise HTTPException(status_code=404, detail="Create study error")


@router.put("/{study_id}", response_model=Study)
def update_study(study_id: int, study: StudyUpdate, db: Session = Depends(get_db)):
    db_study = study_service.update_study(db, study_id, study)
    if not db_study:
        raise HTTPException(status_code=404, detail="Study not found")
    return db_study

@router.delete("/{study_id}", response_model=Study)
def delete_study(study_id: int, db: Session = Depends(get_db)):
    db_study = study_service.delete_study(db, study_id)
    if not db_study:
        raise HTTPException(status_code=404, detail="Study not found")
    return db_study
