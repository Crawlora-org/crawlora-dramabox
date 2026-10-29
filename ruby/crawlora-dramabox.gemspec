require_relative "lib/crawlora/dramabox/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-dramabox"
  spec.version = Crawlora::Dramabox::VERSION
  spec.summary = "DramaBox API client for Crawlora (16 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted DramaBox API. Covers title discovery, categories, search, rankings, recommendations, and public title details across 16 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=dramabox-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-dramabox", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-dramabox/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
