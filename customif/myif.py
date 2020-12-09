#!/usr/bin/env python3

message = 'uhhhh '

# wrap connection in a float() to accept decimals as numbers
guess = float(input("Guess what number am I thinking of? its betwen 0 and 835: "))

# if input value was higher, lower, or equal to 5
if guess == 5:
    message = message + 'wow.. you did it.. good job or something like that'
elif guess <= 5:
    message = message + 'why would you guess that? it doesnt even make sense'
elif guess >= 5:
    message = message + 'nope, sorry you are not turtle enough'
else:
    message = message + 'seriously?... big oof'
print(message)
