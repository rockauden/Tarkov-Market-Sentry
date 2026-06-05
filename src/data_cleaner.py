import pandas as pd
import time
import re

def clean_market_payload(raw_json):
    """Parses raw JSON, applies Regex cleaning, drops nulls, and injects timestamps."""
    if not raw_json or 'errors' in raw_json:
        return None
        
    extracted_items = raw_json['data']['items']
    df = pd.DataFrame(extracted_items)
    
    # 1. Existing Logic: Drop items that don't have a valid 24-hour average price
    df = df.dropna(subset=['avg24hPrice'])
    
    # 2. NEW LOGIC (Fulfilling the README promise): Regex Currency Normalization
    # This scrubs any accidental string formatting (like "₽50,000" or "50000 RUB") 
    # and strips it down to pure math-ready integers.
    def scrub_currency(val):
        if isinstance(val, str):
            # Regex: Strip out everything except numeric digits
            clean_str = re.sub(r'[^\d]', '', val)
            return int(clean_str) if clean_str else 0
        return val

    # Apply the surgical regex cleaning to the pricing columns
    df['avg24hPrice'] = df['avg24hPrice'].apply(scrub_currency)
    df['basePrice'] = df['basePrice'].apply(scrub_currency)
    
    # 3. Existing Logic: Inject extraction timestamp
    df.insert(0, 'Timestamp', time.strftime("%Y-%m-%d %H:%M:%S"))
    
    return df

if __name__ == "__main__":
    print("[+] Data Cleaner Module initialized and ready for payload.")
