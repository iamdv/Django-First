# A List is a collection which is ordered and changeable. Allows duplicate members.
# numbers = [1, 2, 3]
numbers = list((1,2,3))
print(numbers)
print(type(numbers))

fruits = ['Apples', 'Grapes', 'Oranges']

fruits.append('Mangoes')
print(fruits)

# Insert into a position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from a position
print(fruits.pop(2))
print(fruits)