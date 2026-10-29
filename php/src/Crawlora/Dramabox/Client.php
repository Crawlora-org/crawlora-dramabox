<?php

declare(strict_types=1);

namespace Crawlora\Dramabox;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'dramabox';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 16;
    public const OPERATION_IDS = ["dramabox-browse", "dramabox-categories", "dramabox-category-books", "dramabox-channels", "dramabox-drama", "dramabox-genres", "dramabox-home", "dramabox-more", "dramabox-performer", "dramabox-rank", "dramabox-recommend", "dramabox-search", "dramabox-suggest", "dramabox-tag", "dramabox-theater", "dramabox-trending"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"dramabox-browse": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-browse", "method": "GET", "params": [{"description": "Genre id from dramabox-genres; 0 or omitted browses all titles", "in": "query", "name": "genre_id", "type": "integer", "x-example": 161}, {"description": "Page number, 1 to 1000; defaults to 1. Each page holds 12 titles", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/browse", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "genre_id", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-categories": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-categories", "method": "GET", "params": [], "path": "/dramabox/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "dramabox-category-books": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-category-books", "method": "GET", "params": [{"description": "Language/origin value from dramabox-categories' language group, e.g. 美国 (Local) or 中国 (Chinese)", "in": "query", "name": "language", "type": "string", "x-example": "美国"}, {"description": "Production-type value from dramabox-categories' production group: 3 (AI Drama), 1 (Live-Action), 2 (Anime)", "enum": ["3", "1", "2"], "in": "query", "name": "production", "type": "string", "x-example": "1"}, {"description": "Dub-mode value from dramabox-categories' dub group: 1 (Dubbed), 0 (Subtitles Only)", "enum": ["1", "0"], "in": "query", "name": "dub", "type": "string", "x-example": "1"}, {"description": "Genre value from dramabox-categories' genre_1 group, e.g. 1357 (Romance) or 1361 (Strong Heroine)", "in": "query", "name": "genre", "type": "string", "x-example": "1357"}, {"description": "Genre value from dramabox-categories' genre_2 group, e.g. 1392 (Second Chance) or 1359 (BL); multi-tag values such as 1324,1362 are one value", "in": "query", "name": "genre_2", "type": "string", "x-example": "1392"}, {"description": "Sort value from dramabox-categories' sort group: 1 (Trending), 2 (Latest), 3 (Unwatched)", "enum": ["1", "2", "3"], "in": "query", "name": "sort", "type": "string", "x-example": "1"}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Titles per page, 1 to 50; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/dramabox/category-books", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "language", "type": "string"}, {"enum": ["3", "1", "2"], "in": "query", "name": "production", "type": "string"}, {"enum": ["1", "0"], "in": "query", "name": "dub", "type": "string"}, {"in": "query", "name": "genre", "type": "string"}, {"in": "query", "name": "genre_2", "type": "string"}, {"enum": ["1", "2", "3"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-channels": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-channels", "method": "GET", "params": [], "path": "/dramabox/channels", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "dramabox-drama": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-drama", "method": "GET", "params": [{"description": "Title id (digits) from any DramaBox list, or a dramabox.com drama URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "42000028173"}], "path": "/dramabox/drama", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-genres": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-genres", "method": "GET", "params": [{"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/genres", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-home": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-home", "method": "GET", "params": [{"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-more": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-more", "method": "GET", "params": [{"description": "Curated shelf: trending, must-sees or hidden-gems", "enum": ["trending", "must-sees", "hidden-gems"], "in": "query", "name": "position", "required": true, "type": "string", "x-example": "trending"}, {"description": "Page number, 1 to 1000; defaults to 1. Each page holds 18 titles", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/more", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["trending", "must-sees", "hidden-gems"], "in": "query", "name": "position", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-performer": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-performer", "method": "GET", "params": [{"description": "Performer id from dramabox-search or dramabox-suggest's people results", "in": "query", "name": "performer_id", "required": true, "type": "integer", "x-example": 29450}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 20; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/dramabox/performer", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "performer_id", "required": true, "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-rank": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-rank", "method": "GET", "params": [{"description": "Ranking tab: 1 (Most Trending), 2 (Top Searched), 3 (New Releases); omit for the default tab", "enum": [1, 2, 3], "in": "query", "name": "rank_type", "type": "integer", "x-example": 2}], "path": "/dramabox/rank", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["1", "2", "3"], "in": "query", "name": "rank_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-recommend": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-recommend", "method": "GET", "params": [{"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}], "path": "/dramabox/recommend", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-search": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-search", "method": "GET", "params": [{"description": "Search text, trimmed and truncated to 80 characters", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "love"}, {"default": 1, "description": "One-based result page", "in": "query", "maximum": 1000, "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Results per page", "in": "query", "maximum": 50, "minimum": 1, "name": "limit", "type": "integer"}, {"description": "Upstream result ordering mode; omit for the app default", "enum": [1, 2, 3], "in": "query", "name": "sort", "type": "integer", "x-example": 1}], "path": "/dramabox/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"enum": ["1", "2", "3"], "in": "query", "name": "sort", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-suggest": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-suggest", "method": "GET", "params": [{"description": "Partial search text, trimmed and truncated to 80 characters", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lov"}], "path": "/dramabox/suggest", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-tag": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-tag", "method": "GET", "params": [{"description": "Tag id from any title result's tag_refs", "in": "query", "name": "tag_id", "required": true, "type": "integer", "x-example": 1379}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 50; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/dramabox/tag", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tag_id", "required": true, "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-theater": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-theater", "method": "GET", "params": [{"description": "Theater channel: popular, new, rankings, categories, anime, live-action, vip or original", "enum": ["popular", "new", "rankings", "categories", "anime", "live-action", "vip", "original"], "in": "query", "name": "channel", "required": true, "type": "string", "x-example": "popular"}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Titles per paged block, 1 to 20; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/dramabox/theater", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["popular", "new", "rankings", "categories", "anime", "live-action", "vip", "original"], "in": "query", "name": "channel", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-trending": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-trending", "method": "GET", "params": [], "path": "/dramabox/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-dramabox-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function browse(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-browse", $params, $responseType);
    }
    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-categories", $params, $responseType);
    }
    public function category_books(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-category-books", $params, $responseType);
    }
    public function channels(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-channels", $params, $responseType);
    }
    public function drama(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-drama", $params, $responseType);
    }
    public function genres(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-genres", $params, $responseType);
    }
    public function home(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-home", $params, $responseType);
    }
    public function more(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-more", $params, $responseType);
    }
    public function performer(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-performer", $params, $responseType);
    }
    public function rank(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-rank", $params, $responseType);
    }
    public function recommend(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-recommend", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-search", $params, $responseType);
    }
    public function suggest(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-suggest", $params, $responseType);
    }
    public function tag(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-tag", $params, $responseType);
    }
    public function theater(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-theater", $params, $responseType);
    }
    public function trending(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("dramabox-trending", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
