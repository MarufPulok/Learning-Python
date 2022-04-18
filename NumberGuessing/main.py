import random
num_of_trials = 0
correct_answer = random.randint(1, 100)
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

if(choice == "easy"):
    num_of_trials = 10
elif (choice == "hard"):
    num_of_trials = 5
else:
    print("ivalid choice")



for i in range(num_of_trials):
    guess = int(input("Guess a number: "))
    if(guess == correct_answer):
        print("You win!")
        break
    elif(guess > correct_answer):
        print("Too high!")
        if (i != num_of_trials - 1):
            print("You have " + str(num_of_trials - i-1) + " guesses left.")
    else:
        print("Too low!")
        if (i != num_of_trials - 1):
            print("You have " + str(num_of_trials - i-1) + " guesses left.")
    if(i == num_of_trials - 1):
        print("You lose!")