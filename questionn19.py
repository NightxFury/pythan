"""
write a program to add first n terms of following series using a for loop:
1/1!+1/2!+1/3!+1/4!+......+1/n!
"""
n = int(input("Enter a number:"))
total = 0
i = 1
f= 1
while i < n:
    f = f*i
    total = total+i/f
    i= i+1
    print(total)