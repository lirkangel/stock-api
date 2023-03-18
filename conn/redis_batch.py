from logzero import logger as log
from pydantic import BaseModel

from conn import AppConnection


class RedisAppConnection(BaseModel):

    @staticmethod
    def get_data(key):
        conn = AppConnection()
        try:
            result = conn.redis.hgetall(key)
            return result
        except Exception as e:
            log.error(e)
            raise e

    @staticmethod
    def get_data_pipe(keys):
        conn = AppConnection()
        pipe = conn.redis.pipeline()
        pipe.multi()
        try:
            for key in keys:
                pipe.hgetall(key)
            result = [item for item in pipe.execute() if bool(item)]
            return result
        except Exception as e:
            log.error(e)
            raise e

    @staticmethod
    def save_incr_data_pipe(key: str, fields: list, data: int):
        conn = AppConnection()
        pipe = conn.redis.pipeline()
        try:
            for field in fields:
                pipe.hincrby(key, field, data)
            return pipe.execute()
        except Exception as e:
            log.error(e)
            raise e

    @staticmethod
    def save_incr_data(key: str, field: str, data: int):
        conn = AppConnection()
        try:
            return conn.redis.hincrby(key, field, data)
        except Exception as e:
            log.error(e)
            raise e

    @staticmethod
    def save_hash_data(name: str, data):
        conn = AppConnection()
        try:
            result = conn.redis.hmset(name, mapping=data)
            return result
        except Exception as e:
            log.error(e)
            raise e

    @staticmethod
    def delete_data(key):
        conn = AppConnection()
        try:
            return conn.redis.delete(*key)
        except Exception as e:
            log.error(e)
            raise e

    @staticmethod
    def scan_data(*key):
        conn = AppConnection()
        try:
            return conn.redis.scan_iter(*key)
        except Exception as e:
            log.error(e)
            raise e
