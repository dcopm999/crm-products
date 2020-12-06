import logging
import zlib
import asyncio
import aiohttp

from allauth.socialaccount.models import SocialToken

logger = logging.getLogger(__name__)


class ApiBase:
    compress: bool = True
    ssl: bool = True

    def __init__(self):
        self._session = aiohttp.ClientSession()
        self._loop = asyncio.get_event_loop()
        self._headers = {
            'Content-type': 'application/json',
        }

    async def get(self, url, params=None):
        async with self._session.get(url, params=params, ssl=self.ssl) as response:
            print(response)
            try:
                result = await response.json()
            except aiohttp.ContentTypeError:
                result = await response.text()
            finally:
                return result

    async def post(self, url, data):
        if self.compress:
            headers = self._headers['Content-Encoding'] = 'deflate'
            data = zlib.compress(data)
        else:
            headers = self._headers

        async with self._session.post(url, data=data, ssl=self.ssl, headers=headers) as response:
            return await response.json()


class ApiVK(ApiBase):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ApiVK, cls).__new__(cls)
            return cls.instance

    def __init__(self):
        super(ApiVK, self).__init__()
        self._url = 'https://api.vk.com/method/'
        self._vk_api_version = '5.124'

        self._client = SocialToken.objects.get(app__provider='vk')
        self._client_id = int(self._client.app.client_id)
        self._client_token = self._client.token
        self.params = {'owner_id': self._client_id, 'access_token': self._client_token, 'v': self._vk_api_version}

    async def get_product_list(self):
        method = 'market.get'
        url = self._url + method
        print(self.params)
        return await self.get(url, params=self.params)

    async def get_categoty_list(self, count=10):
        method = 'market.getCategories'
        url = self._url + method
        params = self.params
        params.update(count=count)
        result = await self.get(url, params=params)
        return result.get('response').get('items')

    async def get_group_list(self):
        method = 'groups.get'
        url = self._url + method
        return await self.get(url, params=self.params)
