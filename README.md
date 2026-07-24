nano update_readme.py

nano update_readme.py

nano update_readme.py
import os
import re
import yfinance as yf
from datetime import datetime

def get_live_price(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        price = ticker.fast_info['lastPrice']
        if price is not None:
            return round(price, 2)
    except Exception:
        pass
    try:
        ticker = yf.Ticker(ticker_symbol)
        hist = ticker.history(period="1d")
        if not hist.empty:
            return round(hist['Close'].iloc[-1], 2)
    except Exception:
        pass
    return None

def update_markdown_table():
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print(f"Error: Could not find README.md at current location: {os.getcwd()}")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    aapl_live = get_live_price("AAPL")
    bhp_live = get_live_price("BHP.AX")
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 1. Update the AAPL row precisely using text replacement
    if aapl_live is not None:
        aapl_pct = ((aapl_live - 333.74) / 333.74) * 100
        aapl_sign = "+" if aapl_pct >= 0 else ""
        
        old_aapl_pattern = r"\| 2026-07-24 \| AAPL \| Apple Inc\. \| \$333\.74 \| \$XXX\.XX \| \+/-X\.X% \| Bullish \| M-Series Silicon / AI \| Tracking \|"
        new_aapl_row = f"| {current_date} | AAPL | Apple Inc. | $333.74 | ${aapl_live:,.2f} | {aapl_sign}{aapl_pct:.2f}% | Bullish | M-Series Silicon / AI | Tracking |"
        content = re.sub(old_aapl_pattern, new_aapl_row, content)

    # 2. Update the BHP row precisely using text replacement
    if bhp_live is not None:
        bhp_pct = ((bhp_live - 57.54) / 57.54) * 100
        bhp_sign = "+" if bhp_pct >= 0 else ""
        
        old_bhp_pattern = r"\| 2026-07-24 \| BHP \| BHP Group Ltd \| \$57\.54 \| \$XX\.XX \| \+/-X\.X% \| Bullish \| Infrastructure Copper \| Tracking \|"
        new_bhp_row = f"| {current_date} | BHP | BHP Group Ltd | $57.54 | ${bhp_live:,.2f} | {bhp_sign}{bhp_pct:.2f}% | Bullish | Infrastructure Copper | Tracking |"
        content = re.sub(old_bhp_pattern, new_bhp_row, content)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully processed target replacements safely without changing document structure.")

if __name__ == "__main__":
    update_markdown_table()
