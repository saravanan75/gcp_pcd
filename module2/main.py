from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.environ.get("REDIS_HOST", "localhost")
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    visits = cache.incr("counter")
    return f"Hello! You've visited {visits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

~                                         