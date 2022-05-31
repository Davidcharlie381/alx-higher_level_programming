#!/usr/bin/python3
def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % (3 * 5) == 0:
            print("FizzBuzz")
        else:
            print(num)
        num += 1
