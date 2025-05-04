from fastapi import APIRouter
from core.redis import get_redis
from sqlalchemy import text

router = APIRouter()

@router.get("/health")
async def full_health_check(db: Session = Depends(get_db)):
    services = {
        "database": False,
        "redis": False,
        "external_api": False
    }
    
    # Verificar base de datos
    try:
        db.execute(text("SELECT 1"))
        services["database"] = True
    except:
        pass
    
    # Verificar Redis
    try:
        redis = await get_redis()
        await redis.ping()
        services["redis"] = True
    except:
        pass
    
    return {"status": "ok" if all(services.values()) else "degraded", "services": services}