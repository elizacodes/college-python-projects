# This program will ask you to enter a line of
# text and it will portray it backwards.

def get_text():
    text = input("Enter a line of text: ")

    return text


def format_text(text):
    text = text.strip()
    result = ""
    while True:
        index = text.find(" ")
        if index < 0:
            if len(text) > 0:
                result = result + text
            break
        else:
            result = result + text[0:index] + ' '
            text = text[index + 1:]
            text = text.strip()

    return result


def main():
    text = get_text()
    result = format_text(text)
    result = result[::-1]
    print(result)

main()
