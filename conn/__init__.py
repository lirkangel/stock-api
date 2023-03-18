import redis as redis

from conf.cf import CONFIG
from conn.postgres_batch import PostgresWrapper
from utils.func import singleton
from logzero import logger as log


@singleton
class AppConnection:
    redis: redis = None
    psql: PostgresWrapper = None

    async def init_connections(self, config: CONFIG):
        try:
            self.redis = redis.Redis.from_url(url=config.REDIS_URL, encoding="utf-8", decode_responses=True)
            self.psql = await PostgresWrapper.create_from_uri(config.PSQL_URL)

        except Exception as e:
            log.error(e)
            raise e
