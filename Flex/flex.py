# This program is about a flex.

def get_cash():
    print("How much money do you have to flex on a Friday night?")
    cash = float(input())

    return cash


def display_result(recommendation):
    print("Our recommendation for you is: " + str(recommendation))


def main():
    cash = get_cash()
    if cash < 5 and cash > 0:
        recommendation = "Stay home. You don't have enough to flex."
        display_result(recommendation)
    elif cash == 5:
        recommendation = "Get a cup of coffee and relax at home."
        display_result(recommendation)
    elif cash > 5 and cash < 26:
        recommendation = "Go to the movies! Buy some popcorn."
        display_result(recommendation)
    elif cash >= 26 and cash <= 50:
        recommendation = "Flex on your friends and buy them dinner."
        display_result(recommendation)
    elif cash > 50:
        recommendation = "Hardcore flex!!! Do whatever you want with that money!"
        display_result(recommendation)
    else:
        print("You cannot put a negative value for cash. You must be in debt.")


main()
