from fastapi import FastAPI
from app.routes import router as api_router
from app.database import Base, engine

app = FastAPI()


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")
