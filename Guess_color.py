#!/usr/bin/env python

import random

def main():
    #Choose rainbow color
    print("Guess the color!")

    rainbow = ["Merah", "Jingga", "Kuning", "Hijau", "Biru", "Indigo", "Ungu"]
    x = random.choice(rainbow)
    guess = None

    while x!=guess:
        guess = input("Choose one color from rainbow")

        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Sorry u choose wrong color!".format(guess))
main()