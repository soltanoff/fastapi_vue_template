from typing import List

from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    content: str


class ArticleIn(BaseModel):
    title: str
    content: str


class PaginationInfo(BaseModel):
    number: str
    link: str


class PaginatedArticles(BaseModel):
    pages_info = List[PaginationInfo]
    articles = List[Article]
