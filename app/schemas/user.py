from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str
    role: str

class UserOut(UserBase):
    id: int
    role: str
    is_active: bool