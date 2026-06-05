import pandas as pd
import time

def clean_market_payload(raw_json):
    """Parses raw JSON, drops null values, and injects timestamps."""
    if not raw_json or 'errors' in raw_json:
        return None
        
    extracted_items = raw_json['data']['items']
    df = pd.DataFrame(extracted_items)
    
    # Drop items that don't have a valid 24-hour average price
    df = df.dropna(subset=['avg24hPrice'])
    
    # Inject extraction timestamp
    df.insert(0, 'Timestamp', time.strftime("%Y-%m-%d %H:%M:%S"))
    
    return df

if __name__ == "__main__":
    print("[+] Data Cleaner Module initialized and ready for payload.")