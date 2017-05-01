# name = "Jones"
#
# if name is "Sam":
#     print("What's good Sam?")
# elif name is "Lucy":
#     print("Hey Lucy!")
# elif name is "Peter":
#     print("Supskies, Peter!")
# else:
#     print("WHO THE HELL ARE YOU?")

# name = ""
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
#
# print('Thanks brotato')

# spam = 0
# while spam < 5:
#     spam = spam + 1
#     if spam == 3:
#         continue
#     print('spam is ' + str(spam))

# print('My name is')
# for i in range(5):
#     print('Sam Fives Times ' + str(i))

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# import random, sys, os
# print(random.randint(1,10))

# def hello():
#     print('Sup dude')
#     print("What\'s good homie?")
#     print("Ciao buon giorno stronzino!")
#
# hello()
# hello()
# hello()


# def hello(name):
#     print('Sup ' + name)
#
# hello('Sam')
# hello('Jared')

# def plusOne(number):
#     return number + 1
#
# newNumber = plusOne(5)
# print(newNumber)

# print('cat', 'dog', 'reptile')
# print('cat', 'dog', 'reptile', sep='PENIS')

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
#
# def bacon():
#     ham = 101
#     eggs = 0
#
# spam()
#

# def div42by(divideBy):
#     try:
#         return(42) / divideBy
#     except:
#         print("There was an error, sillypants")
#
# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))
#


# THIS IS AN EXAMPLE OF INPUT VALIDATION BECAUSE IT FORCES YOU TO ENTER A NUMBER
# print("How many cats do you have, sir/madam?")
# numCats = input()
# try:
#     if int(numCats) >= 3:
#         print("Why the hell do you have so many cats?")
#     else:
#         print("That is a normal amount of cats that you have")
# except ValueError:
#     print("You didn't enter a number fool")

# THE GUESS THE NUMBER GAME

import random

print('Supskies, what yo name is?')
name = input()

print("Well, " + name + " , I am thinking of a number between 1 and twenty")
secretNumber = random.randint(1, 20)
for guessesTaken in range(1, 4):
    print('Take a guess, you')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low, my friend')
    elif guess > secretNumber:
        print('Your guess is a bit too high')
    else:
        break

if guess == secretNumber:
    print('You did it, ' + name + '!')
else:
    print("I'm sorry, the number I was thinking of was " + str(secretNumber))


print('You took this many guesses: ' + str(guessesTaken))





