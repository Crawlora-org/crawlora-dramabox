use crawlora_dramabox::{Client, DramaboxHomeParams, ModelDramaboxHomeResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .dramabox
        .home(DramaboxHomeParams {
            ..Default::default()
        })
        .await?;
    let data: ModelDramaboxHomeResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
