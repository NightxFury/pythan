"""
sum of odd numbers
"""
numbers = 1

total = 0
count =0
while numbers < 20 :
    if numbers % 2 != 0:
        total = total+numbers
    numbers = numbers+1
    print(total)