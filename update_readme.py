import os
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
        print(f"Error: Could not find README.md")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    aapl_live = get_live_price("AAPL")
    bhp_live = get_live_price("BHP.AX")
    current_date = datetime.now().strftime("%Y-%m-%d")

    if aapl_live is not None:
        aapl_pct = ((aapl_live - 333.74) / 333.74) * 100
        aapl_sign = "+" if aapl_pct >= 0 else ""
        content = content.replace("$XXX.XX", f"${aapl_live:,.2f}")
        content = content.replace("+/-X.X%", f"{aapl_sign}{aapl_pct:.2f}%", 1)

    if bhp_live is not None:
        bhp_pct = ((bhp_live - 57.54) / 57.54) * 100
        bhp_sign = "+" if bhp_pct >= 0 else ""
        content = content.replace("$XX.XX", f"${bhp_live:,.2f}")
        content = content.replace("+/-X.X%", f"{bhp_sign}{bhp_pct:.2f}%")

    content = content.replace("2026-07-18", current_date)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully processed target replacements safely without changing document structure.")

if __name__ == "__main__":
    update_markdown_table()
