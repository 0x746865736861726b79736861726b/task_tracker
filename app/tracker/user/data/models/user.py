from typing import TYPE_CHECKING

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import relationship, Mapped

from app.core.models.models import Base

if TYPE_CHECKING:
    from app.tracker.user.data.models.user import Task


class User(Base):
    __tablename__ = "users"
    email: Mapped[str] | str = Column(String, unique=True, index=True)
    password: Mapped[str] | str = Column(String)
    is_active: Mapped[bool] | bool = Column(Boolean, default=True)

    tasks: Mapped[list["Task"]] = relationship(
        "Task", back_populates="owner", uselist=True
    )
