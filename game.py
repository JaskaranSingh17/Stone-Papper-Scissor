# Import the random module
import random
# Creating the count_rock, 'count_paper and count_scissors variables and set their initial values equal to 0.
count_rock = 0
count_paper = 0
count_scissors = 0

def update_counts(user_input):
  global count_paper, count_rock, count_scissors
  if user_input == 0:
    count_rock = count_rock + 1
  elif user_input == 1:
    count_paper = count_paper + 1
  elif user_input == 2:
    count_scissors = count_scissors + 1

def predict():
  if count_rock > count_paper and count_rock > count_scissors:
    pred = 0
  elif count_paper > count_rock and count_paper > count_scissors:
    pred = 1
  elif count_scissors > count_rock and count_scissors > count_paper:
    pred = 2
  else:
    pred = random.randint(0, 2)
  return pred

# Creating the player_score and comp_score variables.
player_score = 0
comp_score = 0

# Creating the update_scores() function.
def update_scores(user_input):
  global player_score, comp_score
  # Rock wins over scissors, scissors win over paper and paper wins over rock.
  pred = predict()
  if user_input == 0:
    if pred == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

  if user_input == 1:
    if pred == 0:
      print("\nYou played PAPER, computer played ROCK.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played PAPER, computer played PAPER.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played PAPER, computer played SCISSORS.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

  if user_input == 2:
    if pred == 0:
      print("\nYou played SCISSORS, computer played ROCK.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played SCISSORS, computer played PAPER.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played SCISSORS, computer played SCISSORS.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

valid_entries = ['0', '1', '2']
while True:
  user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
  while user_input not in valid_entries:
    print("Invalid Input!!")
    user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
  user_input = int(user_input)
  update_scores(user_input)
  update_counts(user_input)
  if comp_score == 10:
    print("\nComputer Won!!")
    break
  elif player_score == 10:
    print("\nYou Won!!")
    break