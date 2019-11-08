units = int(input("Please choose 1:cm 2:inches "))
while units > 2 or units < 1:
    units = input("Please choose between one or two")
if units == 1:
    h = float(input("Please input the height of the room in cm "))
    w = float(input("Please input the width of the room in cm "))
    d = float(input("Please input the depth of the room in cm "))
elif units == 2:
    h = float(input("Please input the height of the room in inches "))
    w = float(input("Please input the width of the room in inches "))
    d = float(input("Please input the depth of the room in inches "))

if units == 1:
    print("You need", ((h*w)*d), "ml of paint to paint the walls")
elif units == 2:
    print("You need", (((h*w)*d)*2.54), "ml of paint to paint the walls")
