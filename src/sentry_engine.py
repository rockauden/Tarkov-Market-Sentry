import time
import os
from api_client import fetch_live_market_data
from data_cleaner import clean_market_payload

print("--- 🟢 Tarkov Market Sentry: AUTONOMOUS ENGINE ONLINE ---")

OUTPUT_FILE = "../data/live_market_ledger.csv" 
INTERVAL_SECONDS = 60 

print(f"[!] Sentry deployed. Monitoring live Tarkov API.")
print(f"[!] Logging to '{OUTPUT_FILE}' every {INTERVAL_SECONDS} seconds.")
print("[!] Press 'Ctrl + C' to disengage.\n")

cycle_count = 1

while True:
    try:
        print(f"[Cycle {cycle_count}] Fetching live market data...")
        
        # 1. EXTRACT
        raw_data = fetch_live_market_data()
        
        # 2. TRANSFORM
        if raw_data:
            df = clean_market_payload(raw_data)
            
            if df is not None and not df.empty:
                # 3. LOAD
                os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
                file_exists = os.path.exists(OUTPUT_FILE)
                df.to_csv(OUTPUT_FILE, mode='a', index=False, header=not file_exists)
                
                print(f"[+] Cycle {cycle_count} Success. {len(df)} live items secured and appended.")
            else:
                print(f"[-] Cycle {cycle_count} failed during data transformation.")
        else:
            print(f"[-] Cycle {cycle_count} failed to fetch data from API.")
            
        cycle_count += 1
        time.sleep(INTERVAL_SECONDS)
        
    except KeyboardInterrupt:
        print("\n[!] Shutdown sequence received. Sentry offline. Master ledger secured.")
        break