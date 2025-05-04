from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.ext.asyncio import AsyncSession
from dependencies.database import get_db
from dependencies.auth import get_current_user, require_role
from schemas.user import UserOut, UserCreate, UserUpdate
from services.user_service import (
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
    list_users
)

router = APIRouter()

@router.get("/me", response_model=UserOut)
async def read_current_user(
    current_user: UserOut = Depends(get_current_user)
):
    return current_user

@router.post("", response_model=UserOut)
async def create_new_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    _ = Depends(require_role("admin"))
):
    existing_user = await get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    return await create_user(db, user_data)

@router.get("", response_model=Page[UserOut])
async def list_all_users(
    db: AsyncSession = Depends(get_db),
    _ = Depends(require_role("admin"))
):
    users = await list_users(db)
    return paginate(users)

add_pagination(router)