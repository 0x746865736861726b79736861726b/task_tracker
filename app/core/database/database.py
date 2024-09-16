from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from app.config import Settings
from app.dependecies import get_settings


__SETTINGS: Settings = get_settings()

__SQLALCHEMY_DATABASE_URL = "".format(**dict(__SETTINGS))


engine = create_engine(
    __SQLALCHEMY_DATABASE_URL,
    future=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_sessions() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
