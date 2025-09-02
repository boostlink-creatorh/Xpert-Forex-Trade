# Tastytrade API Integration

## 🔐 Setup
- Add `TASTYTRADE_TOKEN` and `ACCOUNT_ID` to `.env`
- Use `tastytrade_api.py` to fetch positions and check profit thresholds

## 🧠 Logic
- Pull positions via API
- Calculate P/L ratio
- Trigger Slack alert if threshold met

## 🧪 Edge Cases
- Token expiry → fallback to refresh logic
- Missing max-profit → default to $1 for ratio calc
