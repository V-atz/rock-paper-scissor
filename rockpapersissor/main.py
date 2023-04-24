import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#defining images
game_image = [rock,paper,scissor]
#taking user input
user_choice = int(input("What's your choice ? \nEnter 0 for rock, enter 1 for paper and 2 for scissor\n"))
print(game_image[user_choice])
#generating random input from computer
computer_choice = random.randint(0,2)
print(game_image[computer_choice])
#rules
#Rock wins against scissors
#paper wins against rock
#scissors wins against paper
if user_choice >2 or user_choice < 0 :
    print("Enter a valid number !")
elif user_choice > computer_choice :
    print("You won")
elif computer_choice > user_choice :
    print("You lost")
elif user_choice == 0 and computer_choice == 2 :
    print("You lost")
elif computer_choice == 0 and user_choice == 2 :
    print("You won")
elif user_choice ==  computer_choice :
    print("It's a draw")