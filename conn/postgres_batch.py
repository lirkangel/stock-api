import asyncpg


class PostgresWrapper:
    def __init__(self, pool):
        self.pool = pool

    async def query(self, sql, *args):
        try:
            async with self.pool.acquire() as conn:
                return await conn.fetch(sql, *args)
        except Exception as e:
            raise e

    async def prepare(self, sql, *args):
        async with self.pool.acquire() as conn:
            return await conn.prepare(sql, *args)

    @staticmethod
    async def create_from_uri(uri: str):
        pool = await asyncpg.create_pool(dsn=uri)

        return PostgresWrapper(pool)
