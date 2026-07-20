# Yeh file kaam karegi:
# → PostgreSQL se connect karegi
# → Session banayegi
# → Base class degi models ke liye


# 3 cheezein banana hain:

# 1. engine
#    → PostgreSQL se actual connection

# 2. SessionLocal
#    → Har request ke liye
#      ek alag DB session

# 3. Base
#    → Saare models
#      isse inherit karenge

# 4. get_db function
#    → Dependency injection ke liye
#    → Har request pe session dega
#    → Request khatam → session band

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Engine create karo
engine = create_engine(DATABASE_URL)

# Session Factory create karo
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# Base Class create karo
Base = declarative_base()

# Dependency Function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()