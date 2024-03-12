from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from redis import Redis
import json

# Redis 클라이언트 초기화
redis_client = Redis(host='localhost', port=6379, db=0, password='yourpassword')

async def session_middleware(request: Request, call_next):
    session_token = request.cookies.get('session_token')
    
    if session_token and redis_client.exists(session_token):
        # 세션 토큰이 유효한 경우, 요청을 계속 진행
        response = await call_next(request)
    else:
        # 세션 토큰이 없거나 유효하지 않은 경우, 에러 응답 반환
        return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
    
    return response
