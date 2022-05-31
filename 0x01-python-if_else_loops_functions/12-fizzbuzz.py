#!/usr/bin/python3
F = "Fizz"
B = "Buzz"


def fizzbuzz():
    num = 1
    while num <= 100:
        if (num % 3 and num % 5):
            print("{}{}".format(F, B), end='')
        elif num % 3:
            print("{}".format(F), end='')
        elif num % 5:
            print("{}".format(B), end='')
        else:
            print("{:d}".format(num), end='')
        num += 1
