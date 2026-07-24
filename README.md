# Investment Research Vault

A listed public equity and ETF thesis portfolio documenting structured asset analyses, catalyst tracking, and valuation modeling.

## 📁 Repository Framework Layout
* `memos/` — individual thesis write-ups, organized by asset class and ticker (e.g. `memos/AU_Equities/BHP/thesis.md`)
* `financial_models/` — supporting models, including `financial_models/Core_ETFs/etf_universe.md`
* `WATCHLIST.md` — active candidate tracking matrix across core and speculative positions
* `MANDATE.md` — governance rules for thesis review cadence and drawdown triggers

## Portfolio Construction Approach
Positions are tracked across two tiers: a 70–80% "Baseline Engine" of core, lower-volatility allocations, paired with a 20–30% high-conviction "Alpha Satellite Engine" for speculative, thesis-driven positions.

## Research & Valuation Methodology
Each thesis in `memos/` follows a consistent structure to keep reasoning comparable across positions over time:
1. **Core thesis statement** — the central argument in one sentence, forcing clarity before detail.
2. **Macro/catalyst drivers** — the structural "why now" case, informed by company reports, industry commentary, and macro data (e.g. company annual/quarterly reports, ASX/Nasdaq announcements, analyst commentary from outlets like Morningstar).
3. **Primary underwriting metric** — one specific, trackable financial metric chosen to test the thesis against future reporting (e.g. segment revenue growth, not blended headline numbers).
4. **Quantitative "red line" violations** — pre-defined, numeric thresholds that would indicate the thesis is breaking, set before the fact to avoid retrospective rationalization.
5. **Valuation framework** — current price, trailing P/E, market cap, and dividend yield as a baseline, with bull/bear case price targets built from the catalyst thesis rather than a full discounted cash flow model at this stage.
6. **Conviction & sizing** — mapped against `MANDATE.md`'s position limits.

Data sources currently include company financial reports and announcements, sector/analyst commentary (e.g. Morningstar, ARK), and general market/macro data. This is deliberately a fundamentals-first, thesis-driven process rather than a quantitative/algorithmic one — cross-referencing broader analyst sentiment is used to stress-test conviction, not to anchor the view.

## 🎯 Active Performance Tracking Index

| Date | Ticker | Company Name | Entry Price | Current Price | Change | Target View | Core Catalyst Horizon | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-24 | AAPL | Apple Inc. | $333.74 | $321.66 | -3.62% | Bullish | M-Series Silicon / AI | Tracking |
| 2026-07-24 | BHP | BHP Group Ltd | $57.54 | $58.85 | +2.28% | Bullish | Infrastructure Copper | Tracking |

## 📅 Automated Review & Checkup Schedule
Per `MANDATE.md`, active theses undergo formal segment evaluation every 3–6 months upon release of corporate financial reports.

| Ticker | Company Name | Last Review | Next Scheduled Review | Core Focus Metrics to Verify |
| :--- | :--- | :--- | :--- | :--- |
| AAPL | Apple Inc. | 2026-07-24 | 2026-10-18 (3-Month Check) | Mac & Advanced Hardware Segment Revenue Growth |
| BHP | BHP Group Ltd | 2026-07-24 | 2027-01-18 (6-Month Check) | Copper Segment Revenue % of EBITDA & Production Guidance |

*Note: if an asset breaches its −10% or −15% structural drawdown boundary before its scheduled review date, an out-of-cycle emergency review memo is triggered.*

## Considered but Not Selected
Global market/security exposures reviewed and deliberately excluded from the current mandate, not overlooked:
* **Private equity / alternative assets** (venture capital, private credit, unlisted infrastructure) — excluded entirely; requires accredited investor status, large capital minimums, and multi-year illiquid lockups, none of which fit a retail, monthly-contribution mandate at this stage.
* **Emerging Markets (VGE, EEM)** — excluded for now; correlation to AU resources exposure already high via BHP satellite position.
* **Direct European/UK equities** — excluded; VGS already provides sufficient developed-market breadth without single-country concentration.
* **Commodities** (direct or via ETF, e.g. gold, oil) — excluded per `MANDATE.md`; commodity exposure already indirectly captured through BHP's resources thesis.
* **Forex** (currency trading/speculation) — excluded per `MANDATE.md`; FX exposure exists passively through offshore holdings (VGS, VTS, AAPL) rather than as an active strategy.
* **Cryptocurrency** — excluded per `MANDATE.md`'s asset universe restriction.
* **Options/derivatives** — excluded per `MANDATE.md`; no hedging or leveraged strategies in current mandate scope.
* **Direct fixed income** (bonds/bond ETFs) — not yet included; will be considered once the portfolio moves beyond the initial equity-only build phase.
* **REITs / listed property** — not yet included; overlaps conceptually with BHP's infrastructure thesis, avoiding double-exposure to similar macro drivers for now.

## ⚖️ Disclaimer
This repository documents personal investment research and reasoning for educational and career-development purposes only. Nothing here constitutes financial advice, a recommendation, or a solicitation to buy or sell any security. All figures, price targets, and valuations reflect a point-in-time personal view and may be outdated, incomplete, or wrong. Do your own research and consult a licensed financial adviser before making investment decisions.

---
*Maintained by Cohen Pikari ([github.com/cohen-pikari](https://github.com/cohen-pikari))*
