import json

data = '''{
    "name": "Sherry",
    "phone": {
        "type": "intl",
        "number": "0123456789"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name = ', info["name"])
print('Attr = ', info["email"]["hide"])