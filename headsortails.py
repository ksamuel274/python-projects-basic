# This program would play heads or tails
import random
print("Welcome to heads or tails game\nThe computer will pick heads or tails for you\nAre you ready?")
coin = random.randint(0, 1)

if (coin == 1):
    print("Heads")
else:
    print("Tails")
