# DramaBox clients for Crawlora

Official Crawlora client packages for the hosted DramaBox API. Access 16 API endpoints covering title discovery, categories, search, rankings, recommendations, and public title details from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape DramaBox locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by DramaBox or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/dramabox`](javascript/README.md)
- Python: [`crawlora-dramabox`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-dramabox`](go.mod)
- Ruby: [`crawlora-dramabox`](ruby/README.md)
- Java: [`net.crawlora:crawlora-dramabox:0.1.0`](java/README.md)
- PHP: [`crawlora/dramabox`](php/README.md)
- Rust: [`crawlora-dramabox`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 16 selected public DramaBox API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
