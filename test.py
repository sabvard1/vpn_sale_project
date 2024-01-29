import requests

cookies = {
    'lang': 'en-US',
    'session': 'MTcwNTk0OTkzOXxEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCel9oQmtCQWdFSGMyRmlkbUZ5WkFFTFUyRmlaWEpBUURFek5qa0F8CKmu616B6aECbOl97SEPeC9obbZ5GnoJQ8VcLX5mJV0=',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

response = requests.get("http://tests.ss22ss.online:8443/panel/api/inbounds/getClientTraffics/sabvard2@gmail.com", cookies=cookies, headers=headers, verify=False)
aa = response.json()
print(response.text)
print(response.text)
print(aa["obj"]["email"])