import redis
from rediscluster import RedisCluster

def connect_redis():
    startup_nodes = [{"host": "127.0.0.1", "port": "7001"},
                     {"host": "127.0.0.1", "port": "7002"},
                     {"host": "127.0.0.1", "port": "7003"}]

    try:
        rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        print("Connected to Redis Cluster")
        
        rc.set("test-key", "Hello, Redis!")
        value = rc.get("test-key")
        print(f"Retrieved value from cluster: {value}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_redis()
