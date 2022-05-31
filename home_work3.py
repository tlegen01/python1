import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
zapros = requests.get(url)
otvet_decod = zapros.content.decode()
otvet_dict = json.loads(otvet_decod)

for sborka in otvet_dict:
    with open(f"home_work/get_one_{sborka['id']}.json", "w") as file:
        json.dump(sborka, file)