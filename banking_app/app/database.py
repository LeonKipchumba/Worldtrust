from sqlalchemy import create_engine
from sqlalchemypipenv  import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///banking_app.db"  # Change this to your desired database URL

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from .models import Base  # Ensure models are imported so tables are created
    Base.metadata.create_all(bind=engine)