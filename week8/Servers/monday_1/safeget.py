import requests

def safe_get(url):
    request=requests.get(url)
    if request.status_code == 200:
        return request.json()
    if request.status_code == 404:
        return None
    raise Exception(request.status_code)

a=safe_get("http://127.0.0.1:8000/users/jj")
print(a)