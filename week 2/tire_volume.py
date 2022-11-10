from datetime import datetime
from math import pi

x = datetime.now()
width = int(input("What is the width of your tire in mm ex(205): "))
aspect = int(input("What is the aspect ratio of the tire ex(60): "))
diamiter = int(input("What is the diameter of the wheel in inches ex(15): "))
date = (f"{x.year}-{x.month}-{x.day}")

voulme = (pi * width ** 2 * aspect*(width * aspect + 2540 * diamiter)) / 10000000000
print(f'The approximate volume is {voulme:.2f} ')
purchase = input("Would you like to buy the tires? y/n: ")
if purchase == "y":
    phonenumber = input("What is your Phone number, so a rep can reach you? ")

with open("volumes.txt", "at") as volumes_file:

    print()
    print(f"{date}, {width}, {aspect}, {diamiter}, {voulme:.2f}", file=volumes_file)
    print(f"Customer phonenumber{phonenumber}", file=volumes_file)

