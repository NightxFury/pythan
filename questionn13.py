"""
Write a program to print all even numbers that falls between two numbers entered from the user using while loop
"""
num1  = int(input("Enter your first number :"))
num2 = int(input("Enter your second number:"))

if num1 < num2:
    while num1 < num2:
        if num2 %2 == 0:
            print(num2)
            num2 = num2 +1
        elif num1 > num2:
            while num1>num2:
                if num1%2 == 0:
                    print(num1)
                    num1 =num1+1
                else:
                    print("Not valid")
