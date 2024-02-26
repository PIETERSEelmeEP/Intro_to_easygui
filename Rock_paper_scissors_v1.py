import easygui
import random

weapon = ["Rock", "Paper", "Scissors"]

while True:
    continue_game = easygui.buttonbox(f"Welcome to Pock-Paper_Scissors\nRock "
                                      f"eats scissors\nScissors beats paper\n"
                                      f"Paper beats rock\n\nDo you want to "
                                      f"play?", choices=["Yes", "No"],
                                      title="Welcome and Rules")
    if continue_game == "Yes":
        computer_weapon = random.choice(weapon)
        my_weapon = easygui.buttonbox(f"Choose your weapon",
                                      title="Choose Weapon",
                                      choices=["Rock", "Paper", "Scissors"])
        easygui.msgbox(f"You chose {my_weapon} and the computer chose "
                       f"{computer_weapon}")
        if my_weapon == computer_weapon:
            easygui.msgbox(f"This was a draw")
        elif my_weapon == "Paper" and computer_weapon == "Scissors" or \
                my_weapon == "Scissors" and computer_weapon == "Rock" or \
                my_weapon == "Rock" and computer_weapon == "Paper":
            easygui.msgbox(f"You lost")
        else:
            easygui.msgbox(f"You won")
    else:
        break
