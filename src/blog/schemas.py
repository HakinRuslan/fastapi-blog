from pydantic import BaseModel


class BlogSchemaCr(BaseModel):
    id: int
    title: str
    img: str
    content: str
    creator: int

class BlogSchemaUpd(BaseModel):
    title: str
    img: str
    content: str

class BlogSchemaRead(BaseModel):
    title: str
    img: str
    content: str
    creator: int