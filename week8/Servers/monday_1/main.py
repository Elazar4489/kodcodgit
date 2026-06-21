import requests

user=requests.get("https://jsonplaceholder.typicode.com/users/1")

print(f"Nane: {user.json()["name"]}")
print(f"Email: {user.json()["email"]}")
print(f"City: {user.json()["address"]["city"]}")

user1=requests.get("https://jsonplaceholder.typicode.com/posts")
user2=requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
print(len(user1.json()))
for k in user2.json():
    print(k)

print(user2.json())