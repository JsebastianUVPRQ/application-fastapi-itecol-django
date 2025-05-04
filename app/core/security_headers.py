from fastapi import Response

security_headers = {
    "Content-Security-Policy": "default-src 'self'",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
}

async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    for header, value in security_headers.items():
        response.headers[header] = value
    return response