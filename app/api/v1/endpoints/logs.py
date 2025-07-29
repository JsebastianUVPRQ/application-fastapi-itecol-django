from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.crud.activity_log import activity_log
from app.schemas.activity_log import ActivityLogCreate, ActivityLogResponse
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=ActivityLogResponse, status_code=status.HTTP_201_CREATED)
def create_log(
    *,
    db: Session = Depends(get_db),
    request: Request,
    log_in: ActivityLogCreate,
):
    """
    Crear un nuevo log de actividad.
    """
    # Obtener información del cliente
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent", "")
    
    # Actualizar con información del cliente
    log_data = log_in.dict()
    log_data["ip_address"] = client_ip
    log_data["user_agent"] = user_agent
    
    log_obj = activity_log.create(db, obj_in=ActivityLogCreate(**log_data))
    return log_obj

@router.get("/", response_model=List[ActivityLogResponse])
def read_logs(
    db: Session = Depends(get_db),
    user_id: Optional[int] = None,
    user_type: Optional[str] = None,
    resource_type: Optional[str] = None,
    resource_id: Optional[int] = None,
    action: Optional[str] = None,
    limit: int = 100,
):
    """
    Obtener lista de logs de actividad.
    """
    if user_id:
        logs = activity_log.get_by_user(db, user_id=user_id)
    elif user_type:
        logs = activity_log.get_by_user_type(db, user_type=user_type)
    elif resource_type and resource_id:
        logs = activity_log.get_by_resource(db, resource_type=resource_type, resource_id=resource_id)
    elif action:
        logs = activity_log.get_by_action(db, action=action)
    else:
        logs = activity_log.get_recent_logs(db, limit=limit)
    return logs

@router.get("/{log_id}", response_model=ActivityLogResponse)
def read_log(
    *,
    db: Session = Depends(get_db),
    log_id: int,
):
    """
    Obtener un log por ID.
    """
    log_obj = activity_log.get(db, id=log_id)
    if not log_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Log no encontrado"
        )
    return log_obj

@router.get("/recent/", response_model=List[ActivityLogResponse])
def read_recent_logs(
    db: Session = Depends(get_db),
    limit: int = 50,
):
    """
    Obtener logs recientes.
    """
    logs = activity_log.get_recent_logs(db, limit=limit)
    return logs

@router.get("/user/{user_id}/", response_model=List[ActivityLogResponse])
def read_user_logs(
    *,
    db: Session = Depends(get_db),
    user_id: int,
):
    """
    Obtener logs de un usuario específico.
    """
    logs = activity_log.get_by_user(db, user_id=user_id)
    return logs

@router.get("/resource/{resource_type}/{resource_id}/", response_model=List[ActivityLogResponse])
def read_resource_logs(
    *,
    db: Session = Depends(get_db),
    resource_type: str,
    resource_id: int,
):
    """
    Obtener logs de un recurso específico.
    """
    logs = activity_log.get_by_resource(db, resource_type=resource_type, resource_id=resource_id)
    return logs 