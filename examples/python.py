import os

from crawlora_dramabox import DramaBoxClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with DramaBoxClient(api_key=api_key) as client:
    home = client.home()
    print('home', home)
    search = client.search(keyword='romance')
    print('search', search)
