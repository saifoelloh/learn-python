"""
    learning.01-basic
    ~~~~~~~~~~~~~~~~~

    Belajar python mulai dari awal

    :copyright: (c) 2020 by MOH SAIFOELLOH.
"""
print("Hello world")

NAME = "saipul"
print("Hello my name is", NAME)

A, B, C = 10, 11, 12
print(A, B, C)

def greeting(name="foo"):
    return "Hello "+name

NAME = str(input("What's your name ? "))
NAME.strip()
print(greeting(NAME))
print(NAME.lower())
print(NAME.upper())
print(NAME.capitalize())
print(NAME.title())

NUMBER = int(input("Input your number "))

def prime_calc(number=2):
    temp = True
    if number > 1:
        for i in range(2, 9):
            print(i, number)
            if not(number % i) and number is not i:
                temp = False
                break
    return "Your number is Prime Number" if temp else "Your's is not Prime Number"

print(prime_calc(NUMBER))
