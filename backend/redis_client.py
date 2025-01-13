"""
Redis Client Setup
- Initializes a Redis client to store scraping results
"""
import redis
from django.conf import settings

redis_client = redis.StrictRedis(
    host = settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)

def save_scraping_results(key, value):
    redis_client.set(key, value)