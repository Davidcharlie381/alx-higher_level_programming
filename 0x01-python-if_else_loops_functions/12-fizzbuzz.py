#!/usr/bin/python3
F = "Fizz"
B = "Buzz"


def fizzbuzz():
    for num in range(1, 101):
        if (num % 3 and num % 5):
            print("{}{}".format(F, B), end='')
        elif num % 3:
            print("{}".format(F), end='')
        elif num % 5:
            print("{}".format(B), end='')
        else:
            print("{:d}".format(num), end='')
