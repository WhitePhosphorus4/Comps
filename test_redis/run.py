import time 
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis')   # for docker-compose
# cache = redis.Redis(host='localhost', port=14321)   # for local computer

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as e:
            if retries == 0:
                raise e 
            retries -= 1 
            time.sleep(0.5)
        except Exception as e:
            print(e)
            return "Error"

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! You are running this app in local computer! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)