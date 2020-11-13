import random
import time

#Storing the number of rocks, papers, and scissors that the player has played
count_rock = 0
count_paper = 0
count_scissor = 0

#Storing the scores of the computer and the player
player_score = 0
comp_score = 0

def update_counts(user_input):
    global count_rock, count_scissor, count_paper
    if user_input == 0:
        count_rock = count_rock + 1
    elif user_input == 1:
        count_paper = count_paper + 1
    else:
        count_scissor = count_scissor + 1

def predict():
    if count_rock > count_scissor and count_rock > count_paper:
        pred = 0
    elif count_paper > count_rock and count_paper > count_scissor:
        pred = 1
    elif count_scissor > count_paper and count_scissor > count_rock:
        pred = 2
    else:
        pred = random.randint(0,2)
    return pred


def update_scores(user_input):
    global player_score, comp_score
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
    elif user_input == 1:
        if pred == 0:
            print("\nYou played PAPER, computer played ROCK.")
            player_score += 1
            print("\nComputer Score: ",comp_score,"\nYour Score: ", player_score)
        elif pred == 1:
            print("\nYou played PAPER, computer played PAPER.")
            print("\nComputer Score: ",comp_score,"\nYour Score: ", player_score)
        elif pred == 2:
            print("\nYou played PAPER, computer played SCISSORS.")
            comp_score = comp_score + 1
            print("\nComputer Score: ",comp_score,"\nYour Score: ", player_score)
    else:
        if pred == 0:
            print("\nYou played SCISSORS, computer played ROCK.")
            comp_score += 1
            print("\nComputer Score: ",comp_score,"\nYour Score: ", player_score)
        elif pred == 1:
            print("\nYou played SCISSORS, computer played PAPER.")
            player_score += 1
            print("\nComputer Score: ",comp_score,"\nYour Score: ", player_score)
        elif pred == 2:
            print("\nYou played SCISSORS, computer played SCISSORS.")
            print("\nComputer Score: ",comp_score,"\nYour Score: ", player_score)


valid_entries = ['0','1','2']
while True:
    user_input = input("Please enter 0 for Rock, 1 for Paper, and 2 for Scissors:")
    while user_input not in valid_entries:
        print("Invalid input!")
        user_input = input("Please enter 0 for Rock, 1 for Paper, and 2 for Scissors:")
    user_input = int(user_input)
    update_scores(user_input)
    update_counts(user_input)
    if comp_score == 10:
        print("Computer won!")
        break
    elif player_score == 10:
        print("You won!")
        break   
time.sleep(2)
print("Now you are going to exit the game!")
time.sleep(10)