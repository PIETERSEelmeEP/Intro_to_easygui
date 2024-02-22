import easygui
import random

number = random.randint(a=0, b=5)
print(number)

words = ["bat", "cat", "hat", "mat"]
my_word = random.choice(words)
print(my_word)

friend = "Sarah"
letter = random.choice(friend)
print(letter)
print(friend[3])

# name = easygui.enterbox("Hey, What's your name?")
# print(name)
#
# age = easygui.integerbox("How old are you?")
# carry_on = easygui.buttonbox("Do you want to continue?",
#                              choices=["Yes", "No", "Don't care"],
#                              title="Continue")
#
# welcome = easygui.msgbox("Welcome to Easygui", title="Welcome")
#
# gender = easygui.buttonbox("Choose gender", title="Gender",
#                            choices=["Male", "Female", "Other"])
