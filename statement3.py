def trafficLight():
    signal = input("Enter the colour of the traffic light: ")
    if (signal not in ("RED", "YELLOW", "GREEN")):
        print("Please enter a valid Traffic Light colour in CAPITALS")
    else:
        value = light(signal)  # function call to light()
    if (value == 0):
        print("STOP, Your Life is Precious.")
    elif (value == 1):
        print("PLEASE GO SLOW.")
    else:
        print("GO!,Thank you for being patient.")


# function ends here

def light(colour):
    if (colour == "RED"):
        return (0);
    elif (colour == "YELLOW"):
        return (1)
    else:
        return (2)


# function ends here

trafficLight()
print("SPEED THRILLS BUT KILLS")





