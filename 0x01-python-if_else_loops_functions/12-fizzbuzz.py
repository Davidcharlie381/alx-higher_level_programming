#!/usr/bin/python3

F = "Fizz"
B = "Buzz"

def fizzbuzz():
    num = 1
    while num <= 100:
        if (num % 3 and num % 5 == 0):
            print("{}{}".format(F, B), end='')
        elif num % 5:
            print("{}".format(B), end='')
        elif num % 3:
            print("{}".format(F), end='')
        else:
            print(num, end='')
        num += 1
