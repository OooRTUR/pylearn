import  json

data = {
    "president":{
        "name": "Zaphod Bebbelbroz",
        "species": "Bettlegum"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

json_data = json.dumps(data, indent=4)
# decoded_data = json.loads(json_data)
#
# print(decoded_data)
# print(type(decoded_data))

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(type(data))