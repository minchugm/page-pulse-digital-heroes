import asyncio

MAX_CONCURRENT_AUDITS = 5

audit_semaphore = asyncio.Semaphore(MAX_CONCURRENT_AUDITS)