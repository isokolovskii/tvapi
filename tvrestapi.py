from api import app
from config import config


# TODO Fix programme requests

if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'])
