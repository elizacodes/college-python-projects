# This program wil display the data read from cd_catalog.xml
# and build parallel arrays for each item. The total number
# of items and average of the price will be displayed.

import xml.etree.ElementTree as ET


def read_catalog(tag, root):
    result = []
    for cd in root.findall('CD'):
        try:
            result.append(cd.find(tag).text)
        except:
            print("WARN: CD XML missing element " + tag + "\n")
            result.append("UNKNOWN")
        if tag == 'PRICE':
            try:
                result[len(result) - 1] = float(result[len(result) - 1])
            except:
                print("WARN: The price is not a numeric value. \n")
                result[len(result) - 1] = 0

    return result


def display_results(title, artist, country, company, price, year):
    for i in range(0, len(title)):
        print(f"{title[i]} - {artist[i]} - {country[i]} - {company[i]} - {price[i]} - {year[i]}")
    print("\n" + str(len(title)) + " items - " + str(round(calculate_average(price),2)))


def calculate_average(price):
    total = 0.0
    for i in range(len(price)):
        total += float(price[i])

    return total / len(price)


def main():
    error = False
    try:
        tree = ET.parse('cd_catalog.xml')
    except:
        error = True
        print("Something went wrong reading your file.")
    if not error:
        root = tree.getroot()
        title = read_catalog('TITLE', root)
        artist = read_catalog('ARTIST', root)
        country = read_catalog('COUNTRY', root)
        company = read_catalog('COMPANY', root)
        price = read_catalog('PRICE', root)
        year = read_catalog('YEAR', root)
        if len(title) > 0:
            display_results(title, artist, country, company, price, year)
        else:
            print("WARN: Your file was empty.")

main()
