print("select your ride")
print("1. Bike")
print("2. Car")
choice=int(input("enter your choice"))
if choice==1:
    print("select your bike")
    print("1. Scootie")
    print("2. Honda")
    bchoice=int(input("enter your bike choice"))
    if bchoice==1:
        print("you selected scootie, rent is 100/day")
    else:
        print("you selcted honda, rent is 200/day")
else:
    print("select your car")
    print("1. Sedan")
    print("2. Audi")
    cchoice=int(input("enter your car choice"))
    if cchoice==1:
        print("you selected Sedan, rent is 350/day")
    else:
        print("you selcted Audi, rent is 1100/day")