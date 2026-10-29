import { DramaBoxClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new DramaBoxClient({ apiKey });

  const home = await client.home({  });
  console.log("home", home);
  const search = await client.search({ keyword: "romance" });
  console.log("search", search);
