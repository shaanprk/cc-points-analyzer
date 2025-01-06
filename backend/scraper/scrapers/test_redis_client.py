"""
Redis Client Test Setup Test
- Initializes a Redis client to store scraping results
"""
import redis
from django.conf import settings

redis_client = redis.StrictRedis(
    host = 'localhost',
    port= 6380,
    db= 0,
    # decode_responses=True
)

# def save_scraping_results(key, value):
#     redis_client.set(key, value)