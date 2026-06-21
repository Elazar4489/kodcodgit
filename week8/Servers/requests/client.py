import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
if response.status_code == 200:
    print("Got data:", response.json())
elif response.status_code == 404:
    print("Not found")
else:
    print(f"Unexpected status: {response.status_code}")
