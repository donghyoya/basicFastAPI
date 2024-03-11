from fastapi import FastAPI
from domain.user.router import router as user_router
from domain.multifile.router import router as mf_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(mf_router, prefix="/multifile")