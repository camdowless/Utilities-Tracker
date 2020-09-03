from openpyxl import *

class Person:
    def __init__(self, name, utility, paid):
        self.name = name
        self.utility = utility
        self.paid = paid
        self.owes = 0
people = list()
total = 0

names = ["Evan", "Cam", "Zach", "West"]
utils = ["Electric", "Gas", "WiFi", "Water"]

for n,u in zip(names,utils):
    people.append(Person(n,u,int(input(f"Price for {u}:  "))))


for p in people:
    #print(f"{p.name}, {p.utility}, ${p.paid}\n")
    total += p.paid
#print(f"Total: ${total}")


each = total / 4
for p in people:
    if p.name != "Evan":
        p.owes = each - p.paid
        print(f"{p.name} owes Evan ${p.owes}")


