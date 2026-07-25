from typing import Optional

from pydantic import BaseModel, HttpUrl


class AuditRequest(BaseModel):
    url: HttpUrl


class AuditResponse(BaseModel):
    url: str
    status: str
    message: str
    title: Optional[str] = None
    status_code: Optional[int] = None
    response_time_ms: Optional[float] = None
    content_length: Optional[int] = None