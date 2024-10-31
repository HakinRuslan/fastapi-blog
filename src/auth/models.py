from sqlalchemy import String, Integer, TIMESTAMP, Boolean, Date

import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    avatar: Mapped[str] = mapped_column(
        String(length=300), nullable=False
    )
    firstname: Mapped[str] = mapped_column(
        String(length=16), nullable=False
    )
    lastname: Mapped[str] = mapped_column(
        String(length=16), nullable=True
    )
    timereg: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, default=datetime.datetime.utcnow
    )
    email: Mapped[str] = mapped_column(
        String(length=80), unique=True, index=True, nullable=False
    )
    bio: Mapped[str] = mapped_column(
        String(length=365), nullable=True
    )
    date_birth: Mapped[Date] = mapped_column(
        Date, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )