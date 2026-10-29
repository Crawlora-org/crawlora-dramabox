"""Typed DramaBox client for the Crawlora hosted API."""

from .platform import DramaBoxClient, AsyncDramaBoxClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = DramaBoxClient
AsyncClient = AsyncDramaBoxClient
__version__ = '0.1.0'
DISPLAY_NAME = 'DramaBox'
PLATFORM = 'dramabox'
CONTRACT_REVISION = 'sha256:4e4d3a78e19ef7b79f962e66b7835707f5f41894925473e3800db244cb044487'

__all__ = [
    "DramaBoxClient", "AsyncDramaBoxClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
