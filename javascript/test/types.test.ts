import { DramaBoxClient } from "../src/index.js";

const client = new DramaBoxClient({ apiKey: "test-key" });
void client.drama({"id": "sample"});
void client.request("dramabox-drama", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("dramabox-drama", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("dramabox-drama", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.drama({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("dramabox-drama", {"id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("dramabox-drama", {"id": "sample"}, { responseType: "text" });
void rawText;


void client.browse();
void client.request("dramabox-browse");
// @ts-expect-error The selected operation requires its documented params.
void client.drama();
