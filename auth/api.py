from fastapi import APIRouter
from starlette.responses import RedirectResponse	

router = APIRouter()

@router.get("/")
def read_root():
	return RedirectResponse(url="/docs")
