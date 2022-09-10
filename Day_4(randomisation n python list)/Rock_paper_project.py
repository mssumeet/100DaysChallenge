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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]

choice = int(input(" enter your choice 0 for rock,1 for paper, 2 for sissors"))


if choice>=3 or choice<0:
    print("You typed an invalid number , you loose!!....")
else:
    print(game_images[choice])
    computer_choice = random.randint(0,2)

    print(f"computer choose: ")
    print(game_images[computer_choice])


    if computer_choice== 0 and computer_choice == 2:
        print(" You Win ")

    elif computer_choice > choice:
        print (" You loose.... :( ")

    elif computer_choice == choice:
        print("Its a draw>>>>")

    elif computer_choice ==0 and choice==2:
        print("i loose")

    elif choice > computer_choice:
        print(" You loose.... :( ")

