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

#Write your code below this line 👇
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice=random.randint(0, 2)
if choice>2 and choice<0:
  print("Invalid Choice!")
  
elif choice==0 and computer_choice==0:
  print("You choose\n")
  print(rock)
  print(f"Computer choose \n{rock}")
  print("It's a draw!")

elif choice==1 and computer_choice==1:
  print("You choose\n")
  print(paper)
  print(f"Computer choose \n{paper}")
  print("It's a draw!")

elif choice==2 and computer_choice==2:
  print("You choose\n")
  print(scissors)
  print(f"Computer choose \n{scissors}")
  print("It's a draw!")
elif choice==0 and computer_choice==1:
  print("You choose\n")
  print(rock)
  print(f"Computer choose \n{paper}")
  print("You Lose!")
elif choice==0 and computer_choice==2:
  print("You choose\n")
  print(rock)
  print(f"Computer choose \n{scissors}")
  print("You Win!")

elif choice==1 and computer_choice==0:
  print("You choose\n")
  print(paper)
  print(f"Computer choose \n{rock}")
  print("You Win!")
elif choice==1 and computer_choice==2:
  print("You choose\n")
  print(paper)
  print(f"Computer choose \n{scissors}")
  print("You Lose!")

elif choice==2 and computer_choice==0:
  print("You choose\n")
  print(scissors)
  print(f"Computer choose \n{rock}")
  print("You Lose!")
elif choice==2 and computer_choice==1:
  print("You choose\n")
  print(scissors)
  print(f"Computer choose \n{paper}")
  print("You Win!")