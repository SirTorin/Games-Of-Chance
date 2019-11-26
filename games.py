import random

money = 100


# Write your game of chance functions here
def coin_flip(bet, guess):
    global money

    not_int_bet = False
    bet_too_big = False
    try_it2 = False
    try_it3 = False
    bad_guess = False

    try:
        bet = int(bet)
    except ValueError:
        not_int_bet = True

    num = random.randint(1, 2)

    if not_int_bet == False:
        try:
            if type(money) == type(bet):
                try_it3 = True
        except TypeError:
            ot_int_bet = True
        else:
            if money < int(bet):
                bet_too_big = True
            else:
                try_it2 = True
    if guess.lower() == "heads" or guess.lower() == "tails":
        bad_guess = False
    else:
        bad_guess = True


    if try_it2 == True and try_it3 == True and not_int_bet == False and not_int_bet == False:
        if num == 1:
            side = "Heads"
        else:
            side = "Tails"

        if guess.lower() == side.lower():
            money += int(bet)
            return "And the flip was..", side.capitalize() + "! You win!", "+$" + str(bet), "   balance is now", "$"+ str(money)

        elif guess.lower() == "heads" or guess.lower() == "tails":
            money -= int(bet)
            return "And the flip was..", side.capitalize() + ". You lose.", "-" + str(bet), "   balance is now", "$"+str(money)

    if bad_guess == True and not_int_bet == True:
        return "Bet is not a number and guess not valid"

    elif bad_guess == True and bet_too_big == True:
        return "Not enough money and guess not valid"

    elif not_int_bet == False and bet_too_big == False:
        return "Guess not valid"

    elif not_int_bet == True and bet_too_big == False:
        return "Bet is not a number."

    elif not_int_bet == False and bet_too_big == True:
        return "You do not have enough money."
    
# Call your game of chance functions here

print(coin_flip(input("Bet "), input("Guess ")))


