from uuid import uuid4
import time

import redis
from flask import Flask, jsonify

app_id = str(uuid4())

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr(f'{app_id}:hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def index():
    count = get_hit_count()
    return jsonify({
        'app_id': app_id, 
        'type': 'web',
        'status': 'Ok',
        'hits': count
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


