"""
sum of even first even numbers
"""

numbers = 2

even_sum = 0

while numbers <= 20 :
    even_sum = even_sum + numbers
    numbers = numbers + 2
    print(even_sum)
