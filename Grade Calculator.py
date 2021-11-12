# This program will help calculate the average of
# the scores and show the highest, lowest, and
# the average of your scores.

def get_scores():
  scores = []

  while True:
    score = float(input("Enter a score or a negative value to stop: \n"))
    if score < 0:
      if len(scores) == 0:
        print("You must enter at least one value.")
      else:
        break
    else:
      scores.append(score)

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
  print("Your maximum is " + str(maximum))
  print("Your minimum is " + str(minimum))
  print("Your average is " + str(average))


def main():
  scores = get_scores()
  maximum = calculate_maximum(scores)
  minimum = calculate_minimum(scores)
  average = calculate_average(scores)
  display_results(maximum, minimum, average)

main()
