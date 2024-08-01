from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.study import Study
from app.models.tag import Tag
from app.schemas.study_schema import StudyCreate, StudyUpdate
from app.repositories.study_repository import StudyRepository
from app.repositories.tag_repository import TagRepository
from app.logger import logger
class StudyService:
    def __init__(self, study_repository: StudyRepository, tag_repository: TagRepository):
        self.study_repository = study_repository
        self.tag_repository = tag_repository

    def get_studies(self, db: Session, skip: int = 0, limit: int = 10) -> List[Study]:
        studies = self.study_repository.get_studies(db, skip=skip, limit=limit)
        logger.info(studies)
        return studies

    def get_study(self, db: Session, study_id: int) -> Optional[Study]:
        study = self.study_repository.get_study(db, study_id)
        logger.info(study)
        return study

    def create_study(self, db: Session, study_create: StudyCreate) -> Study:
        logger.info(study_create)
        study = self.study_repository.create_study(db, study_create)
        for tag_name in study_create.tags:
            logger.info(tag_name)
            tag = self.tag_repository.create_tag(db, tag_name)
            logger.info(tag)
            self.study_repository.add_tag_to_study(db, study.id, tag.id)
        return {
            "subject": study.subject,
            "notes": study.notes,
            "user_id": study.user_id,
            "id":  study.id,
            "tags": study_create.tags,
        }

    def update_study(self, db: Session, study_id: int, study_update: StudyUpdate) -> Optional[Study]:
        study = self.study_repository.update_study(db, study_id, study_update)
        if study:
            self.study_repository.remove_tags_from_study(db, study_id)
            for tag_name in study_update.tags:
                tag = self.tag_repository.create_tag(db, tag_name)
                self.study_repository.add_tag_to_study(db, study.id, tag.id)
        return {
            "subject": study.subject,
            "notes": study.notes,
            "user_id": study.user_id,
            "id":  study.id,
            "tags": study_update.tags,
        }

    def delete_study(self, db: Session, study_id: int) -> Optional[Study]:
        return self.study_repository.delete_study(db, study_id)
