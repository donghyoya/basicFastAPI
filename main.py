from fastapi import FastAPI
from domain.user.router import router as user_router
from domain.multifile.router import router as mf_router

from default.middleware.corsmiddleware import setup_cors
from default.middleware.sessionmiddleware import session_middleware


app = FastAPI()

setup_cors(app)
app.add_middleware(session_middleware)

app.include_router(user_router, prefix="/user")
app.include_router(mf_router, prefix="/multifile")