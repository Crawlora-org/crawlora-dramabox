# Crawlora DramaBox API client for Java

The official Java client for Crawlora's hosted DramaBox API. It exposes 16 endpoints covering title discovery, categories, search, rankings, recommendations, and public title details. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-dramabox</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-java-console) to get an API key.

```java
import net.crawlora.dramabox.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.categories(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported DramaBox API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-dramabox/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-dramabox)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-java-api-docs)
