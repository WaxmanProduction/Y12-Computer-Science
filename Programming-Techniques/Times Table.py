number = -1
time = 0
while number == 0 or number < 0:
    number = int(input("Please enter the positive integer you would like to multiply "))
while time == 0:
    time = int(input("Please enter the number of times you would like to multiply it "))

for x in range(1,time):
    print(x*number)
