from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from sqlalchemy import Boolean, Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base(object):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp,
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
