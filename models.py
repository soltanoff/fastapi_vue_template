from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    content: str


class ArticleIn(BaseModel):
    title: str
    content: str
