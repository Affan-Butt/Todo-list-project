from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL connection string (tumhari HeidiSQL config ke mutabiq)
DATABASE_URL = "postgresql://postgres:Admin1@127.0.0.1:5432/Atm_Machines"

# Engine banate hain
engine = create_engine(DATABASE_URL, echo=True)

# Har request ke liye DB session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class jisse saare ORM models inherit karenge
Base = declarative_base()


# FastAPI dependency: har request pe session open/close
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
