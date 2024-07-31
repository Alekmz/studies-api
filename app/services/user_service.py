from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def get_user_by_id(self, db: Session, user_id: int):
        return self.repository.get_user_by_id(db, user_id)
    
    def get_user_by_username(self, db: Session, username: str):
        return self.repository.get_user_by_username(db, username)
    
    def get_user_by_email(self, db: Session, email: str):
        return self.repository.get_user_by_email(db, email)
    
    def create_user(self, db: Session, user: UserCreate):
        hashed_password = pwd_context.hash(user.password)
        db_user = UserCreate(username=user.username, email=user.email, password=hashed_password)
        return self.repository.create_user(db, db_user)
    
    def authenticate_user(self, db: Session, username: str, password: str):
        user = self.get_user_by_username(db, username)
        if not user:
            return False
        if not pwd_context.verify(password, user.password):
            return False
        return user