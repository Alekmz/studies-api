from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class StudyTag(Base):
    __tablename__ = 'study_tags'

    study_id = Column(Integer, ForeignKey('studies.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)
