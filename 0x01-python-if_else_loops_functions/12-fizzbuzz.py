#!/usr/bin/python3
def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0:
            print("Fizz", end='')
        elif num % 5 == 0:
            print("Buzz", end='')
        elif num % 3 and number % 5 == 0:
            print("FizzBuzz", end='')
        else:
            print(num)
        num += 1
