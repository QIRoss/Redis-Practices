import redis
import time

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def set_cache(key, value, expiration_in_seconds):
    """Set a key-value pair in Redis cache with an expiration time."""
    cache.setex(key, expiration_in_seconds, value)
    print(f"Cached {key} = {value} for {expiration_in_seconds} seconds.")

def get_cache(key):
    """Retrieve a value from Redis cache by its key."""
    value = cache.get(key)
    if value:
        print(f"Retrieved {key} = {value.decode('utf-8')} from cache.")
    else:
        print(f"{key} does not exist or has expired.")
    return value

if __name__ == "__main__":
    set_cache("username", "qiross", 10)
    
    get_cache("username")

    time.sleep(12)

    get_cache("username")
