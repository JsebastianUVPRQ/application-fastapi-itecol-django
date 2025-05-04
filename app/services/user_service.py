from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from models.user import User
from core.security import get_password_hash
from schemas.user import UserCreate, UserUpdate

async def get_user_by_email(db: AsyncSession, email: str) -> User:
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name,
        role=user_data.role
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(
    db: AsyncSession,
    user_id: int,
    update_data: UserUpdate
) -> User:
    update_values = update_data.dict(exclude_unset=True)
    if "password" in update_values:
        update_values["hashed_password"] = get_password_hash(update_values.pop("password"))
    
    await db.execute(
        update(User)
        .where(User.id == user_id)
        .values(**update_values)
    )
    await db.commit()
    return await get_user_by_id(db, user_id)