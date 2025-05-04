from fastapi import Request
import time
import structlog

logger = structlog.get_logger()

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    log_data = {
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "process_time": process_time,
        "client_ip": request.client.host,
        "user_agent": request.headers.get("user-agent")
    }
    
    logger.info("request_handled", **log_data)
    
    if response.status_code >= 500:
        logger.error("server_error", **log_data)
    elif response.status_code >= 400:
        logger.warning("client_error", **log_data)
    
    return response