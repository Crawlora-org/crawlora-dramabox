from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelDramaboxTrendingResponseDoc = TypedDict('ModelDramaboxTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxTrendingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxTrendingResponse = TypedDict('ModelDramaboxTrendingResponse', {
    'hot': NotRequired[list[ModelDramaboxAppTitle]],
    'new_releases': NotRequired[list[ModelDramaboxAppTitle]],
    'preset_keyword': NotRequired[str],
    'rank_tabs': NotRequired[list[ModelDramaboxRankTab]],
    'trending': NotRequired[list[ModelDramaboxAppTitle]],
}, total=False)

ModelDramaboxAppTitle = TypedDict('ModelDramaboxAppTitle', {
    'cover_url': NotRequired[str],
    'description': NotRequired[str],
    'episodes': NotRequired[int],
    'id': NotRequired[str],
    'in_library': NotRequired[bool],
    'play_count': NotRequired[int],
    'protagonist': NotRequired[str],
    'shelf_time': NotRequired[str],
    'shelf_time_ms': NotRequired[int],
    'tag_refs': NotRequired[list[ModelDramaboxAppTagRef]],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelDramaboxAppTagRef = TypedDict('ModelDramaboxAppTagRef', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelDramaboxRankTab = TypedDict('ModelDramaboxRankTab', {
    'name': NotRequired[str],
    'type': NotRequired[int],
}, total=False)

ModelDramaboxTheaterResponseDoc = TypedDict('ModelDramaboxTheaterResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxTheaterResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxTheaterResponse = TypedDict('ModelDramaboxTheaterResponse', {
    'banners': NotRequired[list[ModelDramaboxTheaterBanner]],
    'channel': NotRequired[ModelDramaboxChannel],
    'has_more': NotRequired[bool],
    'hot_words': NotRequired[list[str]],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'sections': NotRequired[list[ModelDramaboxTheaterSection]],
}, total=False)

ModelDramaboxTheaterSection = TypedDict('ModelDramaboxTheaterSection', {
    'style': NotRequired[str],
    'title': NotRequired[str],
    'titles': NotRequired[list[ModelDramaboxAppTitle]],
}, total=False)

ModelDramaboxChannel = TypedDict('ModelDramaboxChannel', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelDramaboxTheaterBanner = TypedDict('ModelDramaboxTheaterBanner', {
    'image_url': NotRequired[str],
    'title': NotRequired[str],
    'title_id': NotRequired[str],
}, total=False)

ModelDramaboxTagResponseDoc = TypedDict('ModelDramaboxTagResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxTagResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxTagResponse = TypedDict('ModelDramaboxTagResponse', {
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'tag_id': NotRequired[int],
    'tag_name': NotRequired[str],
    'titles': NotRequired[list[ModelDramaboxAppTitle]],
}, total=False)

ModelDramaboxSuggestResponseDoc = TypedDict('ModelDramaboxSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxSuggestResponse = TypedDict('ModelDramaboxSuggestResponse', {
    'items': NotRequired[list[ModelDramaboxSuggestItem]],
    'keyword': NotRequired[str],
}, total=False)

ModelDramaboxSuggestItem = TypedDict('ModelDramaboxSuggestItem', {
    'avatar': NotRequired[str],
    'cover_url': NotRequired[str],
    'id': NotRequired[str],
    'kind': NotRequired[str],
    'name': NotRequired[str],
    'videos': NotRequired[int],
}, total=False)

ModelDramaboxSearchResponseDoc = TypedDict('ModelDramaboxSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxSearchResponse = TypedDict('ModelDramaboxSearchResponse', {
    'is_more': NotRequired[bool],
    'keyword': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'people': NotRequired[list[ModelDramaboxSearchPerson]],
    'titles': NotRequired[list[ModelDramaboxAppTitle]],
}, total=False)

ModelDramaboxSearchPerson = TypedDict('ModelDramaboxSearchPerson', {
    'avatar': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'videos': NotRequired[int],
}, total=False)

ModelDramaboxRecommendResponseDoc = TypedDict('ModelDramaboxRecommendResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxRecommendResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxRecommendResponse = TypedDict('ModelDramaboxRecommendResponse', {
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'title': NotRequired[str],
    'titles': NotRequired[list[ModelDramaboxAppTitle]],
}, total=False)

ModelDramaboxRankResponseDoc = TypedDict('ModelDramaboxRankResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxRankResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxRankResponse = TypedDict('ModelDramaboxRankResponse', {
    'rank_type': NotRequired[int],
    'tabs': NotRequired[list[ModelDramaboxRankTab]],
    'titles': NotRequired[list[ModelDramaboxRankedTitle]],
}, total=False)

ModelDramaboxRankedTitle = TypedDict('ModelDramaboxRankedTitle', {
    'cover_url': NotRequired[str],
    'data_from': NotRequired[str],
    'description': NotRequired[str],
    'episodes': NotRequired[int],
    'id': NotRequired[str],
    'in_library': NotRequired[bool],
    'position': NotRequired[int],
    'protagonist': NotRequired[str],
    'rank': NotRequired[ModelDramaboxRankMeta],
    'shelf_time': NotRequired[str],
    'shelf_time_ms': NotRequired[int],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelDramaboxRankMeta = TypedDict('ModelDramaboxRankMeta', {
    'hot_code': NotRequired[str],
    'sort': NotRequired[int],
    'type': NotRequired[int],
}, total=False)

ModelDramaboxPerformerResponseDoc = TypedDict('ModelDramaboxPerformerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxPerformerResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxPerformerResponse = TypedDict('ModelDramaboxPerformerResponse', {
    'avatar': NotRequired[str],
    'followed': NotRequired[bool],
    'gender': NotRequired[int],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'name': NotRequired[str],
    'page': NotRequired[int],
    'titles': NotRequired[list[ModelDramaboxAppTitle]],
    'video_count': NotRequired[int],
}, total=False)

ModelDramaboxMoreResponseDoc = TypedDict('ModelDramaboxMoreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxMoreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxMoreResponse = TypedDict('ModelDramaboxMoreResponse', {
    'books': NotRequired[list[ModelDramaboxBook]],
    'language': NotRequired[str],
    'name': NotRequired[str],
    'page': NotRequired[int],
    'position': NotRequired[str],
    'total_pages': NotRequired[int],
}, total=False)

ModelDramaboxBook = TypedDict('ModelDramaboxBook', {
    'cover_url': NotRequired[str],
    'description': NotRequired[str],
    'episodes': NotRequired[int],
    'follows': NotRequired[int],
    'genres': NotRequired[list[ModelDramaboxGenre]],
    'id': NotRequired[str],
    'language': NotRequired[str],
    'listed_at': NotRequired[str],
    'rating': NotRequired[float],
    'status': NotRequired[str],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'views_display': NotRequired[str],
}, total=False)

ModelDramaboxGenre = TypedDict('ModelDramaboxGenre', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelDramaboxHomeResponseDoc = TypedDict('ModelDramaboxHomeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxHomeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxHomeResponse = TypedDict('ModelDramaboxHomeResponse', {
    'featured': NotRequired[list[ModelDramaboxBook]],
    'language': NotRequired[str],
    'shelves': NotRequired[list[ModelDramaboxShelf]],
}, total=False)

ModelDramaboxShelf = TypedDict('ModelDramaboxShelf', {
    'books': NotRequired[list[ModelDramaboxBook]],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'position': NotRequired[str],
}, total=False)

ModelDramaboxGenresResponseDoc = TypedDict('ModelDramaboxGenresResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxGenresResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxGenresResponse = TypedDict('ModelDramaboxGenresResponse', {
    'genres': NotRequired[list[ModelDramaboxGenre]],
    'language': NotRequired[str],
}, total=False)

ModelDramaboxDramaResponseDoc = TypedDict('ModelDramaboxDramaResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxDramaResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxDramaResponse = TypedDict('ModelDramaboxDramaResponse', {
    'available_languages': NotRequired[list[str]],
    'cover_url': NotRequired[str],
    'description': NotRequired[str],
    'episode_count': NotRequired[int],
    'episodes': NotRequired[list[ModelDramaboxEpisode]],
    'follows': NotRequired[int],
    'genres': NotRequired[list[ModelDramaboxGenre]],
    'id': NotRequired[str],
    'language': NotRequired[str],
    'listed_at': NotRequired[str],
    'related': NotRequired[list[ModelDramaboxBook]],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
    'views': NotRequired[int],
}, total=False)

ModelDramaboxEpisode = TypedDict('ModelDramaboxEpisode', {
    'duration_ms': NotRequired[int],
    'free': NotRequired[bool],
    'id': NotRequired[str],
    'number': NotRequired[int],
    'thumbnail_url': NotRequired[str],
    'updated_at': NotRequired[str],
}, total=False)

ModelDramaboxChannelsResponseDoc = TypedDict('ModelDramaboxChannelsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxChannelsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxChannelsResponse = TypedDict('ModelDramaboxChannelsResponse', {
    'channels': NotRequired[list[ModelDramaboxChannel]],
}, total=False)

ModelDramaboxCategoryBooksResponseDoc = TypedDict('ModelDramaboxCategoryBooksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxCategoryBooksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxCategoryBooksResponse = TypedDict('ModelDramaboxCategoryBooksResponse', {
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'titles': NotRequired[list[ModelDramaboxAppTitle]],
}, total=False)

ModelDramaboxCategoriesResponseDoc = TypedDict('ModelDramaboxCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxCategoriesResponse = TypedDict('ModelDramaboxCategoriesResponse', {
    'groups': NotRequired[list[ModelDramaboxCategoryGroup]],
}, total=False)

ModelDramaboxCategoryGroup = TypedDict('ModelDramaboxCategoryGroup', {
    'key': NotRequired[str],
    'options': NotRequired[list[ModelDramaboxCategoryOption]],
    'row': NotRequired[int],
    'type': NotRequired[int],
}, total=False)

ModelDramaboxCategoryOption = TypedDict('ModelDramaboxCategoryOption', {
    'name': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelDramaboxBrowseResponseDoc = TypedDict('ModelDramaboxBrowseResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDramaboxBrowseResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDramaboxBrowseResponse = TypedDict('ModelDramaboxBrowseResponse', {
    'books': NotRequired[list[ModelDramaboxBook]],
    'genre_id': NotRequired[int],
    'genre_name': NotRequired[str],
    'language': NotRequired[str],
    'page': NotRequired[int],
    'total_pages': NotRequired[int],
}, total=False)

DramaboxBrowseResponse = ModelDramaboxBrowseResponseDoc
DramaboxBrowseParams = TypedDict('DramaboxBrowseParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'genre_id': NotRequired[int],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxCategoriesResponse = ModelDramaboxCategoriesResponseDoc
DramaboxCategoriesParams = TypedDict('DramaboxCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

DramaboxCategoryBooksResponse = ModelDramaboxCategoryBooksResponseDoc
DramaboxCategoryBooksParams = TypedDict('DramaboxCategoryBooksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'language': NotRequired[str],
    'production': NotRequired[Literal['3', '1', '2']],
    'dub': NotRequired[Literal['1', '0']],
    'genre': NotRequired[str],
    'genre_2': NotRequired[str],
    'sort': NotRequired[Literal['1', '2', '3']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxChannelsResponse = ModelDramaboxChannelsResponseDoc
DramaboxChannelsParams = TypedDict('DramaboxChannelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

DramaboxDramaResponse = ModelDramaboxDramaResponseDoc
DramaboxDramaParams = TypedDict('DramaboxDramaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

DramaboxGenresResponse = ModelDramaboxGenresResponseDoc
DramaboxGenresParams = TypedDict('DramaboxGenresParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxHomeResponse = ModelDramaboxHomeResponseDoc
DramaboxHomeParams = TypedDict('DramaboxHomeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxMoreResponse = ModelDramaboxMoreResponseDoc
DramaboxMoreParams = TypedDict('DramaboxMoreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'position': Required[Literal['trending', 'must-sees', 'hidden-gems']],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxPerformerResponse = ModelDramaboxPerformerResponseDoc
DramaboxPerformerParams = TypedDict('DramaboxPerformerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'performer_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxRankResponse = ModelDramaboxRankResponseDoc
DramaboxRankParams = TypedDict('DramaboxRankParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'rank_type': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxRecommendResponse = ModelDramaboxRecommendResponseDoc
DramaboxRecommendParams = TypedDict('DramaboxRecommendParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
}, total=False)

DramaboxSearchResponse = ModelDramaboxSearchResponseDoc
DramaboxSearchParams = TypedDict('DramaboxSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'sort': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxSuggestResponse = ModelDramaboxSuggestResponseDoc
DramaboxSuggestParams = TypedDict('DramaboxSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

DramaboxTagResponse = ModelDramaboxTagResponseDoc
DramaboxTagParams = TypedDict('DramaboxTagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tag_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTheaterResponse = ModelDramaboxTheaterResponseDoc
DramaboxTheaterParams = TypedDict('DramaboxTheaterParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'channel': Required[Literal['popular', 'new', 'rankings', 'categories', 'anime', 'live-action', 'vip', 'original']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTrendingResponse = ModelDramaboxTrendingResponseDoc
DramaboxTrendingParams = TypedDict('DramaboxTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

class DramaboxGroup:
    @overload
    def browse(self, **params: Unpack[DramaboxBrowseStreamParams]) -> BinaryIO: ...
    @overload
    def browse(self, **params: Unpack[DramaboxBrowseTextResponseParams]) -> str: ...
    @overload
    def browse(self, **params: Unpack[DramaboxBrowseDefaultParams]) -> DramaboxBrowseResponse: ...
    @overload
    def categories(self, **params: Unpack[DramaboxCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[DramaboxCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[DramaboxCategoriesDefaultParams]) -> DramaboxCategoriesResponse: ...
    @overload
    def category_books(self, **params: Unpack[DramaboxCategoryBooksStreamParams]) -> BinaryIO: ...
    @overload
    def category_books(self, **params: Unpack[DramaboxCategoryBooksTextResponseParams]) -> str: ...
    @overload
    def category_books(self, **params: Unpack[DramaboxCategoryBooksDefaultParams]) -> DramaboxCategoryBooksResponse: ...
    @overload
    def channels(self, **params: Unpack[DramaboxChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def channels(self, **params: Unpack[DramaboxChannelsTextResponseParams]) -> str: ...
    @overload
    def channels(self, **params: Unpack[DramaboxChannelsDefaultParams]) -> DramaboxChannelsResponse: ...
    @overload
    def drama(self, **params: Unpack[DramaboxDramaStreamParams]) -> BinaryIO: ...
    @overload
    def drama(self, **params: Unpack[DramaboxDramaTextResponseParams]) -> str: ...
    @overload
    def drama(self, **params: Unpack[DramaboxDramaDefaultParams]) -> DramaboxDramaResponse: ...
    @overload
    def genres(self, **params: Unpack[DramaboxGenresStreamParams]) -> BinaryIO: ...
    @overload
    def genres(self, **params: Unpack[DramaboxGenresTextResponseParams]) -> str: ...
    @overload
    def genres(self, **params: Unpack[DramaboxGenresDefaultParams]) -> DramaboxGenresResponse: ...
    @overload
    def home(self, **params: Unpack[DramaboxHomeStreamParams]) -> BinaryIO: ...
    @overload
    def home(self, **params: Unpack[DramaboxHomeTextResponseParams]) -> str: ...
    @overload
    def home(self, **params: Unpack[DramaboxHomeDefaultParams]) -> DramaboxHomeResponse: ...
    @overload
    def more(self, **params: Unpack[DramaboxMoreStreamParams]) -> BinaryIO: ...
    @overload
    def more(self, **params: Unpack[DramaboxMoreTextResponseParams]) -> str: ...
    @overload
    def more(self, **params: Unpack[DramaboxMoreDefaultParams]) -> DramaboxMoreResponse: ...
    @overload
    def performer(self, **params: Unpack[DramaboxPerformerStreamParams]) -> BinaryIO: ...
    @overload
    def performer(self, **params: Unpack[DramaboxPerformerTextResponseParams]) -> str: ...
    @overload
    def performer(self, **params: Unpack[DramaboxPerformerDefaultParams]) -> DramaboxPerformerResponse: ...
    @overload
    def rank(self, **params: Unpack[DramaboxRankStreamParams]) -> BinaryIO: ...
    @overload
    def rank(self, **params: Unpack[DramaboxRankTextResponseParams]) -> str: ...
    @overload
    def rank(self, **params: Unpack[DramaboxRankDefaultParams]) -> DramaboxRankResponse: ...
    @overload
    def recommend(self, **params: Unpack[DramaboxRecommendStreamParams]) -> BinaryIO: ...
    @overload
    def recommend(self, **params: Unpack[DramaboxRecommendTextResponseParams]) -> str: ...
    @overload
    def recommend(self, **params: Unpack[DramaboxRecommendDefaultParams]) -> DramaboxRecommendResponse: ...
    @overload
    def search(self, **params: Unpack[DramaboxSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[DramaboxSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[DramaboxSearchDefaultParams]) -> DramaboxSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[DramaboxSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[DramaboxSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[DramaboxSuggestDefaultParams]) -> DramaboxSuggestResponse: ...
    @overload
    def tag(self, **params: Unpack[DramaboxTagStreamParams]) -> BinaryIO: ...
    @overload
    def tag(self, **params: Unpack[DramaboxTagTextResponseParams]) -> str: ...
    @overload
    def tag(self, **params: Unpack[DramaboxTagDefaultParams]) -> DramaboxTagResponse: ...
    @overload
    def theater(self, **params: Unpack[DramaboxTheaterStreamParams]) -> BinaryIO: ...
    @overload
    def theater(self, **params: Unpack[DramaboxTheaterTextResponseParams]) -> str: ...
    @overload
    def theater(self, **params: Unpack[DramaboxTheaterDefaultParams]) -> DramaboxTheaterResponse: ...
    @overload
    def trending(self, **params: Unpack[DramaboxTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def trending(self, **params: Unpack[DramaboxTrendingTextResponseParams]) -> str: ...
    @overload
    def trending(self, **params: Unpack[DramaboxTrendingDefaultParams]) -> DramaboxTrendingResponse: ...

OperationId = Literal[
    'dramabox-browse',
    'dramabox-categories',
    'dramabox-category-books',
    'dramabox-channels',
    'dramabox-drama',
    'dramabox-genres',
    'dramabox-home',
    'dramabox-more',
    'dramabox-performer',
    'dramabox-rank',
    'dramabox-recommend',
    'dramabox-search',
    'dramabox-suggest',
    'dramabox-tag',
    'dramabox-theater',
    'dramabox-trending',
]

class CrawloraClient:
    dramabox: DramaboxGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-browse'],
        params: DramaboxBrowseParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxBrowseResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-categories'],
        params: DramaboxCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-category-books'],
        params: DramaboxCategoryBooksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxCategoryBooksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-channels'],
        params: DramaboxChannelsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxChannelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-drama'],
        params: DramaboxDramaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxDramaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-genres'],
        params: DramaboxGenresParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxGenresResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-home'],
        params: DramaboxHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxHomeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-more'],
        params: DramaboxMoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxMoreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-performer'],
        params: DramaboxPerformerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxPerformerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-rank'],
        params: DramaboxRankParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxRankResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-recommend'],
        params: DramaboxRecommendParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxRecommendResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-search'],
        params: DramaboxSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-suggest'],
        params: DramaboxSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-tag'],
        params: DramaboxTagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxTagResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-theater'],
        params: DramaboxTheaterParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxTheaterResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['dramabox-trending'],
        params: DramaboxTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-browse'],
        params: DramaboxBrowseParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxBrowseResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-categories'],
        params: DramaboxCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-category-books'],
        params: DramaboxCategoryBooksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxCategoryBooksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-channels'],
        params: DramaboxChannelsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxChannelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-drama'],
        params: DramaboxDramaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxDramaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-genres'],
        params: DramaboxGenresParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxGenresResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-home'],
        params: DramaboxHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxHomeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-more'],
        params: DramaboxMoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxMoreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-performer'],
        params: DramaboxPerformerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxPerformerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-rank'],
        params: DramaboxRankParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxRankResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-recommend'],
        params: DramaboxRecommendParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxRecommendResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-search'],
        params: DramaboxSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-suggest'],
        params: DramaboxSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-tag'],
        params: DramaboxTagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxTagResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-theater'],
        params: DramaboxTheaterParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxTheaterResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['dramabox-trending'],
        params: DramaboxTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DramaboxTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class DramaBoxClient(CrawloraClient):
    def __enter__(self) -> DramaBoxClient: ...
    @overload
    def browse(self, **params: Unpack[DramaboxBrowseStreamParams]) -> BinaryIO: ...
    @overload
    def browse(self, **params: Unpack[DramaboxBrowseTextResponseParams]) -> str: ...
    @overload
    def browse(self, **params: Unpack[DramaboxBrowseDefaultParams]) -> DramaboxBrowseResponse: ...
    @overload
    def categories(self, **params: Unpack[DramaboxCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[DramaboxCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[DramaboxCategoriesDefaultParams]) -> DramaboxCategoriesResponse: ...
    @overload
    def category_books(self, **params: Unpack[DramaboxCategoryBooksStreamParams]) -> BinaryIO: ...
    @overload
    def category_books(self, **params: Unpack[DramaboxCategoryBooksTextResponseParams]) -> str: ...
    @overload
    def category_books(self, **params: Unpack[DramaboxCategoryBooksDefaultParams]) -> DramaboxCategoryBooksResponse: ...
    @overload
    def channels(self, **params: Unpack[DramaboxChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def channels(self, **params: Unpack[DramaboxChannelsTextResponseParams]) -> str: ...
    @overload
    def channels(self, **params: Unpack[DramaboxChannelsDefaultParams]) -> DramaboxChannelsResponse: ...
    @overload
    def drama(self, **params: Unpack[DramaboxDramaStreamParams]) -> BinaryIO: ...
    @overload
    def drama(self, **params: Unpack[DramaboxDramaTextResponseParams]) -> str: ...
    @overload
    def drama(self, **params: Unpack[DramaboxDramaDefaultParams]) -> DramaboxDramaResponse: ...
    @overload
    def genres(self, **params: Unpack[DramaboxGenresStreamParams]) -> BinaryIO: ...
    @overload
    def genres(self, **params: Unpack[DramaboxGenresTextResponseParams]) -> str: ...
    @overload
    def genres(self, **params: Unpack[DramaboxGenresDefaultParams]) -> DramaboxGenresResponse: ...
    @overload
    def home(self, **params: Unpack[DramaboxHomeStreamParams]) -> BinaryIO: ...
    @overload
    def home(self, **params: Unpack[DramaboxHomeTextResponseParams]) -> str: ...
    @overload
    def home(self, **params: Unpack[DramaboxHomeDefaultParams]) -> DramaboxHomeResponse: ...
    @overload
    def more(self, **params: Unpack[DramaboxMoreStreamParams]) -> BinaryIO: ...
    @overload
    def more(self, **params: Unpack[DramaboxMoreTextResponseParams]) -> str: ...
    @overload
    def more(self, **params: Unpack[DramaboxMoreDefaultParams]) -> DramaboxMoreResponse: ...
    @overload
    def performer(self, **params: Unpack[DramaboxPerformerStreamParams]) -> BinaryIO: ...
    @overload
    def performer(self, **params: Unpack[DramaboxPerformerTextResponseParams]) -> str: ...
    @overload
    def performer(self, **params: Unpack[DramaboxPerformerDefaultParams]) -> DramaboxPerformerResponse: ...
    @overload
    def rank(self, **params: Unpack[DramaboxRankStreamParams]) -> BinaryIO: ...
    @overload
    def rank(self, **params: Unpack[DramaboxRankTextResponseParams]) -> str: ...
    @overload
    def rank(self, **params: Unpack[DramaboxRankDefaultParams]) -> DramaboxRankResponse: ...
    @overload
    def recommend(self, **params: Unpack[DramaboxRecommendStreamParams]) -> BinaryIO: ...
    @overload
    def recommend(self, **params: Unpack[DramaboxRecommendTextResponseParams]) -> str: ...
    @overload
    def recommend(self, **params: Unpack[DramaboxRecommendDefaultParams]) -> DramaboxRecommendResponse: ...
    @overload
    def search(self, **params: Unpack[DramaboxSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[DramaboxSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[DramaboxSearchDefaultParams]) -> DramaboxSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[DramaboxSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[DramaboxSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[DramaboxSuggestDefaultParams]) -> DramaboxSuggestResponse: ...
    @overload
    def tag(self, **params: Unpack[DramaboxTagStreamParams]) -> BinaryIO: ...
    @overload
    def tag(self, **params: Unpack[DramaboxTagTextResponseParams]) -> str: ...
    @overload
    def tag(self, **params: Unpack[DramaboxTagDefaultParams]) -> DramaboxTagResponse: ...
    @overload
    def theater(self, **params: Unpack[DramaboxTheaterStreamParams]) -> BinaryIO: ...
    @overload
    def theater(self, **params: Unpack[DramaboxTheaterTextResponseParams]) -> str: ...
    @overload
    def theater(self, **params: Unpack[DramaboxTheaterDefaultParams]) -> DramaboxTheaterResponse: ...
    @overload
    def trending(self, **params: Unpack[DramaboxTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def trending(self, **params: Unpack[DramaboxTrendingTextResponseParams]) -> str: ...
    @overload
    def trending(self, **params: Unpack[DramaboxTrendingDefaultParams]) -> DramaboxTrendingResponse: ...

class AsyncDramaBoxClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncDramaBoxClient: ...
    dramabox: _AsyncDramaboxGroup
    @overload
    async def browse(self, **params: Unpack[DramaboxBrowseStreamParams]) -> BinaryIO: ...
    @overload
    async def browse(self, **params: Unpack[DramaboxBrowseTextResponseParams]) -> str: ...
    @overload
    async def browse(self, **params: Unpack[DramaboxBrowseDefaultParams]) -> DramaboxBrowseResponse: ...
    @overload
    async def categories(self, **params: Unpack[DramaboxCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[DramaboxCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[DramaboxCategoriesDefaultParams]) -> DramaboxCategoriesResponse: ...
    @overload
    async def category_books(self, **params: Unpack[DramaboxCategoryBooksStreamParams]) -> BinaryIO: ...
    @overload
    async def category_books(self, **params: Unpack[DramaboxCategoryBooksTextResponseParams]) -> str: ...
    @overload
    async def category_books(self, **params: Unpack[DramaboxCategoryBooksDefaultParams]) -> DramaboxCategoryBooksResponse: ...
    @overload
    async def channels(self, **params: Unpack[DramaboxChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def channels(self, **params: Unpack[DramaboxChannelsTextResponseParams]) -> str: ...
    @overload
    async def channels(self, **params: Unpack[DramaboxChannelsDefaultParams]) -> DramaboxChannelsResponse: ...
    @overload
    async def drama(self, **params: Unpack[DramaboxDramaStreamParams]) -> BinaryIO: ...
    @overload
    async def drama(self, **params: Unpack[DramaboxDramaTextResponseParams]) -> str: ...
    @overload
    async def drama(self, **params: Unpack[DramaboxDramaDefaultParams]) -> DramaboxDramaResponse: ...
    @overload
    async def genres(self, **params: Unpack[DramaboxGenresStreamParams]) -> BinaryIO: ...
    @overload
    async def genres(self, **params: Unpack[DramaboxGenresTextResponseParams]) -> str: ...
    @overload
    async def genres(self, **params: Unpack[DramaboxGenresDefaultParams]) -> DramaboxGenresResponse: ...
    @overload
    async def home(self, **params: Unpack[DramaboxHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def home(self, **params: Unpack[DramaboxHomeTextResponseParams]) -> str: ...
    @overload
    async def home(self, **params: Unpack[DramaboxHomeDefaultParams]) -> DramaboxHomeResponse: ...
    @overload
    async def more(self, **params: Unpack[DramaboxMoreStreamParams]) -> BinaryIO: ...
    @overload
    async def more(self, **params: Unpack[DramaboxMoreTextResponseParams]) -> str: ...
    @overload
    async def more(self, **params: Unpack[DramaboxMoreDefaultParams]) -> DramaboxMoreResponse: ...
    @overload
    async def performer(self, **params: Unpack[DramaboxPerformerStreamParams]) -> BinaryIO: ...
    @overload
    async def performer(self, **params: Unpack[DramaboxPerformerTextResponseParams]) -> str: ...
    @overload
    async def performer(self, **params: Unpack[DramaboxPerformerDefaultParams]) -> DramaboxPerformerResponse: ...
    @overload
    async def rank(self, **params: Unpack[DramaboxRankStreamParams]) -> BinaryIO: ...
    @overload
    async def rank(self, **params: Unpack[DramaboxRankTextResponseParams]) -> str: ...
    @overload
    async def rank(self, **params: Unpack[DramaboxRankDefaultParams]) -> DramaboxRankResponse: ...
    @overload
    async def recommend(self, **params: Unpack[DramaboxRecommendStreamParams]) -> BinaryIO: ...
    @overload
    async def recommend(self, **params: Unpack[DramaboxRecommendTextResponseParams]) -> str: ...
    @overload
    async def recommend(self, **params: Unpack[DramaboxRecommendDefaultParams]) -> DramaboxRecommendResponse: ...
    @overload
    async def search(self, **params: Unpack[DramaboxSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[DramaboxSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[DramaboxSearchDefaultParams]) -> DramaboxSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[DramaboxSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[DramaboxSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[DramaboxSuggestDefaultParams]) -> DramaboxSuggestResponse: ...
    @overload
    async def tag(self, **params: Unpack[DramaboxTagStreamParams]) -> BinaryIO: ...
    @overload
    async def tag(self, **params: Unpack[DramaboxTagTextResponseParams]) -> str: ...
    @overload
    async def tag(self, **params: Unpack[DramaboxTagDefaultParams]) -> DramaboxTagResponse: ...
    @overload
    async def theater(self, **params: Unpack[DramaboxTheaterStreamParams]) -> BinaryIO: ...
    @overload
    async def theater(self, **params: Unpack[DramaboxTheaterTextResponseParams]) -> str: ...
    @overload
    async def theater(self, **params: Unpack[DramaboxTheaterDefaultParams]) -> DramaboxTheaterResponse: ...
    @overload
    async def trending(self, **params: Unpack[DramaboxTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def trending(self, **params: Unpack[DramaboxTrendingTextResponseParams]) -> str: ...
    @overload
    async def trending(self, **params: Unpack[DramaboxTrendingDefaultParams]) -> DramaboxTrendingResponse: ...

class _AsyncDramaboxGroup:
    @overload
    async def browse(self, **params: Unpack[DramaboxBrowseStreamParams]) -> BinaryIO: ...
    @overload
    async def browse(self, **params: Unpack[DramaboxBrowseTextResponseParams]) -> str: ...
    @overload
    async def browse(self, **params: Unpack[DramaboxBrowseDefaultParams]) -> DramaboxBrowseResponse: ...
    @overload
    async def categories(self, **params: Unpack[DramaboxCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[DramaboxCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[DramaboxCategoriesDefaultParams]) -> DramaboxCategoriesResponse: ...
    @overload
    async def category_books(self, **params: Unpack[DramaboxCategoryBooksStreamParams]) -> BinaryIO: ...
    @overload
    async def category_books(self, **params: Unpack[DramaboxCategoryBooksTextResponseParams]) -> str: ...
    @overload
    async def category_books(self, **params: Unpack[DramaboxCategoryBooksDefaultParams]) -> DramaboxCategoryBooksResponse: ...
    @overload
    async def channels(self, **params: Unpack[DramaboxChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def channels(self, **params: Unpack[DramaboxChannelsTextResponseParams]) -> str: ...
    @overload
    async def channels(self, **params: Unpack[DramaboxChannelsDefaultParams]) -> DramaboxChannelsResponse: ...
    @overload
    async def drama(self, **params: Unpack[DramaboxDramaStreamParams]) -> BinaryIO: ...
    @overload
    async def drama(self, **params: Unpack[DramaboxDramaTextResponseParams]) -> str: ...
    @overload
    async def drama(self, **params: Unpack[DramaboxDramaDefaultParams]) -> DramaboxDramaResponse: ...
    @overload
    async def genres(self, **params: Unpack[DramaboxGenresStreamParams]) -> BinaryIO: ...
    @overload
    async def genres(self, **params: Unpack[DramaboxGenresTextResponseParams]) -> str: ...
    @overload
    async def genres(self, **params: Unpack[DramaboxGenresDefaultParams]) -> DramaboxGenresResponse: ...
    @overload
    async def home(self, **params: Unpack[DramaboxHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def home(self, **params: Unpack[DramaboxHomeTextResponseParams]) -> str: ...
    @overload
    async def home(self, **params: Unpack[DramaboxHomeDefaultParams]) -> DramaboxHomeResponse: ...
    @overload
    async def more(self, **params: Unpack[DramaboxMoreStreamParams]) -> BinaryIO: ...
    @overload
    async def more(self, **params: Unpack[DramaboxMoreTextResponseParams]) -> str: ...
    @overload
    async def more(self, **params: Unpack[DramaboxMoreDefaultParams]) -> DramaboxMoreResponse: ...
    @overload
    async def performer(self, **params: Unpack[DramaboxPerformerStreamParams]) -> BinaryIO: ...
    @overload
    async def performer(self, **params: Unpack[DramaboxPerformerTextResponseParams]) -> str: ...
    @overload
    async def performer(self, **params: Unpack[DramaboxPerformerDefaultParams]) -> DramaboxPerformerResponse: ...
    @overload
    async def rank(self, **params: Unpack[DramaboxRankStreamParams]) -> BinaryIO: ...
    @overload
    async def rank(self, **params: Unpack[DramaboxRankTextResponseParams]) -> str: ...
    @overload
    async def rank(self, **params: Unpack[DramaboxRankDefaultParams]) -> DramaboxRankResponse: ...
    @overload
    async def recommend(self, **params: Unpack[DramaboxRecommendStreamParams]) -> BinaryIO: ...
    @overload
    async def recommend(self, **params: Unpack[DramaboxRecommendTextResponseParams]) -> str: ...
    @overload
    async def recommend(self, **params: Unpack[DramaboxRecommendDefaultParams]) -> DramaboxRecommendResponse: ...
    @overload
    async def search(self, **params: Unpack[DramaboxSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[DramaboxSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[DramaboxSearchDefaultParams]) -> DramaboxSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[DramaboxSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[DramaboxSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[DramaboxSuggestDefaultParams]) -> DramaboxSuggestResponse: ...
    @overload
    async def tag(self, **params: Unpack[DramaboxTagStreamParams]) -> BinaryIO: ...
    @overload
    async def tag(self, **params: Unpack[DramaboxTagTextResponseParams]) -> str: ...
    @overload
    async def tag(self, **params: Unpack[DramaboxTagDefaultParams]) -> DramaboxTagResponse: ...
    @overload
    async def theater(self, **params: Unpack[DramaboxTheaterStreamParams]) -> BinaryIO: ...
    @overload
    async def theater(self, **params: Unpack[DramaboxTheaterTextResponseParams]) -> str: ...
    @overload
    async def theater(self, **params: Unpack[DramaboxTheaterDefaultParams]) -> DramaboxTheaterResponse: ...
    @overload
    async def trending(self, **params: Unpack[DramaboxTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def trending(self, **params: Unpack[DramaboxTrendingTextResponseParams]) -> str: ...
    @overload
    async def trending(self, **params: Unpack[DramaboxTrendingDefaultParams]) -> DramaboxTrendingResponse: ...

DramaboxBrowseDefaultParams = TypedDict('DramaboxBrowseDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'genre_id': NotRequired[int],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxBrowseTextResponseParams = TypedDict('DramaboxBrowseTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'genre_id': NotRequired[int],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxBrowseStreamParams = TypedDict('DramaboxBrowseStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'genre_id': NotRequired[int],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxCategoriesDefaultParams = TypedDict('DramaboxCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

DramaboxCategoriesTextResponseParams = TypedDict('DramaboxCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

DramaboxCategoriesStreamParams = TypedDict('DramaboxCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

DramaboxCategoryBooksDefaultParams = TypedDict('DramaboxCategoryBooksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'language': NotRequired[str],
    'production': NotRequired[Literal['3', '1', '2']],
    'dub': NotRequired[Literal['1', '0']],
    'genre': NotRequired[str],
    'genre_2': NotRequired[str],
    'sort': NotRequired[Literal['1', '2', '3']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxCategoryBooksTextResponseParams = TypedDict('DramaboxCategoryBooksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'language': NotRequired[str],
    'production': NotRequired[Literal['3', '1', '2']],
    'dub': NotRequired[Literal['1', '0']],
    'genre': NotRequired[str],
    'genre_2': NotRequired[str],
    'sort': NotRequired[Literal['1', '2', '3']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxCategoryBooksStreamParams = TypedDict('DramaboxCategoryBooksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'language': NotRequired[str],
    'production': NotRequired[Literal['3', '1', '2']],
    'dub': NotRequired[Literal['1', '0']],
    'genre': NotRequired[str],
    'genre_2': NotRequired[str],
    'sort': NotRequired[Literal['1', '2', '3']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxChannelsDefaultParams = TypedDict('DramaboxChannelsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

DramaboxChannelsTextResponseParams = TypedDict('DramaboxChannelsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

DramaboxChannelsStreamParams = TypedDict('DramaboxChannelsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

DramaboxDramaDefaultParams = TypedDict('DramaboxDramaDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

DramaboxDramaTextResponseParams = TypedDict('DramaboxDramaTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

DramaboxDramaStreamParams = TypedDict('DramaboxDramaStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

DramaboxGenresDefaultParams = TypedDict('DramaboxGenresDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxGenresTextResponseParams = TypedDict('DramaboxGenresTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxGenresStreamParams = TypedDict('DramaboxGenresStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxHomeDefaultParams = TypedDict('DramaboxHomeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxHomeTextResponseParams = TypedDict('DramaboxHomeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxHomeStreamParams = TypedDict('DramaboxHomeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxMoreDefaultParams = TypedDict('DramaboxMoreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'position': Required[Literal['trending', 'must-sees', 'hidden-gems']],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxMoreTextResponseParams = TypedDict('DramaboxMoreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'position': Required[Literal['trending', 'must-sees', 'hidden-gems']],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxMoreStreamParams = TypedDict('DramaboxMoreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'position': Required[Literal['trending', 'must-sees', 'hidden-gems']],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'ko', 'zhHans', 'zh', 'es', 'ja', 'de', 'in', 'th', 'tl', 'pt', 'fr', 'ar', 'it']],
}, total=False)

DramaboxPerformerDefaultParams = TypedDict('DramaboxPerformerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'performer_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxPerformerTextResponseParams = TypedDict('DramaboxPerformerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'performer_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxPerformerStreamParams = TypedDict('DramaboxPerformerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'performer_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxRankDefaultParams = TypedDict('DramaboxRankDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'rank_type': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxRankTextResponseParams = TypedDict('DramaboxRankTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'rank_type': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxRankStreamParams = TypedDict('DramaboxRankStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'rank_type': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxRecommendDefaultParams = TypedDict('DramaboxRecommendDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'page': NotRequired[int],
}, total=False)

DramaboxRecommendTextResponseParams = TypedDict('DramaboxRecommendTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'page': NotRequired[int],
}, total=False)

DramaboxRecommendStreamParams = TypedDict('DramaboxRecommendStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'page': NotRequired[int],
}, total=False)

DramaboxSearchDefaultParams = TypedDict('DramaboxSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'sort': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxSearchTextResponseParams = TypedDict('DramaboxSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'sort': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxSearchStreamParams = TypedDict('DramaboxSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'sort': NotRequired[Literal['1', '2', '3']],
}, total=False)

DramaboxSuggestDefaultParams = TypedDict('DramaboxSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
}, total=False)

DramaboxSuggestTextResponseParams = TypedDict('DramaboxSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
}, total=False)

DramaboxSuggestStreamParams = TypedDict('DramaboxSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
}, total=False)

DramaboxTagDefaultParams = TypedDict('DramaboxTagDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tag_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTagTextResponseParams = TypedDict('DramaboxTagTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tag_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTagStreamParams = TypedDict('DramaboxTagStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tag_id': Required[int],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTheaterDefaultParams = TypedDict('DramaboxTheaterDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'channel': Required[Literal['popular', 'new', 'rankings', 'categories', 'anime', 'live-action', 'vip', 'original']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTheaterTextResponseParams = TypedDict('DramaboxTheaterTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'channel': Required[Literal['popular', 'new', 'rankings', 'categories', 'anime', 'live-action', 'vip', 'original']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTheaterStreamParams = TypedDict('DramaboxTheaterStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'channel': Required[Literal['popular', 'new', 'rankings', 'categories', 'anime', 'live-action', 'vip', 'original']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

DramaboxTrendingDefaultParams = TypedDict('DramaboxTrendingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

DramaboxTrendingTextResponseParams = TypedDict('DramaboxTrendingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

DramaboxTrendingStreamParams = TypedDict('DramaboxTrendingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)
