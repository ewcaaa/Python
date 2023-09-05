# input function allows you to input data after the program has started running
# data comes out as a string
# {} is a placeholder

age = input('What is your age?')
name = input('What is your name?')
print('Hello, I am {}, {} years old.'.format(name, age))

fruit = input('What fruits do you like?')
num = input('How many fruits?')
print('You like {} and you would like to have {} pieces'.format(fruit, num))

# another option is to use this: print(f'hello {} {}')

# check what type is the variable
print(type(fruit))

friends = input('How many friends?')
pizza = int(int(friends)/2) # you can also just multiply by 0.5 and get the same answer
print("For {} friends  you need {} pizzas".format(friends, pizza))

# python modules
# module is code that someone else has written and we can reuse in our programs
# we import modules: import < math, datetime, timeit, re, copy >

import datetime
import pytz
x = datetime.datetime.now()
print(x)
# we can write from datetime import datetime, then we don't need to write it twice

import datetime as datetime
eastern_tz = pytz.timezone('US/Eastern')
now = datetime.datetime.now()
now_eastern = eastern_tz.localize(now)
print(now_eastern)

# for loops
# use it to iterate over sequences and not only sequences but any iterable object
# the execution will start and look for the first item in the sequence

for number in range(5):
    print('iteration ' + str(number))

for character in 'Banana':
    print('<' + character + '>')

names = ['Mary', 'Eva', 'Nina']
for name in names:
    print(name)

for number in range(5):
    print('executing for loop for number'.format(number + 1))

total = 0
for number in range(3):
    total = total +1
    print('The value each loop is: ' + str(total))
print('The total value is: ' + str(total))

# while loop
# the user does not know how many iterations there will be
# there is a possibility of infinite loops - be careful
# infinite loop --> while n > 0

store_capacity = 5

while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    store_capacity = store_capacity - 1
leaving_people = int(input('How many people have exited? '))
store_capacity = store_capacity + leaving_people

print('\nPlease wait for someone to exit the store.')

# functions
# functions are reusable, improve readability and avoid redundancy

def hello():
    print('Hello, class!')

for i in range(3):
    hello()

def some_function(name, job):
    print(name, 'is a', job)

some_function('Eva', 'developer')

# returning values from functions
# use a return statement
# once it's executed nothing else in the function is executed
# a python function always returns a value --> if you do not include any statements it automatically includes none

def sum(x, y):
    p = x + y
    print(p)

result = sum(10, 15)
print('result is: {}'.format(result))

# Homework
# 1
for number in range(100):
    output = 'o' * number
    print(output)

# the program outputs o times a number until that number hits 100; so the result would be
# o, oo, ooo, oooo...

# 2
def calculate_vat(amount):
    return amount * 1.2 # had to add return and the function works
    total = calculate_vat(100)
print(total)

