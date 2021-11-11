# This program will ask the user for their first
# and last name, and then will display the
# last name first, then the initial of
# their first name.

def get_input():
    while True:
        print("Enter name (first, last):")
        name = input()
        index = name.find(",")
        if index >= 0:
            break

    return name


def get_first(name):
    index = name.find(",")
    if index < 0:
        first = ""
    else:
        first = name[0]
        first = first.strip()
    
    return first


def get_last(name):
    index = name.find(",")
    if index < 0:
        last = ""
    else:
        last = name[index + 1:]
        last = last.strip()

    return last


def display_results(first, last):
    print(f"{last}, {first}.")


def main():
    name = get_input()
    last = get_last(name)
    first = get_first(name)
    display_results(first, last)

main()
