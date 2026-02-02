import requests

def get_session_token(email, password):
    login_url = "https://api.tastytrade.com/sessions"
    payload = {"login": email, "password": password}
    response = requests.post(login_url, json=payload)
    data = response.json()
    return data.get("data", {}).get("session-token")

def get_account_data(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.get("https://api.tastytrade.com/accounts", headers=headers)
    return response.json()
