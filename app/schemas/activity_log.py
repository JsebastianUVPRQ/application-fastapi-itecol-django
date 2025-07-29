from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ActivityLogBase(BaseModel):
    user_id: Optional[int] = None
    user_type: str
    action: str
    resource_type: str
    resource_id: Optional[int] = None
    description: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None

class ActivityLogCreate(ActivityLogBase):
    pass

class ActivityLogResponse(ActivityLogBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True 