from fastapi import APIRouter, Depends
import json

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from blog.schemas import *
from blog.models import *
from database import get_async_session

router = APIRouter(tags=["blogs"], prefix="/blog")

@router.post("/add_blog")
async def add_blog(createblog: BlogSchemaCr, session: AsyncSession = Depends(get_async_session)):
    query = insert(Blog).values(**createblog.dict())
    blog = createblog.dict()
    readblog = BlogSchemaRead(**blog)
    await session.execute(query)
    await session.commit()
    return {"status": 200, "data": readblog.dict(), "detail": "Добавление блога"}

@router.post("/get_blogs")
async def get_blogs(session: AsyncSession = Depends(get_async_session)):
    query = select(Blog).limit(5)
    result = await session.execute(query)
    items = result.mappings().all()
    blogs = list()
    for i in items:
        blog = i['Blog'].__dict__
        print(blog)
        readblog = BlogSchemaRead(**blog)
        blogs.append(readblog)
    return {"status": 200, "data": blogs, "detail": 'Записи с таблицы'}

    
@router.get("/get_blog/{id}")
async def get_blog(id, session: AsyncSession = Depends(get_async_session)):
    item = int(id)
    query = select(Blog).where(Blog.id == item)
    result = await session.execute(query)
    items = result.mappings().all()
    blog = items['Blog'].__dict__
    readblog = BlogSchemaRead(**blog)
    blogs.append(readblog)
    return {"status": 200, "data": blogs, "detail": 'Записи с таблицы'}
