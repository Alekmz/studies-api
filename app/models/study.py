from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Study(Base):
    __tablename__ = 'studies'

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="studies")
    tags = relationship('Tag', secondary='study_tags')
