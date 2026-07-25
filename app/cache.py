from cachetools import TTLCache

CACHE_TTL = 60  # seconds

audit_cache = TTLCache(
    maxsize=100,
    ttl=CACHE_TTL
)