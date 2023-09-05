from typing import List

carrots = int(input('How many carrots do you have?'))
rabbits = 6

if rabbits < carrots:
    print('There are not enough carrots')
elif rabbits > carrots:
    print('There are too many carrots')
else:
    print('You have the right number of carrots')

# lists
# list is an ordered collection of values
lottery_num = [1,2,3,4]

student = ['Hank', 'Kim', 'Ema']
print(student[2])

clothes = ['shorts', 'shoes', 't-shirt']
if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'
print(clothes[0])

# list functions
# min(), max(), len(), sorted(), reversed()
costs=[1, 4, 2, 7, 5, 2, 8]
print(len(costs))
print(max(costs))
print(min(costs))
print(sorted(costs))
print(list(reversed(costs)))

scores = [200, 6, 45, 199, 3, 17, 83, 21, 61, 99]
print(list(reversed(sorted(scores))))
# second option
print('Number', len(scores))
print('Max', max(scores))
print('Low', min(scores))
print(scores.sort(reverse=True)) # does not work

# append and in
stu_name = input('Which student are you looking for?')
name = ['ana', 'nika', 'jan']
if stu_name in name:
    print('{} is in the class'.format(stu_name))
else:
    print('{} is not in the class'.format(stu_name))

list = ['bread', 'flour', 'milk']
if 'bread' in list:
    list.append('butter')
print(list)

# for loops and lists
names = ['nika', 'ana', 'jan']
for name in names:
    print(name)

names = ['nika', 'ana', 'jan']
count = 0
for name in names:
    count = count + 1
print(count)

# dictionaries
person = {
    'name' : 'Jessica',
    'age' : 23,
    'height' : 172
}
print(person['name'])

place = {
    'name' : 'The Anchor',
    'post_code' : 'E14 6HY',
    'street_number' : '54',
    'location' : {
        'longitude' : 127,
        'latitude' : 63,
    }
}

print(place['name'], place['post_code'], place['street_number'])
print(place['location']['longitude'])

location = place['location']

print(location['longitude'])
print(location['latitude'])

people = [
    {'name' : 'Jessica', 'age' : 24},
    {'name' : 'Trish', 'age' : 25},
]

for i in people:
    print(person['name'])
    print(person['age'])

person1 = {'name' : 'Jessica', 'age' : 24}
print(person1['name'])
print(person1['age'])

person2 = {'name' : 'Trish', 'age' : 25}
print(person2['name'])
print(person2['age'])


fruits = [
    {'name' : 'apple', 'color' : 'red', 'price' : 0.12},
    {'name' : 'banana', 'color' : 'yellow', 'price' : 0.2},
    {'name' : 'pear', 'color' : 'green', 'price' : 0.19},
]

for i in fruits:
    print(i['name'])
    print(i['color'])
    print(i['price'])

# random choice
# choice() function in the random module returns a random item from a list
import random
colors = ['red', 'pink', 'orange']
chosen_color = random.choice(colors)
print(chosen_color)

name = ['nika', 'ana', 'jan', 'rok']
chosen_name = random.choice(name)
print(chosen_name)

# exercise
trees = [
    {'color' : 'green', 'height' : 2010},
    {'color' : 'yellow', 'height' : 2210},
]

new_tree = {
    'color' : 'black', 'height' : 3234
}

trees.append(new_tree)
print(trees)

# homework
shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]
print(shopping_list[0])
# item number one has a number 0

# I've started the program and included the chocolates and their prices.
# Finish the program by asking the user to input an item and then output its price.
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

# 2
ask = input('What kind of a chocolate do you like?')
if ask in chocolates:
    print(chocolates[ask])

# 3
import random

def draw():
    lucky_numbers = random.sample(range(1, 50), 6)
    return lucky_numbers

def play_week():
    people = []

    for a in range(0, 7):
        a = random.randint(10, 100)
        people.append(a)
    print("Winning numbers are :", people)

    totalpeople = sum(people)
    played_tickets = []

    for i in range(totalpeople):
        n = random.sample(range(1, 50), 6)
        played_tickets.append(n)

    decide_winners(played_tickets)

def decide_winners(played_tickets):
    lucky_nums = draw()
    right_guesses = [0, 0, 0, 0, 0, 0]

    for i in played_tickets:
        match = len(set(i) & set(lucky_nums))

        if match != 0:
            right_guesses[match - 1] += 1
    print(right_guesses)

play_week()


import random
lottery_ticket = [4, 10, 32, 52, 99, 5, 16]
random_lottery_numbers = []
while len(random_lottery_numbers) < 7:
     random_numbers = random.randrange(1, 100)
     if random_numbers not in random_lottery_numbers:
         random_lottery_numbers.append(random_numbers)
counter = 0

print('My choice:', lottery_ticket)
print('Winning numbers are:', random_lottery_numbers)

for entry in lottery_ticket:
    if entry in random_lottery_numbers:
        counter = counter + 1

if counter == 3:
    print('£20 for three matching numbers')
elif counter == 4:
    print('£40 for four matching numbers')
elif counter == 5:
    print('£100 for five matching numbers')
elif counter == 6:
    print('£10000 for six matching numbers')
elif counter == 7:
    print('£1000000 for seven matching numbers')
else:
    print('No luck, maybe next time!')