from sqlalchemy import Column, Integer, String, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Study(Base):
    __tablename__ = 'studies'

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    user = relationship("User", back_populates="studies")
    tags = relationship('Tag', secondary='study_tags')
