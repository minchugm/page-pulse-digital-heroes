from fastapi import FastAPI

from app.models import AuditRequest, AuditResponse
from app.services.audit_service import audit_url

from fastapi import FastAPI, Request
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.limiter import limiter

app = FastAPI(
    title="Page Pulse API",
    description="Production Grade URL Audit Service",
    version="1.0.0",
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
async def root():
    return {
        "service": "Page Pulse",
        "status": "running",
        "version": "1.0.0",
    }

@app.post("/audit", response_model=AuditResponse)
@limiter.limit("10/minute")
async def audit(request: Request, audit_request: AuditRequest):
    return await audit_url(str(audit_request.url))