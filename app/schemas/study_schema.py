from typing import List, Optional
from pydantic import BaseModel

class StudyBase(BaseModel):
    subject: str
    notes: Optional[str] = None
    user_id: int

class StudyCreate(StudyBase):
    tags: List[str]

class StudyUpdate(StudyBase):
    tags: List[str]

class Study(StudyBase):
    id: int
    tags: List[str] | str

    class Config:
        orm_mode = True
