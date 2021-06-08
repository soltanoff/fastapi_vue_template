from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

import settings

router = APIRouter(
    tags=['index'],
    responses={404: {'description': 'Not found'}},
)

templates = Jinja2Templates(directory=settings.TEMPLATE_DIRECTORY)


@router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        name=settings.BASE_TEMPLATE_NAME,
        context={'request': request, 'csrf_token': 'TODO'}
    )
