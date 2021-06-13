from fastapi import APIRouter, HTTPException
from starlette import status

import models
from tables import database, ArticlesTable

router = APIRouter(
    prefix="/api",
    tags=['api'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/article/')  # , response_model=List[models.Article])
async def get_articles():
    query = ArticlesTable.select()
    articles = await database.fetch_all(query)
    return {
        'pages_info': [],
        'articles': articles
    }


@router.get('/article/{item_id}/', response_model=models.Article)
async def get_article_by_id(item_id: int):
    query = ArticlesTable.select()
    return await database.fetch_one(query.where(ArticlesTable.columns.id == item_id))


@router.post('/article/')
async def create_article(article: models.ArticleIn):
    query = ArticlesTable.insert().values(title=article.title, content=article.content)
    await database.execute(query)


@router.put('/article/{item_id}/', response_model=models.Article)
async def update_article_by_id(item_id: int, article: models.ArticleIn):
    query = ArticlesTable.update().values(title=article.title, content=article.content)
    resultSuccess = await database.execute(query.where(ArticlesTable.columns.id == item_id))
    if resultSuccess:
        return models.Article(id=item_id, title=article.title, content=article.content)
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="The article could not be saved")


@router.delete('/article/{item_id}/')
async def delete_article_by_id(item_id: int):
    query = ArticlesTable.delete()
    await database.execute(query.where(id=item_id))
