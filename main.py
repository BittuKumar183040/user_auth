from fastapi import FastAPI
from auth.api import router
from auth.user.api import router as user_router

app = FastAPI(title="JWT Authentication")

tags_metadata = [
	{
		"name": "users",
		"description": "Operations with users. The **login** logic is also here.",
	},
]

app.include_router(router)
app.include_router(user_router, prefix="/user", tags=["Users Auth."])
