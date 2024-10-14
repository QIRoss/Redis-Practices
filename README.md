# Redis Practices

Alternative studies based in day 35-36 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 31–40: Scalability and Performance Optimization

Day 35–36: Implement and tune a Redis cluster for high performance and scalability.

This repository contains three small examples of using Redis in different ways:

1. **Celery Worker with Redis as a Message Broker**
2. **Redis Cluster Example**
3. **Redis as a Pure Cache**

Each example demonstrates specific use cases for Redis, from task management in Celery to using Redis purely for caching purposes.

## 1. Celery Worker with Redis as a Message Broker

This example demonstrates how to use Redis as a message broker for a Celery worker. The worker listens for tasks and processes them asynchronously. Redis handles the queuing of tasks.

### Key Files:
- `worker.py`: Defines a Celery worker using Redis as a broker.
- `send_task.py`: Sends a sample task to the Celery worker.
- `docker-compose.yml`: Defines the services for Redis and Celery.

### Usage:
1. Ensure Docker is installed.
2. Run the services:
```
docker-compose up --build
```
3. Send a task to the Celery worker.
```
docker exec -ti <celery-container-name> bash
python send_task.py
```

## 2. Redis Cluster Example
This example shows how to set up a Redis cluster with multiple nodes using Docker Compose. A Redis cluster improves availability and scalability by splitting the data into multiple nodes.

Key Files:
cluster_example.py: A script that connects to the Redis cluster and performs operations.
docker-compose.yml: Defines multiple Redis nodes for the cluster.
Usage:
1. Start the Redis cluster:
```
docker-compose up --build
```
2. Run the cluster_example.py script to perform operations on the cluster:
```
python cluster_example.py
```
Expected Output:
The script should connect to the Redis cluster and show data being distributed across the nodes.

## 3. Redis as a Pure Cache

This example demonstrates how to use Redis as a cache for temporary storage. It shows how to set key-value pairs with expiration and retrieve them before they expire.

Key Files:
* cache_example.py: A Python script that sets and retrieves cache values from Redis.

Usage:
1. Start Redis (either locally or using Docker).
2. Run the cache example:
```
python cache_example.py
```
Expected Output:
* The script caches a username for 10 seconds, retrieves it immediately, and then checks if it has expired after 12 seconds.
* You should see something like:
```
Cached username = qiross for 10 seconds.
Retrieved username = qiross from cache.
username does not exist or has expired.
```
### Prerequisites
* Python 3.9+
* Docker & Docker Compose
* Redis installed locally or using Docker
### Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/redis-practices.git
```
2. Install dependencies:
```
pip install -r requirements.txt
```

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"
