from worker import add

result = add.delay(4, 8)

print("Task result:", result.get(timeout=10))
