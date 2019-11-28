import random
import time

money = 100

coin_flip_wins = 0
coin_flip_losses = 0

cho_han_wins = 0
cho_han_losses = 0

war_wins = 0
war_losses = 0
war_ties = 0

# Write your game of chance functions here
def coin_flip(bet, guess):

    print()

    global money
    global coin_flip_wins
    global coin_flip_losses

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
            coin_flip_wins += 1
            return "And the flip was..." + side.capitalize() + "! You win" + " +$" + str(
                bet) + ". balance is now " + "$" + str(money)

        else:
            money -= int(bet)
            coin_flip_losses += 1
            return "And the flip was..." + side.capitalize() + "! You lose" + " -$" + str(
                bet) + ". balance is now " + "$" + str(money)

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


    print()

    global money
    global cho_han_wins
    global cho_han_losses

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


    if bet_not_int == False and bet_under == False and bet_over == False and guess_not_int == False and guess_under == False and guess_over == False:
        if (num % 2) == (guess % 2):
            money += int(bet)
            cho_han_wins += 1
            return "And the roll was..." + even_or_odd + "! (" + str(num1) + " + " + str(num2) + " total: " + str(
                num) + ") You win" + " +$" + str(bet) + ". balance is now " + "$" + str(money)
        else:
            money -= int(bet)
            cho_han_losses += 1
            return "And the roll was..." + even_or_odd + "! (" + str(num1) + " + " + str(num2) + " total: " + str(
                num) + ") You lose" + " -$" + str(bet) + ". balance is now " + "$" + str(money)




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


def war(bet):


    print()

    global money
    global war_wins
    global war_losses
    global war_ties

    try:
        bet = int(bet)
    except ValueError:
        return "ERROR. bet must be a number."


    if money < bet:
        return "ERROR. Not enough money."

    elif bet < 1:
        return "ERROR. Bet must be at least $1."

    cards = ['Ace of spades', 'Two of spades', 'Three of spades', 'Four of spades', 'Five of spades', 'Six of spades',
             'Seven of spades', "Eight of spades", 'Nine of spades', 'Ten of spades', 'Jack of spades',
             'Queen of spades', 'King of spades', 'Ace of hearts', 'Two of hearts', 'Three of hearts', 'Four of hearts',
             'Five of hearts', 'Six of hearts', 'Seven of hearts', "Eight of hearts", 'Nine of hearts', 'Ten of hearts',
             'Jack of hearts', 'Queen of hearts', 'King of diamonds', 'Ace of diamonds', 'Two of diamonds',
             'Three of diamonds', 'Four of diamonds', 'Five of diamonds', 'Six of diamonds', 'Seven of diamonds',
             "Eight of diamonds", 'Nine of diamonds', 'Ten of diamonds', 'Jack of diamonds', 'Queen of diamonds',
             'King of diamonds', 'Ace of clubs', 'Two of clubs', 'Three of clubs', 'Four of clubs', 'Five of clubs',
             'Six of clubs', 'Seven of clubs', "Eight of clubs", 'Nine of clubs', 'Ten of clubs', 'Jack of clubs',
             'Queen of clubs', 'King of clubs']
    cards_value = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4,
                   5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ]

    p1 = random.randint(0, 51)
    p2 = random.randint(0, 51)
    while p1 == p2:
        p1 = random.randint(0, 51)
        p2 = random.randint(0, 51)

    p1_c_value = cards_value[p1]
    p2_c_value = cards_value[p2]

    p1_card = cards[p1]
    p2_card = cards[p2]

    if p1_c_value == p2_c_value:
        war_ties += 1
        return "You pulled: " + p1_card + " He pulled: " + p2_card + " Its a tie! +$0. money still now " + str(money)

    elif p1_c_value > p2_c_value:
        money += bet
        war_wins += 1
        return "You pulled: " + p1_card + ". He pulled: " + p2_card + ". You win +$" + str(
            bet) + ". money is now " + str(money)


    else:
        money -= bet
        war_wins += 1
        return "You pulled: " + p1_card + ". He pulled: " + p2_card + ". You lose -$" + str(
            bet) + ". money is now " + str(money)




def roulette():
    print()



# Call your game of chance functions here

def choose():
    global money

    while money > 0:
        print()
        game = input("What game do you want to play? input 1:Coin-Flip, 2:Cho-Han, 3:War, 4:Roulette, 5:Withdraw ")  # todo roulette_wins
        print()


        try:
            if int(game) == 1:
                print(coin_flip(input("Coin-Flip      Bet "), input("Coin-Flip    Guess ")))
            elif int(game) == 2:
                print(cho_han(input("Cho-Han      Bet "), input("Cho-Han    Guess ")))
            elif int(game) == 3:
                print(war(input("War      Bet ")))
            elif int(game) == 4:
                print("Sorry we currently don't have this game published yet. Stay tuned")
            elif int(game) == 5:
                print("You are withdrawing with " + str(money) + ".")
                time.sleep(1)
                print()
                money = -1
                if coin_flip_wins >= 1 and coin_flip_losses >= 1:
                    coin_flip_w_l_ratio = (coin_flip_wins / coin_flip_losses) * 100
                    coin_flip_w_l_ratio = int(coin_flip_w_l_ratio)
                    print("Coin-Flip win/loss ratio: " + str(coin_flip_w_l_ratio))

                if cho_han_wins >= 1 and cho_han_losses >= 1:
                    cho_han_w_l_ratio = (cho_han_wins / cho_han_losses) * 100
                    cho_han_w_l_ratio = int(cho_han_w_l_ratio)
                    print("Cho Han win/loss ratio: " + str(cho_han_w_l_ratio))

                if war_wins >= 1 and war_losses >= 1:
                    war_w_l_ratio = (war_wins / war_losses) * 100
                    war_w_l_ratio = int(war_w_l_ratio)
                    print("War win/loss ratio: " + str(war_w_l_ratio))
                if war_ties >= 1:
                    print("Amount of War ties: " + war_ties)




        except:
            print("Wrong input")
            if money > 0:
                choose()
    if money == 0:
        print("You are out of money.")
        time.sleep(1)
        if coin_flip_wins >= 1 and coin_flip_losses >= 1:
            coin_flip_w_l_ratio = (coin_flip_wins / coin_flip_losses) * 100
            coin_flip_w_l_ratio = int(coin_flip_w_l_ratio)
            print("Coin-Flip win/loss ratio: " + str(coin_flip_w_l_ratio))

        if cho_han_wins >= 1 and cho_han_losses >= 1:
            cho_han_w_l_ratio = (cho_han_wins / cho_han_losses) * 100
            cho_han_w_l_ratio = int(cho_han_w_l_ratio)
            print("Cho Han win/loss ratio: " + str(cho_han_w_l_ratio))

        if war_wins >= 1 and war_losses >= 1:
            war_w_l_ratio = (war_wins / war_losses) * 100
            war_w_l_ratio = int(war_w_l_ratio)
            print("War win/loss ratio: " + str(war_w_l_ratio))
        if war_ties >= 1:
            print("Amount of War ties: " + war_ties)
choose()


