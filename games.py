import random

money = 100


# Write your game of chance functions here
def coin_flip(bet, guess):
    global money

    bet_not_int = False
    bet_over = False
    bet_under = False
    bad_guess = False

    try:
        bet = int(bet)
    except ValueError:
        bet_not_int = True

    num = random.randint(1, 2)

    if bet_not_int == False:
        if money < bet:
            bet_over = True

        elif bet < 1:
            bet_under = True


    if guess.lower() == "heads" or guess.lower() == "h" or guess.lower() == "tails" or guess.lower() == "t":
        bad_guess = False
    else:
        bad_guess = True

    if bet_under == False and bad_guess == False and bet_not_int == False and bet_over == False:
        if num == 1:
            side = "Heads"
        else:
            side = "Tails"

        short_side = side[:1]

        if guess.lower() == side.lower() or guess.lower() == short_side.lower():
            money += int(bet)
            return "And the flip was..." + side.capitalize() + "! You win" + " +$" + str(bet) + ". balance is now " + "$" + str(money)

        else:
            money -= int(bet)
            return "And the flip was..." + side.capitalize() + "! You lose" + " -$" + str(bet) + ". balance is now " + "$" + str(money)

    if bad_guess == True and bet_not_int == True:
        return "ERROR. Bet must be a number, and guess must be heads or tails"

    elif bad_guess == True and bet_over == True:
        return "ERROR. Bet over, and guess must be heads or tails"

    elif bad_guess == True and bet_under == True:
        return "ERROR. Bet under, and guess must be heads or tails"

    elif bad_guess == True:
        return "ERROR. Guess not valid"

    elif bet_not_int == True:
        return "ERROR. Bet is not a number."

    elif bet_over == True:
        return "ERROR Not enough money."
    elif bet_under == True:
        return "ERROR. bet must be at least $1"


def cho_han(bet, guess):

    global money

    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num = num1 + num2
    if num % 2 == 0:
        even_or_odd = "Even"
    else:
        even_or_odd = "Odd"

    bet_not_int = False
    bet_over = False
    bet_under = False
    guess_not_int = False
    guess_over = False
    guess_under = False

    try:
        bet = int(bet)
    except ValueError:
        bet_not_int = True

    if bet_not_int == False:
        if money < bet:
            bet_over = True

        elif bet < 1:
            bet_under = True
    try:
        guess = int(guess)
    except ValueError:
        guess_not_int = True

    if guess_not_int == False:
        if guess > 12:
            guess_over = True

        elif guess < 2:
            guess_under = True


    if bet_not_int == False  and bet_under == False and bet_over == False and guess_not_int == False  and guess_under == False and guess_over == False:
        if (num % 2) == (guess % 2):
            money += int(bet)
            return "And the roll was..." + even_or_odd + "! (" + str(num1) + " + " + str(num2) + " total: " + str(num) + ") You win" + " +$" + str(bet) + ". balance is now " + "$" + str(money)
        else:
            money -= int(bet)
            return "And the roll was..." + even_or_odd + "! (" + str(num1) + " + " + str(num2) + " total: " + str(num) + ") You lose" + " -$" + str(bet) + ". balance is now " + "$" + str(money)



    if bet_not_int == True and guess_not_int == True:
        return "ERROR. Bet must be a number, and guess must be a number."

    elif bet_not_int == True and guess_over == True:
        return "ERROR. Bet must be a number, and guess must be 2 to 12."

    elif bet_not_int == True and guess_under == True:
        return "ERROR. bet must be a number, and guess must be 2 to 12."


    elif bet_over == True and guess_not_int == True:
        return "ERROR. Bet over, and guess must be a number."

    elif bet_over == True and guess_over == True:
        return "ERROR. Bet over, and guess must be 2 to 12."

    elif bet_over == True and guess_under == True:
        return "ERROR. Bet over, and guess must be 2 to 12."


    elif bet_under == True and guess_not_int == True:
        return "ERROR. Bet under, and guess must be a number."

    elif bet_under == True and guess_over == True:
        return "ERROR. Bet under, and guess must be 2 to 12."

    elif bet_under == True and guess_under == True:
        return "ERROR. Bet under, and guess must be 2 to 12."


    elif bet_not_int == True:
        return "ERROR. bet must be a number."
    elif bet_over == True:
        return "ERROR. Not enough money."
    elif bet_under == True:
        return "ERROR. Bet must be at least $1."

    elif guess_not_int == True:
        return "ERROR. Guess must be a number."
    elif guess_over == True:
        return "ERROR. Guess must be 2 to 12."
    elif guess_under == True:
        return "ERROR. Guess must be 2 to 12."




# Call your game of chance functions here

#print(coin_flip(input("Coin-Flip      Bet "), input("Coin-Flip    Guess ")))
print(cho_han(input("Cho-Han      Bet "), input("Cho-Han    Guess ")))
