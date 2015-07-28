#!/usr/bin/python

import random
import gettext

gettext.install('messages', './local', unicode=True)
gettext.translation('messages', './local', languages=['cn']).install(True)



guessesTaken = 0

print(_("Hello! What's your name?"))
print(_("Hello1! What's your name?"))
print(_("Hello2! What's your name?"))
myName = input()

number = random.randint(1, 20)
print("Well, {}, I am thinking of a number between 1 and 20.".format(myName))

while guessesTaken < 6:
    print("Take a guess.")
    guess = input()
    try:
        guess = int(guess)
    except ValueError:
        print("You should give me a number.")
        continue
 
    if guess < number:
        print("Your guess is too low.")
 
    if guess > number:
        print("You guess is too high.")
 
    if guess == number:
        break
 
if guess == number:
    print("Good job, {}! You guessed my number in {} guesses!".format(
        myName, guessesTaken))
 
if guess != number:
    print("Nope. The number I was thinking of was {}.".format(number))
