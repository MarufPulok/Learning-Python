import random
from art import logo
is_game_over = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCard = []
computerCard = []
def calculateScore(cardList):
    if sum(cardList) == 21 and len(cardList) == 2:
       return 0 
    
    if 11 in cardList and sum(cardList) > 21:
        cardList.remove(11)
        cardList.append(1)
        # return sum(cardList)
    return sum(cardList)
def dealCard():
    return random.choice(cards)

# print(dealCard())
def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return "Lose, computer has blackjack"
    elif userScore == 0:
        return "Win, you have blackjack"
    elif userScore > 21:
        return "Lose, you busted"
    elif computerScore > 21:
        return "Win, computer busted"
    elif userScore > computerScore:
        return "Win"
    else:
        return "Lose"
for i in range(2):
    userCard.append(dealCard())
    computerCard.append(dealCard()) 
# print(userCard)
# print(computerCard)
print(logo)
while not is_game_over:
    userScore = calculateScore(userCard)
    computerScore = calculateScore(computerCard)
    print(f"Your Cards: {userCard}")
    print(f"Computer's first card: {computerCard[0]}")

    if userScore == 0 or computerScore == 0 or userScore > 21:
        is_game_over = True
    else:
        user_should_deal = input("Do you want to deal? (y/n) ")
        if user_should_deal == "y":
            userCard.append(dealCard())
        else:
            is_game_over = True

while computerScore !=0 and computerScore < 17:
    computerCard.append(dealCard())
    computerScore = calculateScore(computerCard)

print(f"Your Cards: {userCard}")
print(f"Your Score: {userScore}")
print("Computer's Cards: ", computerCard)
print(f"Computer's Score: {computerScore}")
print(compare(userScore, computerScore))