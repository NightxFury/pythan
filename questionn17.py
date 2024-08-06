"""
stone paper scissor
"""
import random
def play_game():
    choice = ["rock", "paper", "scissor"]
    player_choice1 = random.choice(choice)
    player_choice2 = random.choice(choice)
    while True:
