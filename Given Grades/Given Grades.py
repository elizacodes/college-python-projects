# This program will help calculate the average of
# the scores and show the highest, lowest, and
# the average of the scores given from scores.txt

def read_file():
  data = []

  try:
    f = open("scores.txt","r")
    x = f.readlines()
    for i in x:
      data.append(i.strip())
  except:
    print("Something went wrong.")
  
  return data


def create_scores(data):
  scores = []

  for i in range(0, len(data)):
    if data[i] == "Name,Score":
      continue
    else:
      index = data[i].find(",")
      scores.append(float(data[i][index + 1:]))


  return scores


def calculate_average(scores):
    total = 0.0
    for i in range(len(scores)):
      total += scores[i]

    return total / len(scores)


def calculate_maximum(scores):
  maximum = scores[0]
  for i in range (1, len(scores)):
    if maximum < scores[i]:
      maximum = scores[i]

  return maximum


def calculate_minimum(scores):
  minimum = scores[0]
  for i in range (1, len(scores)):
    if minimum > scores[i]:
      minimum = scores[i]

  return minimum


def display_results(maximum, minimum, average):
  print("The maximum is " + str(maximum))
  print("The minimum is " + str(minimum))
  print("The average is " + str(round(average,2)))


def display_data(data):
  print("\nThis is the content of scores.txt.")
  for i in range(0, len(data)):
    print(data[i])


def main():
  data = read_file()
  if len(data) == 0:
    return
  scores = create_scores(data)
  average = calculate_average(scores)
  maximum = calculate_maximum(scores)
  minimum = calculate_minimum(scores)
  display_results(maximum, minimum, average)
  display_data(data)

main()
