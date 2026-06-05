import requests
import pandas as pd
import time
import os

print("--- 🟢 Tarkov Market Sentry: AUTONOMOUS ENGINE ONLINE ---")

# 1. PIPELINE CONFIGURATION
url = "https://api.tarkov.dev/graphql"
# We path this to save directly into your new data folder
output_file = "../data/live_market_ledger.csv" 
interval_seconds = 60 # Polling every 60 seconds is polite to live production servers

graphql_query = """
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
payload = {"query": graphql_query}

print(f"[!] Sentry deployed. Monitoring live Tarkov API.")
print(f"[!] Logging to '{output_file}' every {interval_seconds} seconds.")
print("[!] Press 'Ctrl + C' to disengage.\n")

cycle_count = 1

# 2. THE CONTINUOUS LOOP
while True:
    try:
        print(f"[Cycle {cycle_count}] Fetching live market data...")
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            raw_json = response.json()
            
            if 'errors' in raw_json:
                print(f"[-] Gateway Error: {raw_json['errors'][0]['message']}")
            else:
                # Extract the nested data
                extracted_items = raw_json['data']['items']
                df = pd.DataFrame(extracted_items)
                
                # 3. TRANSFORM: Clean the data safely
                # Drop any items that don't have an average price yet
                df = df.dropna(subset=['avg24hPrice'])
                
                # Add the exact time of extraction
                df.insert(0, 'Timestamp', time.strftime("%Y-%m-%d %H:%M:%S"))
                
                # 4. LOAD: Append to the historical ledger safely
                # Create the data folder if it doesn't exist yet
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
                file_exists = os.path.exists(output_file)
                df.to_csv(output_file, mode='a', index=False, header=not file_exists)
                
                print(f"[+] Cycle {cycle_count} Success. {len(df)} live items secured and appended.")
                
        else:
            print(f"[-] Cycle {cycle_count} failed. Server Code: {response.status_code}")
            
        cycle_count += 1
        time.sleep(interval_seconds)
        
    except KeyboardInterrupt:
        print("\n[!] Shutdown sequence received. Sentry offline. Master ledger secured.")
        break