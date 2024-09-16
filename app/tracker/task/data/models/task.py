from typing import TYPE_CHECKING

from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from app.core.models.models import Base


from app.tracker.user.data.models.user import User


class Task(Base):
    __tablename__ = "tasks"

    title: Mapped[str] | str = Column(String, index=True)
    is_completed: Mapped[bool] | bool | None = Column(Boolean, default=False)
    owner_id: Mapped[int] | int | None = Column(Integer, ForeignKey("users.id"))

    owner: Mapped["User"] = relationship("User", back_populates="tasks", uselist=True)
