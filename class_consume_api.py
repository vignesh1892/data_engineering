import requests

##response = requests.get("http://127.0.0.1:8000/addnum/18/3",headers={"Content-Type":"application/json"})

BASE_URL = "https://jsonplaceholder.typicode.com"

#GET API consume
response = requests.get(f"{BASE_URL}/posts/1",headers={"Content-Type":"application/json"})
print(f"status code:{response.status_code}")
print(f"Response:{response.json()}")

##post method
new_post = {
    "title": "Hello API",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=new_post,headers={"Content-Type":"application/json"})
print(f"status code:{response.status_code}")
print(f"Response:{response.json()}")
