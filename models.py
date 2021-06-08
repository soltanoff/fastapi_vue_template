from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    context: str


class ArticleIn(BaseModel):
    title: str
    context: str
