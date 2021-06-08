from fastapi import APIRouter

import models

router = APIRouter(
    prefix="/api",
    tags=['api'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/article')
async def get_articles():
    return {
        'pages_info': {'length': 0},
        'articles': [{
            'id': 1,
            'title': 1,
            'content': 1,
        }]
    }


@router.get('/article/{item_id}')
async def get_article_by_id(item_id: int):
    return {
        'id': 1,
        'title': 1,
        'content': 1
    }


@router.post('/article')
async def create_article(article: models.Article):
    return {}


@router.put('/article/{item_id}')
async def update_article_by_id(item_id: int):
    return {}


@router.delete('/article/{item_id}')
async def delete_article_by_id(item_id: int):
    return {}
