from fastapi import FastAPI
from domain.user.router import router as user_router
from domain.multifile.router import router as mf_router

from default.config.corsmiddleware import setup_cors

import redis

redis_client = redis.Redis(host='localhost', port=6376, decode_responses=True)

app = FastAPI()

setup_cors(app)

app.include_router(user_router, prefix="/user")
app.include_router(mf_router, prefix="/multifile")