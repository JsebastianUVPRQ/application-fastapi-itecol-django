from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.activity_log import ActivityLog
from app.schemas.activity_log import ActivityLogCreate

class CRUDActivityLog(CRUDBase[ActivityLog, ActivityLogCreate, ActivityLogCreate]):
    def get_by_user(self, db: Session, *, user_id: int) -> List[ActivityLog]:
        return db.query(ActivityLog).filter(ActivityLog.user_id == user_id).all()
    
    def get_by_user_type(self, db: Session, *, user_type: str) -> List[ActivityLog]:
        return db.query(ActivityLog).filter(ActivityLog.user_type == user_type).all()
    
    def get_by_resource(self, db: Session, *, resource_type: str, resource_id: int) -> List[ActivityLog]:
        return db.query(ActivityLog).filter(
            ActivityLog.resource_type == resource_type,
            ActivityLog.resource_id == resource_id
        ).all()
    
    def get_by_action(self, db: Session, *, action: str) -> List[ActivityLog]:
        return db.query(ActivityLog).filter(ActivityLog.action == action).all()
    
    def get_recent_logs(self, db: Session, *, limit: int = 100) -> List[ActivityLog]:
        return db.query(ActivityLog).order_by(ActivityLog.created_at.desc()).limit(limit).all()

activity_log = CRUDActivityLog(ActivityLog) 