for i in range(0, 9):
    print('~' * i)

# boolean --> true or false
today = input('What day it is?')
is_monday = today == 'Monday'
print('Today is Monday: {}'.format(is_monday))

# equal to =
# not equal !=
# greater than >
# less than <
# greater than or equal to >=
# less than or equal to <=

tem = input('What is the temperature?')
is_freezing = float(tem) <= 0.0
print('The temperature is freezing: {}'.format(is_freezing))

veg = input("Does the burger have veg food?")
burger = input('What is the price of the burger?')
is_bur = (float(burger) <= 15.0)
res = is_bur and veg == 'yes'
print('The burger is in budget: {}'.format(is_bur))
print('Restaurant meets criteria: {}'.format(res))

meal_price = float(input('How much did the meal cost?'))
discount_choice = input('Do you have a discount? yes/no ')
discount_applicable = discount_choice == 'yes'
if meal_price >= 20 and discount_choice == 'yes':
    meal_price = meal_price - (meal_price * 0.1)
    print('Discount applied, the final price is: {}'.format(meal_price))
else:
    print('No discount')


occupation = 'manager'
city = 'scranton'
age = 50
name = 'Michael'
second_checker = city == 'scranton' and occupation == 'manager'
second_checker2 = city == 'scranton' or occupation == 'CEO'
print(second_checker)
print(second_checker2)

# if and else statement
password = input('password: ')
if password == 'jumanji':
    print('Success!')
else:
    print('That is wrong')

name = input('What is your name?')
is_admin = name == 'admin'
password = input('What is your password?')
is_password_correct = password == 'dinosaurs'
if is_admin and is_password_correct:
    print('Welcome')
if not is_admin or not is_password_correct:
    print('Go away')

dog_size = int(input('How big is the dog?'))
if dog_size > 75:
    print('This is a big dog')
elif dog_size < 25:
    print('That is a small dog')
else:
    print('That is an average dog')

# random
import random
random_int = random.randint(1, 100)
print(random_int)

import random
sides = int(input('How many slides does the die have?'))
random_int = random.randint(1, sides)
print('You rolled a {}'.format(random_int))

# homework
my_money = input('How much money do you have? ')
boat_cost = 20 + 5
if int(my_money) > int(boat_cost):
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')
