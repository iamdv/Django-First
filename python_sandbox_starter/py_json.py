# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# sample json
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 39}'

# Parse to Dict
user = json.loads(userJSON)

print(user)
print(type(user['first_name']))

car = {'make': 'ford', 'year': 1970}
carJSON = json.dumps(car)

print(carJSON)
print(type(carJSON))