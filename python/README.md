# crawlora-dramabox — DramaBox API client for Python

Python client for Crawlora's hosted DramaBox API. It exposes 16 API endpoints covering title discovery, categories, search, rankings, recommendations, and public title details. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-python-homepage); the package does not run a browser or scrape
DramaBox locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
DramaBox or its owners.

## Install

```sh
python -m pip install crawlora-dramabox
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_dramabox import DramaBoxClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with DramaBoxClient(api_key=api_key) as client:
    result_1 = client.home()
    print(result_1)
    result_2 = client.search(keyword='romance')
    print(result_2)
```

The package also exports `Client` as an alias for `DramaBoxClient`. Operation
methods are available directly in snake_case and through the `dramabox`
group. The async package client is `AsyncDramaBoxClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_dramabox import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.home()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/examples/python.py) for a complete usage example.

## Supported DramaBox API endpoints

This package exposes every route below through direct snake_case methods and the `dramabox` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/dramabox/browse` | `dramabox-browse` | Browse DramaBox short dramas by genre |
| `GET` | `/dramabox/categories` | `dramabox-categories` | List DramaBox category filters |
| `GET` | `/dramabox/category-books` | `dramabox-category-books` | Browse DramaBox titles by category |
| `GET` | `/dramabox/channels` | `dramabox-channels` | List DramaBox theater channels |
| `GET` | `/dramabox/drama` | `dramabox-drama` | Get a DramaBox short drama and its episodes |
| `GET` | `/dramabox/genres` | `dramabox-genres` | List DramaBox genres |
| `GET` | `/dramabox/home` | `dramabox-home` | List DramaBox's featured titles and shelves |
| `GET` | `/dramabox/more` | `dramabox-more` | Get a whole DramaBox curated shelf |
| `GET` | `/dramabox/performer` | `dramabox-performer` | Get a DramaBox performer and their titles |
| `GET` | `/dramabox/rank` | `dramabox-rank` | Get a DramaBox ranking list |
| `GET` | `/dramabox/recommend` | `dramabox-recommend` | Get a page of DramaBox's recommendation feed |
| `GET` | `/dramabox/search` | `dramabox-search` | Search DramaBox titles and performers |
| `GET` | `/dramabox/suggest` | `dramabox-suggest` | Get DramaBox search-box suggestions |
| `GET` | `/dramabox/tag` | `dramabox-tag` | List the DramaBox titles carrying a tag |
| `GET` | `/dramabox/theater` | `dramabox-theater` | Get a DramaBox theater channel feed |
| `GET` | `/dramabox/trending` | `dramabox-trending` | Get DramaBox's search landing feeds |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
