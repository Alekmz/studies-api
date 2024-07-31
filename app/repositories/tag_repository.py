from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.tag import Tag

class TagRepository:
    def get_tags(self, db: Session, skip: int = 0, limit: int = 10) -> List[Tag]:
        return db.query(Tag).offset(skip).limit(limit).all()

    def get_tag_by_name(self, db: Session, name: str) -> Optional[Tag]:
        return db.query(Tag).filter(Tag.tag_name == name).first()

    def create_tag(self, db: Session, name: str) -> Tag:
        db_tag = db.query(Tag).filter(Tag.tag_name == name).first()
        if db_tag:
            return db_tag
        db_tag = Tag(tag_name=name)
        db.add(db_tag)
        db.commit()
        db.refresh(db_tag)
        return db_tag
