# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
person = {
  'firstname': 'Deepak',
  'lastname': 'Vadithala',
  'age': 39
}

# print(person['firstname'])
# person['phone'] = '07455'

# print(person)

person2 = person.copy()
print(id(person))
print(id(person2))