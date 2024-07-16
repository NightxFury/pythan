name = input("enter your name:")

print("Hello", name)

marks = int(input("enter your marks :"))
if 90 <= marks <=100 :
    print("your grade is A+",name)
    print("Very good")
elif 80 <= marks < 90 :
    print("Your grade is A", name)
    print("Very good")
elif 70 <= marks < 80:
    print("Your grade is B", name)
elif 60 <= marks <70 :
    print("Your grade is C", name)
elif 50 <= marks < 60 :
    print("Your grade is D")
elif 45 <= marks < 50 :
    print("Your grade is P")
elif marks >= 45 :
    print("You are fail")
    print("Better luck next time")

