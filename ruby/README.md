# Crawlora DramaBox API client for Ruby (`crawlora-dramabox`)

This Ruby gem calls Crawlora's hosted DramaBox API at `https://api.crawlora.net/api/v1`. It exposes 16 endpoints covering title discovery, categories, search, rankings, recommendations, and public title details; it does not call or scrape DramaBox directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-dramabox"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/dramabox"

client = Crawlora::Dramabox::Client.new
result = client.request("dramabox-search", JSON.parse("{\"keyword\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 16 API operations.

```ruby
client = Crawlora::Dramabox::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported DramaBox API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-dramabox) for account setup, the API operation reference, and release history.
