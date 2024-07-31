from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.study import Study
from app.models.study_tag import StudyTag
from app.schemas.study_schema import StudyCreate, StudyUpdate
from sqlalchemy import text
class StudyRepository:
    def get_studies(self, db: Session, skip: int = 0, limit: int = 10) -> List[Study]:
        query = text("""
            SELECT 
                s.subject, 
                s.notes, 
                array_agg(t.tag_name) AS tags,
                s.id ,
                s.user_id   
            FROM 
                studies s
            JOIN 
                study_tags st ON s.id = st.study_id
            JOIN 
                tags t ON st.tag_id = t.id
            GROUP BY 
                s.id;
        """)    
        result = db.execute(query).fetchall()
        return result
    def get_study(self, db: Session, study_id: int) -> Optional[Study]:
        query = text(f"""
            SELECT 
                s.subject, 
                s.notes, 
                array_agg(t.tag_name) AS tags,
                s.id ,
                s.user_id   
            FROM 
                studies s
            JOIN 
                study_tags st ON s.id = st.study_id
            JOIN 
                tags t ON st.tag_id = t.id
            WHERE 
                s.id = {study_id}
                	GROUP BY s.id;
        """) 
        return db.execute(query).first()
    def create_study(self, db: Session, study: StudyCreate) -> Study:
        db_study = Study(
            subject=study.subject,
            notes=study.notes,
            user_id=study.user_id
        )
        db.add(db_study)
        db.commit()
        db.refresh(db_study)
        return db_study

    def update_study(self, db: Session, study_id: int, study_update: StudyUpdate) -> Optional[Study]:
        db_study = db.query(Study).filter(Study.id == study_id).first()
        if db_study:
            db_study.topic = study_update.topic
            db_study.subject = study_update.subject
            db_study.notes = study_update.notes
            db.commit()
            db.refresh(db_study)
        return db_study

    def delete_study(self, db: Session, study_id: int) -> Optional[Study]:
        db_study = db.query(Study).filter(Study.id == study_id).first()
        if db_study:
            db.query(StudyTag).filter(StudyTag.study_id == study_id).delete()
            db.delete(db_study)
            db.commit()
        return db_study

    def add_tag_to_study(self, db: Session, study_id: int, tag_id: int) -> None:
        study_tag = StudyTag(study_id=study_id, tag_id=tag_id)
        db.add(study_tag)
        db.commit()

    def remove_tags_from_study(self, db: Session, study_id: int) -> None:
        db.query(StudyTag).filter(StudyTag.study_id == study_id).delete()
        db.commit()
