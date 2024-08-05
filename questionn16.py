"""
guessing number
"""

number = 44

while True :
    guess = int(input("Enter your number:"))
    if guess == number:
        print("Congo")
        break
    else:
        print("Try again")