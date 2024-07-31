from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    tag_name = Column(String, unique=True, index=True)

    studies = relationship("Study", secondary="study_tags", back_populates="tags")
