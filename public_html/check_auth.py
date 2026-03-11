import os
from tastytrade.session import create_session

email = os.getenv("TASTYTRADE_EMAIL")
password = os.getenv("TASTYTRADE_PASSWORD")

print(f"🔍 Checking credentials for: {email}")

try:
    session = create_session(email, password)
    print("✅ Tastytrade session is active.")
    print(f"🔐 Session token: {session.access_token[:10]}...")  # Preview only
except Exception as e:
    print(f"❌ Authentication failed: {e}")
