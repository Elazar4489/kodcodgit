import requests
params = {"userId": 2}
response = requests.get(
"https://jsonplaceholder.typicode.com/posts",
params=params # becomes: /posts?userId=1
)
posts = response.json()
print(f"Found {len(posts)} posts for user 1")
for post in posts: # print first 3
    print(f" - {post}")


