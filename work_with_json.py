import requests
import json

var_dict1 = dict(Age=24, Name='Ally')  # создание словаря
print(var_dict1)

var_dict2 = {"Age": 24, "Name": 'Ally'}  # создание словаря
print(var_dict2)

var_dict3 = {}  # создание словаря
var_dict3["Age"] = 24
var_dict3["Name"] = 'Ally'
print(var_dict3)

var_dict4 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": {
        "streetAddress": "Московское ш., 101, кв.101",
        "city": "Ленинград",
        "postalCode": 101101
    },
    "phoneNumbers": [
        "812 123-1234",
        "916 123-4567"
    ]
}
print(type(var_dict4))

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url) # возврощает объект RESPONSE (объект)
# У RESPONSE объекта статус код {ключ: значение}
if response.status_code == 200:
    print("OK")
else:
    print ("False")
json_data = response.content.decode() #Мы возврощаем декодированные из байтов в строку (строка)
airlines = json.loads(json_data) #Мы получаем диктионару
print(type(airlines))
# print(json_data)
#
# with open('data.json', 'w') as file:
#     json.dump(json_data, file)
    # json.dumps()

# with open('src/dist/new_file.json', 'r') as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()