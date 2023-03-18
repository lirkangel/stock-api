import aiohttp


class AioHttpClient:
    session = None

    @staticmethod
    def init():
        AioHttpClient.session = aiohttp.ClientSession()

    @staticmethod
    async def close():
        if AioHttpClient.session:
            await AioHttpClient.session.close()
            AioHttpClient.session = None

    @staticmethod
    async def get(url: str, **kwargs):
        async with AioHttpClient.session.get(url, **kwargs) as resp:
            return await resp.json(content_type=None)

    @staticmethod
    async def post(url: str, **kwargs):
        async with AioHttpClient.session.post(url, **kwargs) as resp:
            return await resp.text()

