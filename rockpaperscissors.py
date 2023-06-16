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
cpu = random.randint(0, 2)

print("Welcome to Rock Paper Scissors")
player = int(
    input("What do you choose, Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(player)
player_decision = [player]
cpu_decision = [cpu]

if(cpu == 0):
    print(rock)
elif (cpu == 1):
    print(paper)
else:
    print(scissors)

if(player == 0):
    print(rock)
elif (player == 1):
    print(paper)
elif(player == 2):
    print(scissors)
else:
    print("You failed to follow instructions")

if (player_decision == cpu_decision):
    print("Its a tie!")
elif (player == 0 and cpu == 1):
    print("You Lose!")
elif (player == 0 and cpu == 2):
    print("You Win!")
elif (player == 1 and cpu == 0):
    print("You Win!")
elif (player == 1 and cpu == 2):
    print("You Lose!")
elif(player == 2 and cpu == 0):
    print("You Lose")
elif(player == 2 and cpu == 1):
    print("You win")
else:
    print("That was not an option\nYou Lose!")
