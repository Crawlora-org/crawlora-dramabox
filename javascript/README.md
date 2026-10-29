# @crawlora-org/dramabox — DramaBox API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted DramaBox API.
It exposes 16 API endpoints for title discovery, categories, search, rankings, recommendations, and public title details through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-javascript-homepage). It does not run a browser or scrape DramaBox locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by DramaBox or its owners.

## Install

```sh
npm install @crawlora-org/dramabox
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { DramaBoxClient } from "@crawlora-org/dramabox";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new DramaBoxClient({ apiKey });
const result1 = await client.home({});
console.log(result1);
const result2 = await client.search({ keyword: "romance" });
console.log(result2);
```

The client also exports `Client` as an alias for `DramaBoxClient`. Operation
methods are available directly in camelCase and through the `dramabox`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported DramaBox API endpoints

This package exposes each route below as a direct method and through the `dramabox` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
