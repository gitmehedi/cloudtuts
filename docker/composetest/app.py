import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='cache', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


def count_country():
    return 'Country :' + str(get_hit_count())


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


@app.route('/count/<val>')
def count_code(val):
    count = get_hit_count()
    mod = count % int(val)
    if mod:
        return "<h1>You are unlucky right now,</h1> keep try for next time."
    else:
        return "<b style='color: red;'>Wow!!!</b> you are really a lucky person. But if you want to try for next luck keep trying."


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)