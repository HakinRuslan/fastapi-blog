from typing import AsyncGenerator

from sqlalchemy import MetaData

from sqlalchemy.orm import DeclarativeBase

from config import u, psw, h, p, db

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

metadata = MetaData()

class Base(DeclarativeBase):
    pass

url = f"postgresql+asyncpg://{u}:{psw}@{h}:{p}/{db}"

engine = create_async_engine(url)
session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session 