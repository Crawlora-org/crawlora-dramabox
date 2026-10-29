# Crawlora DramaBox JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `16`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dramabox | `dramabox.browse` | `dramabox-browse` | `GET /dramabox/browse` | `genre_id` (query number)<br>`page` (query number)<br>`language` (query "en" \| "ko" \| "zhHans" \| "zh" \| "es" \| "ja" \| "de" \| "in" \| "th" \| "tl" \| "pt" \| "fr" \| "ar" \| "it") | `ApiKeyAuth` | `DramaboxBrowseResponse` |  |
| dramabox | `dramabox.categories` | `dramabox-categories` | `GET /dramabox/categories` | none | `ApiKeyAuth` | `DramaboxCategoriesResponse` |  |
| dramabox | `dramabox.categoryBooks` | `dramabox-category-books` | `GET /dramabox/category-books` | `language` (query string)<br>`production` (query "3" \| "1" \| "2")<br>`dub` (query "1" \| "0")<br>`genre` (query string)<br>`genre_2` (query string)<br>`sort` (query "1" \| "2" \| "3")<br>`page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `DramaboxCategoryBooksResponse` |  |
| dramabox | `dramabox.channels` | `dramabox-channels` | `GET /dramabox/channels` | none | `ApiKeyAuth` | `DramaboxChannelsResponse` |  |
| dramabox | `dramabox.drama` | `dramabox-drama` | `GET /dramabox/drama` | `id` (query string required) | `ApiKeyAuth` | `DramaboxDramaResponse` |  |
| dramabox | `dramabox.genres` | `dramabox-genres` | `GET /dramabox/genres` | `language` (query "en" \| "ko" \| "zhHans" \| "zh" \| "es" \| "ja" \| "de" \| "in" \| "th" \| "tl" \| "pt" \| "fr" \| "ar" \| "it") | `ApiKeyAuth` | `DramaboxGenresResponse` |  |
| dramabox | `dramabox.home` | `dramabox-home` | `GET /dramabox/home` | `language` (query "en" \| "ko" \| "zhHans" \| "zh" \| "es" \| "ja" \| "de" \| "in" \| "th" \| "tl" \| "pt" \| "fr" \| "ar" \| "it") | `ApiKeyAuth` | `DramaboxHomeResponse` |  |
| dramabox | `dramabox.more` | `dramabox-more` | `GET /dramabox/more` | `position` (query "trending" \| "must-sees" \| "hidden-gems" required)<br>`page` (query number)<br>`language` (query "en" \| "ko" \| "zhHans" \| "zh" \| "es" \| "ja" \| "de" \| "in" \| "th" \| "tl" \| "pt" \| "fr" \| "ar" \| "it") | `ApiKeyAuth` | `DramaboxMoreResponse` |  |
| dramabox | `dramabox.performer` | `dramabox-performer` | `GET /dramabox/performer` | `performer_id` (query number required)<br>`page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `DramaboxPerformerResponse` |  |
| dramabox | `dramabox.rank` | `dramabox-rank` | `GET /dramabox/rank` | `rank_type` (query 1 \| 2 \| 3) | `ApiKeyAuth` | `DramaboxRankResponse` |  |
| dramabox | `dramabox.recommend` | `dramabox-recommend` | `GET /dramabox/recommend` | `page` (query number) | `ApiKeyAuth` | `DramaboxRecommendResponse` |  |
| dramabox | `dramabox.search` | `dramabox-search` | `GET /dramabox/search` | `keyword` (query string required)<br>`page` (query number)<br>`limit` (query number)<br>`sort` (query 1 \| 2 \| 3) | `ApiKeyAuth` | `DramaboxSearchResponse` |  |
| dramabox | `dramabox.suggest` | `dramabox-suggest` | `GET /dramabox/suggest` | `keyword` (query string required) | `ApiKeyAuth` | `DramaboxSuggestResponse` |  |
| dramabox | `dramabox.tag` | `dramabox-tag` | `GET /dramabox/tag` | `tag_id` (query number required)<br>`page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `DramaboxTagResponse` |  |
| dramabox | `dramabox.theater` | `dramabox-theater` | `GET /dramabox/theater` | `channel` (query "popular" \| "new" \| "rankings" \| "categories" \| "anime" \| "live-action" \| "vip" \| "original" required)<br>`page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `DramaboxTheaterResponse` |  |
| dramabox | `dramabox.trending` | `dramabox-trending` | `GET /dramabox/trending` | none | `ApiKeyAuth` | `DramaboxTrendingResponse` |  |
