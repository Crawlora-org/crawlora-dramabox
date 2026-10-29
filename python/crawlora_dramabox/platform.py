"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class DramaBoxClient(CrawloraClient):
    """Synchronous DramaBox API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-dramabox-python/0.1.0')
        super().__init__(*args, **kwargs)

    def browse(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-browse', params, response_type=response_type, timeout=timeout, headers=headers)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def category_books(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-category-books', params, response_type=response_type, timeout=timeout, headers=headers)

    def channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    def drama(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-drama', params, response_type=response_type, timeout=timeout, headers=headers)

    def genres(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-genres', params, response_type=response_type, timeout=timeout, headers=headers)

    def home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-home', params, response_type=response_type, timeout=timeout, headers=headers)

    def more(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-more', params, response_type=response_type, timeout=timeout, headers=headers)

    def performer(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-performer', params, response_type=response_type, timeout=timeout, headers=headers)

    def rank(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-rank', params, response_type=response_type, timeout=timeout, headers=headers)

    def recommend(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-recommend', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

    def tag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-tag', params, response_type=response_type, timeout=timeout, headers=headers)

    def theater(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-theater', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('dramabox-trending', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncDramaBoxClient(AsyncCrawloraClient):
    """Asynchronous DramaBox API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-dramabox-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def browse(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-browse', params, response_type=response_type, timeout=timeout, headers=headers)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category_books(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-category-books', params, response_type=response_type, timeout=timeout, headers=headers)

    async def channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    async def drama(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-drama', params, response_type=response_type, timeout=timeout, headers=headers)

    async def genres(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-genres', params, response_type=response_type, timeout=timeout, headers=headers)

    async def home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-home', params, response_type=response_type, timeout=timeout, headers=headers)

    async def more(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-more', params, response_type=response_type, timeout=timeout, headers=headers)

    async def performer(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-performer', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rank(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-rank', params, response_type=response_type, timeout=timeout, headers=headers)

    async def recommend(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-recommend', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-tag', params, response_type=response_type, timeout=timeout, headers=headers)

    async def theater(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-theater', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('dramabox-trending', params, response_type=response_type, timeout=timeout, headers=headers)
