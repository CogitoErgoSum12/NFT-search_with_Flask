import requests




nft = "3HcD2Zz7cpZShUbS4KTEAXfLu31Yb9zb8wcJmNB6cQsh"

url = f"https://solana-gateway.moralis.io/nft/mainnet/{nft}/metadata"



headers = {

    "accept": "application/json",

    "X-API-Key": "S77RJTmiMoBbTQTEed5MExSDfHQ2HolnDEXy7GZRoo3Eah6t1YAR20dfdGIJASaT"

}



response = requests.get(url, headers=headers)



print(response.json())