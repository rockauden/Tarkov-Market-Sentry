import requests

def fetch_live_market_data():
    """Establishes a GraphQL connection to the Tarkov.dev API"""
    url = "https://api.tarkov.dev/graphql"
    query = """
    {
      items(lang: en) {
        id
        name
        shortName
        basePrice
        avg24hPrice
      }
    }
    """
    response = requests.post(url, json={"query": query})

    if response.status_code == 200:
        return response.json()
    else:
        print(f"[-] API Connection Failed: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    print(f"[+] Testing API Client Module...")
    data = fetch_live_market_data()
    if data and 'data' in data:
        print(f"[+] Connection Successful. Payload received.")