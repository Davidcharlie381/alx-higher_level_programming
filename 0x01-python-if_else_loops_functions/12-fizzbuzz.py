#!/usr/bin/python3
F = "Fizz"
B = "Buzz"


def fizzbuzz():
    for num in range(1, 101):
        if (num % 3 and num % 5):
            print("%s%s" % (F, B), end=' ')
        elif (num % 3):
            print("%s" % (F), end=' ')
        elif (num % 5):
            print("%s" % (B), end=' ')
        else:
            print("%d" % (num), end=' ')
