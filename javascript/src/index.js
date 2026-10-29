import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class DramaBoxClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-dramabox-js/0.1.0" });
    this["browse"] = (...args) => this.request("dramabox-browse", ...args);
    this["categories"] = (...args) => this.request("dramabox-categories", ...args);
    this["categoryBooks"] = (...args) => this.request("dramabox-category-books", ...args);
    this["channels"] = (...args) => this.request("dramabox-channels", ...args);
    this["drama"] = (...args) => this.request("dramabox-drama", ...args);
    this["genres"] = (...args) => this.request("dramabox-genres", ...args);
    this["home"] = (...args) => this.request("dramabox-home", ...args);
    this["more"] = (...args) => this.request("dramabox-more", ...args);
    this["performer"] = (...args) => this.request("dramabox-performer", ...args);
    this["rank"] = (...args) => this.request("dramabox-rank", ...args);
    this["recommend"] = (...args) => this.request("dramabox-recommend", ...args);
    this["search"] = (...args) => this.request("dramabox-search", ...args);
    this["suggest"] = (...args) => this.request("dramabox-suggest", ...args);
    this["tag"] = (...args) => this.request("dramabox-tag", ...args);
    this["theater"] = (...args) => this.request("dramabox-theater", ...args);
    this["trending"] = (...args) => this.request("dramabox-trending", ...args);
  }
}

export { DramaBoxClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default DramaBoxClient;
