# Crawlora DramaBox Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `16`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dramabox | `dramabox.browse` | `dramabox-browse` | `GET /dramabox/browse` | `genre_id` (query i64)<br>`page` (query i64)<br>`language` (query String enum{en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it}) | `ApiKeyAuth` | `DramaboxBrowseResponse` |  |
| dramabox | `dramabox.categories` | `dramabox-categories` | `GET /dramabox/categories` | none | `ApiKeyAuth` | `DramaboxCategoriesResponse` |  |
| dramabox | `dramabox.category_books` | `dramabox-category-books` | `GET /dramabox/category-books` | `language` (query String)<br>`production` (query String enum{3, 1, 2})<br>`dub` (query String enum{1, 0})<br>`genre` (query String)<br>`genre_2` (query String)<br>`sort` (query String enum{1, 2, 3})<br>`page` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `DramaboxCategoryBooksResponse` |  |
| dramabox | `dramabox.channels` | `dramabox-channels` | `GET /dramabox/channels` | none | `ApiKeyAuth` | `DramaboxChannelsResponse` |  |
| dramabox | `dramabox.drama` | `dramabox-drama` | `GET /dramabox/drama` | `id` (query String required) | `ApiKeyAuth` | `DramaboxDramaResponse` |  |
| dramabox | `dramabox.genres` | `dramabox-genres` | `GET /dramabox/genres` | `language` (query String enum{en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it}) | `ApiKeyAuth` | `DramaboxGenresResponse` |  |
| dramabox | `dramabox.home` | `dramabox-home` | `GET /dramabox/home` | `language` (query String enum{en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it}) | `ApiKeyAuth` | `DramaboxHomeResponse` |  |
| dramabox | `dramabox.more` | `dramabox-more` | `GET /dramabox/more` | `position` (query String enum{trending, must-sees, hidden-gems} required)<br>`page` (query i64)<br>`language` (query String enum{en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it}) | `ApiKeyAuth` | `DramaboxMoreResponse` |  |
| dramabox | `dramabox.performer` | `dramabox-performer` | `GET /dramabox/performer` | `performer_id` (query i64 required)<br>`page` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `DramaboxPerformerResponse` |  |
| dramabox | `dramabox.rank` | `dramabox-rank` | `GET /dramabox/rank` | `rank_type` (query String enum{1, 2, 3}) | `ApiKeyAuth` | `DramaboxRankResponse` |  |
| dramabox | `dramabox.recommend` | `dramabox-recommend` | `GET /dramabox/recommend` | `page` (query i64) | `ApiKeyAuth` | `DramaboxRecommendResponse` |  |
| dramabox | `dramabox.search` | `dramabox-search` | `GET /dramabox/search` | `keyword` (query String required)<br>`page` (query i64)<br>`limit` (query i64)<br>`sort` (query String enum{1, 2, 3}) | `ApiKeyAuth` | `DramaboxSearchResponse` |  |
| dramabox | `dramabox.suggest` | `dramabox-suggest` | `GET /dramabox/suggest` | `keyword` (query String required) | `ApiKeyAuth` | `DramaboxSuggestResponse` |  |
| dramabox | `dramabox.tag` | `dramabox-tag` | `GET /dramabox/tag` | `tag_id` (query i64 required)<br>`page` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `DramaboxTagResponse` |  |
| dramabox | `dramabox.theater` | `dramabox-theater` | `GET /dramabox/theater` | `channel` (query String enum{popular, new, rankings, categories, anime, live-action, vip, original} required)<br>`page` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `DramaboxTheaterResponse` |  |
| dramabox | `dramabox.trending` | `dramabox-trending` | `GET /dramabox/trending` | none | `ApiKeyAuth` | `DramaboxTrendingResponse` |  |
