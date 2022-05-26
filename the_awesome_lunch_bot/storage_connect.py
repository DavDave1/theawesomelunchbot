from sqlite3 import connect
import redis
from decouple import config

REDIS_URL = config("REDIS_URL")


class StorageConnect(object):
    _instance = None

    connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageConnect, cls).__new__(cls)
            cls._instance.connection = redis.Redis(REDIS_URL)

        return cls._instance
