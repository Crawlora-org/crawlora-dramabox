package net.crawlora.dramabox;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the DramaBox endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 16;
    public static final List<String> OPERATION_IDS = List.of(
            "dramabox-browse",
            "dramabox-categories",
            "dramabox-category-books",
            "dramabox-channels",
            "dramabox-drama",
            "dramabox-genres",
            "dramabox-home",
            "dramabox-more",
            "dramabox-performer",
            "dramabox-rank",
            "dramabox-recommend",
            "dramabox-search",
            "dramabox-suggest",
            "dramabox-tag",
            "dramabox-theater",
            "dramabox-trending"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("dramabox-browse", new Operation("dramabox-browse", "GET", "/dramabox/browse", Map.ofEntries(Map.entry("genre_id", new Param("genre_id", "query", false, "integer", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("language", new Param("language", "query", false, "string", List.of("en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"), "csv"))), List.of("application/json")));
        operations.put("dramabox-categories", new Operation("dramabox-categories", "GET", "/dramabox/categories", Map.of(), List.of("application/json")));
        operations.put("dramabox-category-books", new Operation("dramabox-category-books", "GET", "/dramabox/category-books", Map.ofEntries(Map.entry("language", new Param("language", "query", false, "string", List.of(), "csv")), Map.entry("production", new Param("production", "query", false, "string", List.of("3", "1", "2"), "csv")), Map.entry("dub", new Param("dub", "query", false, "string", List.of("1", "0"), "csv")), Map.entry("genre", new Param("genre", "query", false, "string", List.of(), "csv")), Map.entry("genre_2", new Param("genre_2", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("1", "2", "3"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("dramabox-channels", new Operation("dramabox-channels", "GET", "/dramabox/channels", Map.of(), List.of("application/json")));
        operations.put("dramabox-drama", new Operation("dramabox-drama", "GET", "/dramabox/drama", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("dramabox-genres", new Operation("dramabox-genres", "GET", "/dramabox/genres", Map.ofEntries(Map.entry("language", new Param("language", "query", false, "string", List.of("en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"), "csv"))), List.of("application/json")));
        operations.put("dramabox-home", new Operation("dramabox-home", "GET", "/dramabox/home", Map.ofEntries(Map.entry("language", new Param("language", "query", false, "string", List.of("en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"), "csv"))), List.of("application/json")));
        operations.put("dramabox-more", new Operation("dramabox-more", "GET", "/dramabox/more", Map.ofEntries(Map.entry("position", new Param("position", "query", true, "string", List.of("trending", "must-sees", "hidden-gems"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("language", new Param("language", "query", false, "string", List.of("en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"), "csv"))), List.of("application/json")));
        operations.put("dramabox-performer", new Operation("dramabox-performer", "GET", "/dramabox/performer", Map.ofEntries(Map.entry("performer_id", new Param("performer_id", "query", true, "integer", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("dramabox-rank", new Operation("dramabox-rank", "GET", "/dramabox/rank", Map.ofEntries(Map.entry("rank_type", new Param("rank_type", "query", false, "integer", List.of("1", "2", "3"), "csv"))), List.of("application/json")));
        operations.put("dramabox-recommend", new Operation("dramabox-recommend", "GET", "/dramabox/recommend", Map.ofEntries(Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("dramabox-search", new Operation("dramabox-search", "GET", "/dramabox/search", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "integer", List.of("1", "2", "3"), "csv"))), List.of("application/json")));
        operations.put("dramabox-suggest", new Operation("dramabox-suggest", "GET", "/dramabox/suggest", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("dramabox-tag", new Operation("dramabox-tag", "GET", "/dramabox/tag", Map.ofEntries(Map.entry("tag_id", new Param("tag_id", "query", true, "integer", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("dramabox-theater", new Operation("dramabox-theater", "GET", "/dramabox/theater", Map.ofEntries(Map.entry("channel", new Param("channel", "query", true, "string", List.of("popular", "new", "rankings", "categories", "anime", "live-action", "vip", "original"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("dramabox-trending", new Operation("dramabox-trending", "GET", "/dramabox/trending", Map.of(), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown DramaBox operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object browse(Map<String, ?> params) { return request("dramabox-browse", params); }
    public Object categories(Map<String, ?> params) { return request("dramabox-categories", params); }
    public Object categoryBooks(Map<String, ?> params) { return request("dramabox-category-books", params); }
    public Object channels(Map<String, ?> params) { return request("dramabox-channels", params); }
    public Object drama(Map<String, ?> params) { return request("dramabox-drama", params); }
    public Object genres(Map<String, ?> params) { return request("dramabox-genres", params); }
    public Object home(Map<String, ?> params) { return request("dramabox-home", params); }
    public Object more(Map<String, ?> params) { return request("dramabox-more", params); }
    public Object performer(Map<String, ?> params) { return request("dramabox-performer", params); }
    public Object rank(Map<String, ?> params) { return request("dramabox-rank", params); }
    public Object recommend(Map<String, ?> params) { return request("dramabox-recommend", params); }
    public Object search(Map<String, ?> params) { return request("dramabox-search", params); }
    public Object suggest(Map<String, ?> params) { return request("dramabox-suggest", params); }
    public Object tag(Map<String, ?> params) { return request("dramabox-tag", params); }
    public Object theater(Map<String, ?> params) { return request("dramabox-theater", params); }
    public Object trending(Map<String, ?> params) { return request("dramabox-trending", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
