import pandas as pd
import matplotlib.pyplot as plt

def plot_market_trend(csv_path, target_item="LEDX Skin Transilluminator"):
    """Reads the local ledger and generates an enterprise trend chart."""
    try:
        df = pd.read_csv(csv_path)
        target_data = df[df['name'] == target_item]
        
        if target_data.empty:
            print(f"[-] No historical data found for {target_item}.")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(target_data['Timestamp'], target_data['avg24hPrice'], marker='o', linestyle='-', color='r')
        
        plt.title(f"Market Trend & Quality Analysis: {target_item}")
        plt.xlabel("Time of Extraction")
        plt.ylabel("Average 24h Price (RUB)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        print("[-] Ledger not found. Run the Sentry Engine to collect data first.")

if __name__ == "__main__":
    print("[+] Visualizer Module executing...")
    plot_market_trend("../data/live_market_ledger.csv")