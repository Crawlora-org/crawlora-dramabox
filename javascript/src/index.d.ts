import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class DramaBoxClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  browse(params?: OperationParamsMap["dramabox-browse"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params?: OperationParamsMap["dramabox-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categoryBooks(params?: OperationParamsMap["dramabox-category-books"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  channels(params?: OperationParamsMap["dramabox-channels"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  drama(params: OperationParamsMap["dramabox-drama"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  genres(params?: OperationParamsMap["dramabox-genres"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  home(params?: OperationParamsMap["dramabox-home"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  more(params: OperationParamsMap["dramabox-more"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  performer(params: OperationParamsMap["dramabox-performer"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rank(params?: OperationParamsMap["dramabox-rank"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  recommend(params?: OperationParamsMap["dramabox-recommend"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["dramabox-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  suggest(params: OperationParamsMap["dramabox-suggest"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tag(params: OperationParamsMap["dramabox-tag"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  theater(params: OperationParamsMap["dramabox-theater"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trending(params?: OperationParamsMap["dramabox-trending"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  browse(params?: OperationParamsMap["dramabox-browse"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params?: OperationParamsMap["dramabox-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categoryBooks(params?: OperationParamsMap["dramabox-category-books"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  channels(params?: OperationParamsMap["dramabox-channels"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  drama(params: OperationParamsMap["dramabox-drama"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  genres(params?: OperationParamsMap["dramabox-genres"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  home(params?: OperationParamsMap["dramabox-home"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  more(params: OperationParamsMap["dramabox-more"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  performer(params: OperationParamsMap["dramabox-performer"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rank(params?: OperationParamsMap["dramabox-rank"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  recommend(params?: OperationParamsMap["dramabox-recommend"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["dramabox-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  suggest(params: OperationParamsMap["dramabox-suggest"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tag(params: OperationParamsMap["dramabox-tag"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  theater(params: OperationParamsMap["dramabox-theater"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trending(params?: OperationParamsMap["dramabox-trending"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  browse(...args: OperationRequestArgs<"dramabox-browse">): Promise<OperationResponseMap["dramabox-browse"]>;
  categories(...args: OperationRequestArgs<"dramabox-categories">): Promise<OperationResponseMap["dramabox-categories"]>;
  categoryBooks(...args: OperationRequestArgs<"dramabox-category-books">): Promise<OperationResponseMap["dramabox-category-books"]>;
  channels(...args: OperationRequestArgs<"dramabox-channels">): Promise<OperationResponseMap["dramabox-channels"]>;
  drama(...args: OperationRequestArgs<"dramabox-drama">): Promise<OperationResponseMap["dramabox-drama"]>;
  genres(...args: OperationRequestArgs<"dramabox-genres">): Promise<OperationResponseMap["dramabox-genres"]>;
  home(...args: OperationRequestArgs<"dramabox-home">): Promise<OperationResponseMap["dramabox-home"]>;
  more(...args: OperationRequestArgs<"dramabox-more">): Promise<OperationResponseMap["dramabox-more"]>;
  performer(...args: OperationRequestArgs<"dramabox-performer">): Promise<OperationResponseMap["dramabox-performer"]>;
  rank(...args: OperationRequestArgs<"dramabox-rank">): Promise<OperationResponseMap["dramabox-rank"]>;
  recommend(...args: OperationRequestArgs<"dramabox-recommend">): Promise<OperationResponseMap["dramabox-recommend"]>;
  search(...args: OperationRequestArgs<"dramabox-search">): Promise<OperationResponseMap["dramabox-search"]>;
  suggest(...args: OperationRequestArgs<"dramabox-suggest">): Promise<OperationResponseMap["dramabox-suggest"]>;
  tag(...args: OperationRequestArgs<"dramabox-tag">): Promise<OperationResponseMap["dramabox-tag"]>;
  theater(...args: OperationRequestArgs<"dramabox-theater">): Promise<OperationResponseMap["dramabox-theater"]>;
  trending(...args: OperationRequestArgs<"dramabox-trending">): Promise<OperationResponseMap["dramabox-trending"]>;
}
export { DramaBoxClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default DramaBoxClient;
