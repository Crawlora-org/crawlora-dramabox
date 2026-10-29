<?php
declare(strict_types=1);

require_once __DIR__ . '/../src/Crawlora/Dramabox/Client.php';

$calls = [];
$transport = function ($url, $headers, $timeout) use (&$calls) {
    $calls[] = [$url, $headers, $timeout];
    return ['status' => 200, 'content_type' => 'application/json', 'body' => '{"ok":true}'];
};
$client = new Crawlora\Dramabox\Client(
    apiKey: 'test-key',
    baseUrl: 'https://api.example.test/api/v1',
    transport: $transport,
);
$result = $client->request("dramabox-search", ['keyword' => 'sample']);
if ($result !== ['ok' => true]) {
    throw new RuntimeException('Expected the mocked JSON response.');
}
if (count($calls) !== 1 || !str_contains($calls[0][0], '/dramabox/')) {
    throw new RuntimeException('The generated operation did not use the platform API path.');
}
if (!in_array('x-api-key: test-key', $calls[0][1], true)) {
    throw new RuntimeException('The API key header was not sent.');
}
if ($client->operationCount() !== 16) {
    throw new RuntimeException('The operation count did not match the generated contract.');
}
$defaultClient = new Crawlora\Dramabox\Client(
    apiKey: 'test-key',
    transport: function ($url) {
        if (!str_starts_with($url, 'https://api.crawlora.net/api/v1/dramabox/')) {
            throw new RuntimeException('The default API base URL did not include /api/v1.');
        }
        return ['status' => 200, 'content_type' => 'application/json', 'body' => '{"ok":true}'];
    },
);
$defaultClient->request("dramabox-search", ['keyword' => 'sample']);
try {
    $client->request('unlisted-operation');
    throw new RuntimeException('An unlisted operation was accepted.');
} catch (Crawlora\Dramabox\ClientException $error) {
    if (!str_contains($error->getMessage(), 'Unknown')) {
        throw $error;
    }
}
$client->close();
echo "PHP platform client tests passed\n";
