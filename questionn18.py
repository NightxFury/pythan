"""
Factorial
"""
numbers = int(input("Enter your number:"))
i = 1
fact = 1

while i <= numbers:
    fact *= i
    i += 1
    print(fact)
