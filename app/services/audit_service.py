import time

import httpx
from bs4 import BeautifulSoup
from app.concurrency import audit_semaphore
from app.cache import audit_cache
from app.models import AuditResponse

REQUEST_TIMEOUT = 10


async def audit_url(url: str) -> AuditResponse:
    # Check cache first
    if url in audit_cache:
        cached_response = audit_cache[url]
        cached_response.message = "Returned from cache"
        return cached_response

    start_time = time.perf_counter()

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        }
        async with audit_semaphore:

            async with httpx.AsyncClient(
                timeout=REQUEST_TIMEOUT,
                headers=headers,
                follow_redirects=True,
            ) as client:
                response = await client.get(url)

                end_time = time.perf_counter()

                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.title.string.strip() if soup.title else None

                audit_result = AuditResponse(
                    url=url,
                    status="success",
                    message="Audit completed successfully",
                    title=title,
                    status_code=response.status_code,
                    response_time_ms=round((end_time - start_time) * 1000, 2),
                    content_length=len(response.content),
                )

                # Save result in cache
                audit_cache[url] = audit_result

                return audit_result

    except httpx.TimeoutException:
        return AuditResponse(
            url=url,
            status="error",
            message="Request timed out.",
        )

    except httpx.ConnectError:
        return AuditResponse(
            url=url,
            status="error",
            message="Unable to connect to the target website.",
        )

    except Exception as e:
        return AuditResponse(
            url=url,
            status="error",
            message=str(e),
        )