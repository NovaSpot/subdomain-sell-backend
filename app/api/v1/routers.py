# routers/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login(): ...

@router.post("/register")
async def register(): ...

@router.post("/refresh-token")
async def refresh_token(): ...