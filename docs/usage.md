# DramaBox API endpoint reference and client usage

This reference lists all 16 public DramaBox API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/dramabox`, `crawlora-dramabox`, and `crawlora-dramabox` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape DramaBox locally; Crawlora is independent from and not endorsed by DramaBox or its owners.

The package tracks the public API contract revision `sha256:4e4d3a78e19ef7b79f962e66b7835707f5f41894925473e3800db244cb044487` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `dramabox`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `browse` | `browse` | `dramabox.browse` | `GET /dramabox/browse` | `genre_id` (query, optional), `page` (query, optional), `language` (query, optional; values: `en`, `ko`, `zhHans`, `zh`, `es`, `ja`, `de`, `in`, `th`, `tl`, `pt`, `fr`, `ar`, `it`) | Browse DramaBox short dramas by genre |
| `categories` | `categories` | `dramabox.categories` | `GET /dramabox/categories` | — | List DramaBox category filters |
| `categoryBooks` | `category_books` | `dramabox.category_books` | `GET /dramabox/category-books` | `language` (query, optional), `production` (query, optional; values: `3`, `1`, `2`), `dub` (query, optional; values: `1`, `0`), `genre` (query, optional), `genre_2` (query, optional), `sort` (query, optional; values: `1`, `2`, `3`), `page` (query, optional), `limit` (query, optional) | Browse DramaBox titles by category |
| `channels` | `channels` | `dramabox.channels` | `GET /dramabox/channels` | — | List DramaBox theater channels |
| `drama` | `drama` | `dramabox.drama` | `GET /dramabox/drama` | `id` (query, required) | Get a DramaBox short drama and its episodes |
| `genres` | `genres` | `dramabox.genres` | `GET /dramabox/genres` | `language` (query, optional; values: `en`, `ko`, `zhHans`, `zh`, `es`, `ja`, `de`, `in`, `th`, `tl`, `pt`, `fr`, `ar`, `it`) | List DramaBox genres |
| `home` | `home` | `dramabox.home` | `GET /dramabox/home` | `language` (query, optional; values: `en`, `ko`, `zhHans`, `zh`, `es`, `ja`, `de`, `in`, `th`, `tl`, `pt`, `fr`, `ar`, `it`) | List DramaBox's featured titles and shelves |
| `more` | `more` | `dramabox.more` | `GET /dramabox/more` | `position` (query, required; values: `trending`, `must-sees`, `hidden-gems`), `page` (query, optional), `language` (query, optional; values: `en`, `ko`, `zhHans`, `zh`, `es`, `ja`, `de`, `in`, `th`, `tl`, `pt`, `fr`, `ar`, `it`) | Get a whole DramaBox curated shelf |
| `performer` | `performer` | `dramabox.performer` | `GET /dramabox/performer` | `performer_id` (query, required), `page` (query, optional), `limit` (query, optional) | Get a DramaBox performer and their titles |
| `rank` | `rank` | `dramabox.rank` | `GET /dramabox/rank` | `rank_type` (query, optional; values: `1`, `2`, `3`) | Get a DramaBox ranking list |
| `recommend` | `recommend` | `dramabox.recommend` | `GET /dramabox/recommend` | `page` (query, optional) | Get a page of DramaBox's recommendation feed |
| `search` | `search` | `dramabox.search` | `GET /dramabox/search` | `keyword` (query, required), `page` (query, optional), `limit` (query, optional), `sort` (query, optional; values: `1`, `2`, `3`) | Search DramaBox titles and performers |
| `suggest` | `suggest` | `dramabox.suggest` | `GET /dramabox/suggest` | `keyword` (query, required) | Get DramaBox search-box suggestions |
| `tag` | `tag` | `dramabox.tag` | `GET /dramabox/tag` | `tag_id` (query, required), `page` (query, optional), `limit` (query, optional) | List the DramaBox titles carrying a tag |
| `theater` | `theater` | `dramabox.theater` | `GET /dramabox/theater` | `channel` (query, required; values: `popular`, `new`, `rankings`, `categories`, `anime`, `live-action`, `vip`, `original`), `page` (query, optional), `limit` (query, optional) | Get a DramaBox theater channel feed |
| `trending` | `trending` | `dramabox.trending` | `GET /dramabox/trending` | — | Get DramaBox's search landing feeds |

## Client forms

- JavaScript: import `DramaBoxClient` (also exported as `Client`) from `@crawlora-org/dramabox`; use `new DramaBoxClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `DramaBoxClient` (also exported as `Client`) from `crawlora_dramabox`; use `with DramaBoxClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncDramaBoxClient`, used with `async with` and `await`.
- Rust: add `crawlora-dramabox` with Cargo; import `Client` and the generated operation parameter struct, then call `client.dramabox.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
