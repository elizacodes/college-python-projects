# This program will take the names and addresses
# from file addresses.txt and place them in one
# single line.

def read_file():
  data = []

  try:
    f = open("addresses.txt","r")
    x = f.readlines()
    for i in x:
      data.append(i.strip())
  except:
    print("Something went wrong.")
  
  return data


def display_address(data):
    lineNumber = 1
    first = ""
    last = ""
    address = ""
    city = ""
    state = ""
    postal = ""
    for i in range(0, len(data)):
        if lineNumber == 1:
            index = data[i].find(" ")
            first = data[i][0:index]
            last = data[i][index + 1:]
        elif lineNumber == 2:
            address = data[i]
        elif lineNumber == 3:
            index = data[i].find(",")
            city = data[i][0:index]
            statePostal = data[i][index + 2:]
            index = statePostal.find(" ")
            state = statePostal[0:index]
            postal = statePostal[index + 1:]
            display_results(first, last, address, city, state, postal)
        elif lineNumber == 4:
            lineNumber = 0
        lineNumber += 1


def display_results(first, last, address, city, state, postal):
    print(f"{last}, {first}, {address}, {city}, {state}, {postal}.")


def main():
    data = read_file()
    display_address(data)

main()
