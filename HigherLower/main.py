import random
from art import logo
from art import vs
from game_data import data
A = random.randint(0, len(data) - 1)
B = random.randint(0, len(data) - 1)
score = 0
while True:
    

    print(logo)
    print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}")

    print(vs)

    print(f"Against B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == 'A' and data[A]['follower_count'] > data[B]['follower_count']:
        print("That's right! A has more followers!")
        score += 1
        B = random.randint(0, len(data) - 1)
    elif choice == 'B' and data[A]['follower_count'] < data[B]['follower_count']:
        print("That's right! B has more followers!")
        score += 1
        A = random.randint(0, len(data) - 1)
    else:
        print(f"That's wrong. Final score: {score}")
        break