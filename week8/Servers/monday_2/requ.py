import requests

square={"type": "square", "length": 29}
rectangle={"type": "rectangle", "length": 50, "width": 100}
circle={"type": "circle", "radius": 13}






a=requests.get("http://127.0.0.1:8002/shapes")
print(a.json())
# for s in a.json():
#     print(s)
print(a.status_code)
