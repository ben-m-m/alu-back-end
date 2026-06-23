import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}

url = "https://www.reddit.com/r/python/about.json"

response = requests.get(url, headers=HEADERS)

print(response.status_code)
print(response.text[:200])