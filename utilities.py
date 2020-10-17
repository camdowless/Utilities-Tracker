import sys
from datetime import datetime
import csv

class Person:
    def __init__(self, name, utility, paid):
        self.name = name
        self.utility = utility
        self.paid = paid
        self.owes = 0



def main():
    people = list()
    total = 0

    names = ["Evan", "Cam", "Zach", "West"]
    utils = ["Electric", "Gas", "WiFi", "Water"]

    write_to_file = sys.argv[1] if len(sys.argv) == 2 else False

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

    if write_to_file:
        entry = build_string(people, total)
        f = open("utilities.csv", 'a')
        f.write(entry)
        f.close()

def build_string(people, total):
    string = "\n"
    string = string + (datetime.now().strftime('%B'))
    for p in people:
        string = string + ',' + str(p.paid)
    string += (f",{total}")
    return(string)

if __name__ == "__main__":
    main()
