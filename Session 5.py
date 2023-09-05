list = [
    {'species' : 'zebra', 'name' : 'Penelope'},
    {'species' : 'penguin', 'name' : 'Jenn'},
    {'species' : 'elephant', 'name' : 'Harris'},
    {'species' : 'flamingo', 'name' : 'Florence'},
]

for i in list:
    print(i['species'])

# writing to a file
with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nAna'
    text_file.write(people)

# reading from a file
with open('people.txt', r) as text_file:
    contents = text_file.read()
print(contents)

# write a user input to a file
ask = input('Please add a new to-do item:')

# instead of w+ we can use a and then we append to the existing list
with open('to-do.txt', 'w+') as to_do:
    to_do.write(ask)

# writing a csv
import csv
field_names = ['name', 'age']
data = [
    {'name' : 'Jill', 'age' : 32},
    {'name' : 'Sara', 'age' : 28},
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)

# reading a csv
import csv
with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))

# read the csv file
import csv
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
