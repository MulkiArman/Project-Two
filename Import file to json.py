import json

user = {
    "id": 1,
    "name": "Muhamad",
    "adress": "Karawang,jawa barat",
    "nickname": "Alson",
}


result = json.dumps(user)
print(result)
with open('example.json', 'w') as file:
    json.dump(user, file)
