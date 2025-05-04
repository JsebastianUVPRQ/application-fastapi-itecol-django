from redis.asyncio import Redis
from core.config import settings

redis_client: Redis = None

async def get_redis():
    return redis_client

async def connect_redis():
    global redis_client
    redis_client = Redis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True
    )

async def close_redis():
    await redis_client.close()