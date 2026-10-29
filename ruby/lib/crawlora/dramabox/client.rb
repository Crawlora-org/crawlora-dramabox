require "json"
require "net/http"
require "uri"

module Crawlora
  module Dramabox
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"dramabox-browse": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-browse", "method": "GET", "params": [{"description": "Genre id from dramabox-genres; 0 or omitted browses all titles", "in": "query", "name": "genre_id", "type": "integer", "x-example": 161}, {"description": "Page number, 1 to 1000; defaults to 1. Each page holds 12 titles", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/browse", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "genre_id", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-categories": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-categories", "method": "GET", "params": [], "path": "/dramabox/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "dramabox-category-books": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-category-books", "method": "GET", "params": [{"description": "Language/origin value from dramabox-categories' language group, e.g. 美国 (Local) or 中国 (Chinese)", "in": "query", "name": "language", "type": "string", "x-example": "美国"}, {"description": "Production-type value from dramabox-categories' production group: 3 (AI Drama), 1 (Live-Action), 2 (Anime)", "enum": ["3", "1", "2"], "in": "query", "name": "production", "type": "string", "x-example": "1"}, {"description": "Dub-mode value from dramabox-categories' dub group: 1 (Dubbed), 0 (Subtitles Only)", "enum": ["1", "0"], "in": "query", "name": "dub", "type": "string", "x-example": "1"}, {"description": "Genre value from dramabox-categories' genre_1 group, e.g. 1357 (Romance) or 1361 (Strong Heroine)", "in": "query", "name": "genre", "type": "string", "x-example": "1357"}, {"description": "Genre value from dramabox-categories' genre_2 group, e.g. 1392 (Second Chance) or 1359 (BL); multi-tag values such as 1324,1362 are one value", "in": "query", "name": "genre_2", "type": "string", "x-example": "1392"}, {"description": "Sort value from dramabox-categories' sort group: 1 (Trending), 2 (Latest), 3 (Unwatched)", "enum": ["1", "2", "3"], "in": "query", "name": "sort", "type": "string", "x-example": "1"}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Titles per page, 1 to 50; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/dramabox/category-books", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "language", "type": "string"}, {"enum": ["3", "1", "2"], "in": "query", "name": "production", "type": "string"}, {"enum": ["1", "0"], "in": "query", "name": "dub", "type": "string"}, {"in": "query", "name": "genre", "type": "string"}, {"in": "query", "name": "genre_2", "type": "string"}, {"enum": ["1", "2", "3"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-channels": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-channels", "method": "GET", "params": [], "path": "/dramabox/channels", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "dramabox-drama": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-drama", "method": "GET", "params": [{"description": "Title id (digits) from any DramaBox list, or a dramabox.com drama URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "42000028173"}], "path": "/dramabox/drama", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-genres": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-genres", "method": "GET", "params": [{"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/genres", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-home": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-home", "method": "GET", "params": [{"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-more": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-more", "method": "GET", "params": [{"description": "Curated shelf: trending, must-sees or hidden-gems", "enum": ["trending", "must-sees", "hidden-gems"], "in": "query", "name": "position", "required": true, "type": "string", "x-example": "trending"}, {"description": "Page number, 1 to 1000; defaults to 1. Each page holds 18 titles", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Site locale, one of: en, ko, zhHans, zh, es, ja, de, in, th, tl, pt, fr, ar, it (in is Indonesian); defaults to en. Each locale has its own title library", "enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string", "x-example": "ja"}], "path": "/dramabox/more", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["trending", "must-sees", "hidden-gems"], "in": "query", "name": "position", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "ko", "zhHans", "zh", "es", "ja", "de", "in", "th", "tl", "pt", "fr", "ar", "it"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-performer": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-performer", "method": "GET", "params": [{"description": "Performer id from dramabox-search or dramabox-suggest's people results", "in": "query", "name": "performer_id", "required": true, "type": "integer", "x-example": 29450}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 20; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/dramabox/performer", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "performer_id", "required": true, "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-rank": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-rank", "method": "GET", "params": [{"description": "Ranking tab: 1 (Most Trending), 2 (Top Searched), 3 (New Releases); omit for the default tab", "enum": [1, 2, 3], "in": "query", "name": "rank_type", "type": "integer", "x-example": 2}], "path": "/dramabox/rank", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["1", "2", "3"], "in": "query", "name": "rank_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-recommend": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-recommend", "method": "GET", "params": [{"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}], "path": "/dramabox/recommend", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-search": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-search", "method": "GET", "params": [{"description": "Search text, trimmed and truncated to 80 characters", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "love"}, {"default": 1, "description": "One-based result page", "in": "query", "maximum": 1000, "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Results per page", "in": "query", "maximum": 50, "minimum": 1, "name": "limit", "type": "integer"}, {"description": "Upstream result ordering mode; omit for the app default", "enum": [1, 2, 3], "in": "query", "name": "sort", "type": "integer", "x-example": 1}], "path": "/dramabox/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"enum": ["1", "2", "3"], "in": "query", "name": "sort", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-suggest": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-suggest", "method": "GET", "params": [{"description": "Partial search text, trimmed and truncated to 80 characters", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lov"}], "path": "/dramabox/suggest", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "dramabox-tag": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-tag", "method": "GET", "params": [{"description": "Tag id from any title result's tag_refs", "in": "query", "name": "tag_id", "required": true, "type": "integer", "x-example": 1379}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 50; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/dramabox/tag", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tag_id", "required": true, "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-theater": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-theater", "method": "GET", "params": [{"description": "Theater channel: popular, new, rankings, categories, anime, live-action, vip or original", "enum": ["popular", "new", "rankings", "categories", "anime", "live-action", "vip", "original"], "in": "query", "name": "channel", "required": true, "type": "string", "x-example": "popular"}, {"description": "Page number, 1 to 1000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Titles per paged block, 1 to 20; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/dramabox/theater", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["popular", "new", "rankings", "categories", "anime", "live-action", "vip", "original"], "in": "query", "name": "channel", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "dramabox-trending": {"bodyParam": null, "bodyRequired": false, "id": "dramabox-trending", "method": "GET", "params": [], "path": "/dramabox/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["dramabox-browse", "dramabox-categories", "dramabox-category-books", "dramabox-channels", "dramabox-drama", "dramabox-genres", "dramabox-home", "dramabox-more", "dramabox-performer", "dramabox-rank", "dramabox-recommend", "dramabox-search", "dramabox-suggest", "dramabox-tag", "dramabox-theater", "dramabox-trending"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-dramabox-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('browse') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-browse', params, response_type: response_type)
      end
      define_method('categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-categories', params, response_type: response_type)
      end
      define_method('category_books') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-category-books', params, response_type: response_type)
      end
      define_method('channels') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-channels', params, response_type: response_type)
      end
      define_method('drama') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-drama', params, response_type: response_type)
      end
      define_method('genres') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-genres', params, response_type: response_type)
      end
      define_method('home') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-home', params, response_type: response_type)
      end
      define_method('more') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-more', params, response_type: response_type)
      end
      define_method('performer') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-performer', params, response_type: response_type)
      end
      define_method('rank') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-rank', params, response_type: response_type)
      end
      define_method('recommend') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-recommend', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-search', params, response_type: response_type)
      end
      define_method('suggest') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-suggest', params, response_type: response_type)
      end
      define_method('tag') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-tag', params, response_type: response_type)
      end
      define_method('theater') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-theater', params, response_type: response_type)
      end
      define_method('trending') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('dramabox-trending', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
