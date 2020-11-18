import random


def main():
    print("This thing will take a bunch of city names, shuffle them about and then whittle them down to a list\n"
          "about a third of the size. This lets you blend different namebases to create new, unique ones.\n"
          "For the purpose of being used with Azgaar's FMG entering a list of around 300 city names is best.\n"
          "Paste them is as you would find them in the FMG, one large block with no spaces.\n")
    cities = input("Enter cities: ")  # takes user input, stores as cities
    namebase = cities.split(",")  # takes input and stores in namebase as list
    random.shuffle(namebase)  # shuffles the list elements around randomly
    removed = []  # empty list, will store elements that are removed

    while len(namebase) >= len(removed) // 3:
        num = random.randint(0, len(namebase))
        item = namebase[num-1]
        removed.append(item)
        namebase.remove(item)
    # this takes the namebase entered and whittles it down to a third of it's previous size

    print(*namebase, sep=",")  # prints what remains of namebase seperated by commas
    print()


main()
