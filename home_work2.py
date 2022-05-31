import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
zapros = requests.get(url)
otvet_decod = zapros.content.decode()
# print(type(otvet_decod))
otvet_dict = json.loads(otvet_decod)

with open ("home_work/get_one.json", "w") as file:
    json.dump(otvet_dict, file)