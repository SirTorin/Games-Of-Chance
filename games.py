import random
import time

money = 100

coin_flip_wins = 0
coin_flip_losses = 0
coin_flip_profit = 0

cho_han_wins = 0
cho_han_losses = 0
cho_han_profit = 0

war_wins = 0
war_losses = 0
war_ties = 0
war_profit = 0

roulette_wins = 0
roulette_losses = 0
roulette_profit = 0


# Write your game of chance functions here
def coin_flip(bet, guess):

    print()

    global money
    global coin_flip_wins
    global coin_flip_losses
    global coin_flip_profit

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
            coin_flip_profit += int(bet)
            coin_flip_wins += 1
            return "And the flip was..." + side.capitalize() + "! You win" + " +$" + str(
                bet) + ". balance is now " + "$" + str(money)

        else:
            money -= int(bet)
            coin_flip_profit -= int(bet)
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
    global cho_han_profit

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
            cho_han_profit += int(bet)
            cho_han_wins += 1
            return "And the roll was..." + even_or_odd + "! (" + str(num1) + " + " + str(num2) + " total: " + str(
                num) + ") You win" + " +$" + str(bet) + ". balance is now " + "$" + str(money)
        else:
            money -= int(bet)
            cho_han_profit -= int(bet)
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
    global war_profit

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
        money += int(bet)
        war_profit += int(bet)
        war_wins += 1
        return "You pulled: " + p1_card + ". He pulled: " + p2_card + ". You win +$" + str(
            bet) + ". money is now " + str(money)


    else:
        money -= int(bet)
        war_profit -= int(bet)
        war_wins += 1
        return "You pulled: " + p1_card + ". He pulled: " + p2_card + ". You lose -$" + str(
            bet) + ". money is now " + str(money)




def roulette():

    global money
    global roulette_wins
    global roulette_losses
    global roulette_profit
    

    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
     "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "0", "00"]

    color = ['red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'black', 'red', 'black','red'
     ,"black" ,"red", "black", "red", "red", "black", "red", "black", "red", "black", "red", "black", "red", 'black', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', '0', '00']

    odd_even = ["odd", "even", "odd", "even", "odd", "even", "odd", "even", "odd", "even", "odd", "even", "odd", "even",
                "odd", "even", "odd", "even", "odd", "even", "odd", "even", "odd", "even", "odd", "even", "odd", "even",
                "odd", "even", "odd", "even", "odd", "even", "odd", "even", "0", "00"]
    
    row = ["row1", "row2", "row3", "row1", "row2", "row3", "row1", "row2", "row3", "row1", "row2", "row3", "row1", "row2",
     "row3", "row1", "row2", "row3", "row1", "row2", "row3", "row1", "row2", "row3", "row1", "row2", "row3", "row1", "row2", "row3",
      "row1", "row2", "row3", "row1", "row2", "row3", "0", "00"]
    
    _12 = ["1st twelve", "1st twelve", "1st twelve", "1st twelve", "1st twelve", "1st twelve", "1st twelve",
     "1st twelve", "1st twelve", "1st twelve", "1st twelve", "1st twelve", "2nd twelve", "2nd twelve", "2nd twelve", "2nd twelve",
     "2nd twelve", "2nd twelve", "2nd twelve", "2nd twelve", "2nd twelve", "2nd twelve", "2nd twelve", "2nd twelve", "3rd twelve",
      "3rd twelve", "3rd twelve", "3rd twelve", "3rd twelve", "3rd twelve", "3rd twelve", "3rd twelve", "3rd twelve","3rd twelve", "3rd twelve", "3rd twelve", "0", "00"]

    _18 = ["first_18", "first_18", "first_18", "first_18", "first_18", "first_18", "first_18", "first_18", "first_18", "first_18", "first_18", "first_18", "first_18",
     "first_18", "first_18", "first_18", "first_18", "first_18","second_18", "second_18", "second_18", "second_18", "second_18", "second_18", "second_18", "second_18",
      "second_18", "second_18", "second_18", "second_18", "second_18", "second_18", "second_18", "second_18", "second_18", "second_18", "0", "00"]

    split_two = ["00/0", "0/1", "0/2", "00/2", "00/3", "1/4", "2/5", "3/6", "4/7", "5/8", "6/9", "7/10", "8/11", "9/12", "10/13", "11/14", "12/15", "13/16", "14/17", "15/18",
    "16/19", "17/20", "18/21", "19/22", "20/23", "21/24", "22/25", "23/26", "24/27", "25/28", "26/29", "27/30", "28/31", "29/32", "30/33", "31/34", "32/35", "33/36", "36/35",
    "35/34", "33/32", "32/31", "30/29", "29/28", "27/26", "26/25", "24/23", "23/22", "21/20", "20/19", "18/17", "17/16", "15/14", "14/13", "12/11", "11/10", "9/8", "8/7",
    "6/5", "5/4", "3/2", "2/1"]
    # 36: Single Number (Straight) 18: Two Numbers (Split) 12: Three Numbers (Street, Trio) 9: Four Numbers (Corner) 7: Five Numbers (Basket in US Roulette)
    #6: Six Numbers (Six Line)	3: Dozens/Columns 2: 18 Numbers 2: ‘Even’ Odds 

    guess_l = []
    bet_l = []
    times = []
    type_ = []

    while True:

        print("""A. ‘Straight Up’(one specific number) B. ‘Split’(one of two specific numbers)
C. ‘Street’(one of three specific numbers) D. ‘Corner’(one of four specific numbers)
E. ‘First Four’(one of numbers 0,1,2,3) F.‘Six Line’(one of six specific numbers)
G. ‘Column’ (one of twelve specific numbers in a row) H. ‘Dozen’ (one of twelve specific numbers in a block)
J. ‘Red or Black’ (one of eighteen specific numbers) K. ‘Odd or Even’ (one of eighteen specific numbers)
L. ‘Low or High’ (one of eighteen specific numbers) M. ‘Split Columns’(one of 24 specific numbers in a row)
N. ‘Split Dozens’(one of 24 specific numbers in a block)
 _____________________________________________________________
| 0 |r3 |b6 |r9 |r12||b15|r18|r21|b24||r27|r30|b33|r36| row1  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|---|b2 |r5 |b8 |b11||r14|b17|b20|r23||b26|b29|r32|b35| row2  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|   |r1 |b4 |r7 |b10||b13|r16|r19|b22||r25|b28|b31|r34| row3  |
 ---|---------------||---------------||---------------|-------
    |    1st  12    ||    2nd  12    ||    3rd  12    |
     -------------------------------------------------""")
        bet_not_int = False

        letter = input('Balance = ${}\n"place" to place bets\n"current" to see current bets\nType of bet '.format(money))
        
        if letter.lower() == "place":
            break

        elif letter.lower() == "current":
            if True:
                skip = False
                for i in range(len(guess_l)):
                    if type_[i] == "split":
                        try:
                           if skip == False:
                               skip = True
                           else:
                               skip = False
                               continue
                        except:
                            pika = True

                        if guess_l[i] == "0" or guess_l[i] == "00":
                            if guess_l[i+1] == "0" or guess_l[i+1] == "00":
                                print("\n{}: ${} split on {} and {}".format(i+1, bet_l[i], guess_l[i], guess_l[i+1]))
                                time.sleep(.5)
                            else:
                                print("\n{}: ${} split on {} and {} {}".format(i+1, bet_l[i], guess_l[i], color[int(guess_l[i+1])], guess_l[i+1]))
                                time.sleep(.5)

                        else:
                            if guess_l[i+1] == "0" or guess_l[i+1] == "00":
                                print("\n{}: ${} split on {} {} and {}".format(i+1, bet_l[i], color[int(guess_l[i])], guess_l[i], guess_l[i+1]))
                                time.sleep(.5)
                            else:
                                print("\n{}: ${} split on {} {} and {} {}".format(i+1, bet_l[i], color[int(guess_l[i])], guess_l[i], color[int(guess_l[i+1])], guess_l[i+1]))
                                time.sleep(.5)

                    else:    
                        if guess_l[i] == "0" or guess_l[i] == "00":
                            print("\n{}: ${} on {}".format(i+1, bet_l[i], guess_l[i]))
                            time.sleep(.5)

                        elif guess_l[i] in number:
                            print("\n{}: ${} on {} {}".format(i+1, bet_l[i], color[int(guess_l[i])], guess_l[i]))
                            time.sleep(.5)
                        else:
                            print("\n{}: ${} on {}".format(i+1, bet_l[i], guess_l[i]))
                            time.sleep(.5)
                if len(guess_l) > 0:
                    okay = input("back: ")
                    continue
                else:
                    print("\nMust have bets placed to see current bets")
                    time.sleep(2)
            
        elif letter.lower() == "a":
            print(""" _____________________________________________________________
| 0 |r3 |b6 |r9 |r12||b15|r18|r21|b24||r27|r30|b33|r36| row1  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|---|b2 |r5 |b8 |b11||r14|b17|b20|r23||b26|b29|r32|b35| row2  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|   |r1 |b4 |r7 |b10||b13|r16|r19|b22||r25|b28|b31|r34| row3  |
 ---|---------------||---------------||---------------|-------
    |    1st  12    ||    2nd  12    ||    3rd  12    |
     -------------------------------------------------\nBalance = ${}""".format(money))
            guess = (input("\n‘Straight Up’(one specific number): ").lower())

            if guess in number:
                
                bet = (input("\nBet amount (min $1): $"))

                try:
                  bet = int(bet)
                except ValueError:
                    bet_not_int = True
                    print("\nThe bet is not a number")
                    time.sleep(3)
                    continue

                if bet_not_int == False:
                    if money < bet:
                        print("\nYou do not have enough money. Bet was {}, Balance is {}".format(bet, money))
                        time.sleep(3)
                        continue

                    elif bet < 1:
                        print("\Minimum $2")
                        time.sleep(3)
                        continue
                
                guess_l.append(guess)
                bet_l.append(bet)
                times.append(18)
                type_.append("single")

                money -= bet
                roulette_profit -= bet

            else:
                print("Guess is not a possible answer. 1-36, 0 and 00")
                time.sleep(2)

        elif letter.lower() == "b":
            print(""" _____________________________________________________________
| 0 |r3 |b6 |r9 |r12||b15|r18|r21|b24||r27|r30|b33|r36| row1  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|---|b2 |r5 |b8 |b11||r14|b17|b20|r23||b26|b29|r32|b35| row2  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|   |r1 |b4 |r7 |b10||b13|r16|r19|b22||r25|b28|b31|r34| row3  |
 ---|---------------||---------------||---------------|-------
    |    1st  12    ||    2nd  12    ||    3rd  12    |
     -------------------------------------------------\nBalance = ${}""".format(money))

            guess = (input("\n‘Two Numbers' (Split)\n_________\n|r3 |b6 |\n --- ---\nformat like  3/6: ").lower())
            if True:
                if guess in split_two:

                    bet = (input("\nBet amount (min $2): $"))


                    try:
                        bet = int(bet)
                    except ValueError:
                        bet_not_int = True
                        print("\nThe bet is not a number")
                        time.sleep(3)
                        continue

                    if bet_not_int == False:
                        if money < bet:
                            print("\nYou do not have enough money. Bet was {}, Balance is {}".format(bet, money))
                            time.sleep(3)
                            continue

                        elif bet < 1:
                            print("\Minimum $1")
                            time.sleep(3)
                            continue
                    
                    split_two_s = guess.split("/")
                    
                    for s in split_two_s:
                        guess_l.append(s)
                        times.append(18)
                        bet_l.append(bet)
                        type_.append("split")
                    
                    print(split_two_s, guess_l, s, bet_l)

                    money -= bet
                    roulette_profit -= bet

                else:
                    print("Guess is not a possible answer. 1-36, 0 and 00")
                    time.sleep(2)
        elif letter.lower() == "c":
            print()
        elif letter.lower() == "d":
            print()
        elif letter.lower() == "e":
            print()
        elif letter.lower() == "f":
            print()
        elif letter.lower() == "g":
            print()
        elif letter.lower() == "h":
            print()
        elif letter.lower() == "j":
            guess = (input("\nred or black: ").lower())

            if guess in color:
                
                bet = (input("\nBet amount (min $1): $"))

                try:
                  bet = int(bet)
                except ValueError:
                    bet_not_int = True
                    print("\nThe bet is not a number")
                    time.sleep(3)
                    continue

                if bet_not_int == False:
                    if money < bet:
                        print("\nYou do not have enough money. Bet was {}, Balance is {}".format(bet, money))
                        time.sleep(3)
                        continue

                    elif bet < 1:
                        print("\Minimum $1")
                        time.sleep(3)
                        continue
                
                guess_l.append(guess)
                bet_l.append(bet)
                times.append(2)

                money -= bet
                roulette_profit -= bet

            else:
                print("Guess is not a possible answer. red or black")
                time.sleep(2)
        elif letter.lower() == "k":
            guess = (input("\nodd or even: ").lower())

            if guess in odd_even:
                
                bet = (input("\nBet amount (min $1): $"))

                try:
                  bet = int(bet)
                except ValueError:
                    bet_not_int = True
                    print("\nThe bet is not a number")
                    time.sleep(3)
                    continue

                if bet_not_int == False:
                    if money < bet:
                        print("\nYou do not have enough money. Bet was {}, Balance is {}".format(bet, money))
                        time.sleep(3)
                        continue

                    elif bet < 1:
                        print("\Minimum $1")
                        time.sleep(3)
                        continue
                
                guess_l.append(guess)
                bet_l.append(bet)
                times.append(2)

                money -= bet
                roulette_profit -= bet

            else:
                print("Guess is not a possible answer. odd or even")
                time.sleep(2)
        elif letter.lower() == "l":
            print()
        elif letter.lower() == "m":
            print()
        elif letter.lower() == "n":
            print()
        else:
            print("Not a possible answer")
            time.sleep(1.5)


    num = random.randint(0, 38)
    chosen_one = []
    
    chosen_one.append(number[num])
    chosen_one.append(color[num])
    chosen_one.append(odd_even[num])
    chosen_one.append(row[num])
    chosen_one.append(_12[num])
    chosen_one.append(_18[num])

    money_profit = 0
    

    print("\nRolling")
    time.sleep(.5)
    print("Rolling.")
    time.sleep(.6)
    print("Rolling..")
    time.sleep(.7)
    print("Rolling...")
    time.sleep(.8)
    print("It landed on {} {}.".format(color[num], number[num]))
    time.sleep(2)
    skip = False
    for i in range(len(guess_l)):
        if type_[i] == "split":
            if skip == False:
                skip = True
            else:
                skip = False
                continue
            if guess_l[i] in chosen_one:
                money_profit += (bet_l[i]* times[i])
                money += (bet_l[i]* times[i]) 
                roulette_profit += (bet_l[i]* times[i])
                roulette_wins += 1
                bet_l_t = bet_l[i] * times[i]

                if guess_l[i] == "0" or guess_l[i] == "00":
                    if guess_l[i+1] == "0" or guess_l[i+1] == "00":
                        print("\nbet was ${}. split between {} and {}\n\nwon {}".format(bet_l[i], guess_l[i], guess_l[i+1], bet_l_t))
                        time.sleep(1)
                    else:
                        print("\nbet was ${}. split between {} and {} {}\n\nwon {}".format(bet_l[i], guess_l[i], color[int(guess_l[i+1])], guess_l[i+1], bet_l_t))
                        time.sleep(1)

                else:
                    if guess_l[i+1] == "0" or guess_l[i+1] == "00":
                        print("\nbet was ${}. split between {} {} and {}\n\nwon {}".format(bet_l[i], color[int(guess_l[i])], guess_l[i], guess_l[i+1], bet_l_t))
                        time.sleep(1)
                    else:
                        print("\nbet was ${}. split between {} {} and {} {}\n\nwon {}".format(bet_l[i], color[int(guess_l[i])], guess_l[i], color[int(guess_l[i+1])], guess_l[i+1], bet_l_t))
                        time.sleep(1)
                
            else:
                money_profit -= bet_l[i]
                roulette_profit -= bet_l[i]
                roulette_losses -= 1
                
                
                if guess_l[i] == "0" or guess_l[i] == "00":
                    if guess_l[i+1] == "0" or guess_l[i+1] == "00":
                        print("\nbet was ${}. split between {} and {}\n\nlost {}".format(bet_l[i], guess_l[i], guess_l[i+1], bet_l[i]))
                        time.sleep(1)
                    else:
                        print("\nbet was ${}. split between {} and {} {}\n\nlost {}".format(bet_l[i], guess_l[i], color[int(guess_l[i+1])], guess_l[i+1], bet_l[i]))
                        time.sleep(1)

                else:
                    if guess_l[i+1] == "0" or guess_l[i+1] == "00":
                        print("\nbet was ${}. split between {} {} and {}\n\nlost {}".format(bet_l[i], color[int(guess_l[i])], guess_l[i], guess_l[i+1], bet_l[i]))
                        time.sleep(1)
                    else:
                        print("\nbet was ${}. split between {} {} and {} {}\n\nlost {}".format(bet_l[i], color[int(guess_l[i])], guess_l[i], color[int(guess_l[i+1])], guess_l[i+1], bet_l[i]))
                        time.sleep(1)

        else:
            if guess_l[i] in chosen_one:
                money_profit += (bet_l[i]* times[i])
                money += (bet_l[i]* times[i]) 
                roulette_profit += (bet_l[i]* times[i])
                roulette_wins += 1
                bet_l_t = bet_l[i] * times[i]
                if guess_l[i] in number:
                    if guess_l[i] == "0" or guess_l[i] == "00":
                        print("\nbet was ${} on {}".format(bet_l[i], guess_l[i]))
                        print("\nwon ${}".format(bet_l_t))
                        time.sleep(1)

                    else:
                        print("\nbet was ${} on {} {}".format(bet_l[i], color[int(guess_l[i])], guess_l[i]))
                        print("\nwon ${}".format(bet_l_t))
                        time.sleep(1)
                else:
                    print("\nbet was ${} on {}".format(bet_l[i], guess_l[i]))
                    print("\nwon ${}".format(bet_l_t))
                    time.sleep(1)
            else:
                money_profit -= bet_l[i]
                roulette_profit -= bet_l[i]
                roulette_losses -= 1
                
                
                if guess_l[i] in number:
                    if guess_l[i] == "0" or guess_l[i] == "00":
                        print("\nbet was ${} on {}".format(bet_l[i], guess_l[i]))
                        print("\nlost ${}".format(bet_l[i]))
                        time.sleep(1)

                    else:
                        print("\nbet was ${} on {} {}".format(bet_l[i], color[int(guess_l[i])], guess_l[i]))
                        print("\nlost ${}".format(bet_l[i]))
                        time.sleep(1)
                else:
                    print("\nbet was ${} on {}".format(bet_l[i], guess_l[i]))
                    print("\nlost ${}".format(bet_l[i]))
                    time.sleep(1)

    if money_profit > 0:
        print("\n profit/loss ${}".format(money_profit))
    
    if money_profit == 0:
        print("\n profit/loss ${}, oh thats anticlimatic lul".format(money_profit))
    else:
        money_profit = str(money_profit)
        money_profit = money_profit.strip("-")
        print("\n profit/loss -${}".format(money_profit))

# Call your game of chance functions here

def choose():
    global money

    while money > 0:
        print()
        game = input("What game do you want to play? input 1:Coin-Flip, 2:Cho-Han, 3:War, 4:Roulette, 5:Withdraw, 6:Rules ")
        print()


        try:
            if int(game) == 1:
                print(coin_flip(input("Coin-Flip      Bet "), input("Coin-Flip      guess ")))
            elif int(game) == 2:
                print(cho_han(input("Cho-Han      Bet "), input("Cho-Han    Guess ")))
            elif int(game) == 3:
                print(war(input("War      Bet ")))
            elif int(game) == 4:
                print(roulette())
            elif int(game) == 5:
                print("You are withdrawing with " + str(money) + ".")

                time.sleep(1)
                money = -1
                print()

                if coin_flip_wins >= 1 and coin_flip_losses >= 1:

                    coin_flip_w_l_ratio = coin_flip_wins / (coin_flip_losses + coin_flip_wins)
                    coin_flip_w_l_ratio = float(coin_flip_w_l_ratio) * 100
                    coin_flip_w_l_ratio = int(coin_flip_w_l_ratio)

                    print("Coin-Flip win/loss ratio: " + str(coin_flip_w_l_ratio) + "%")

                elif coin_flip_wins >= 1 and coin_flip_losses == 0:
                    print("Coin-Flip win/loss ratio: 100%")

                elif coin_flip_losses >= 1 and coin_flip_wins == 0:
                    print("Coin-Flip win/loss ratio: 0%")

                if coin_flip_wins >= 1 and coin_flip_losses >= 1:
                    print("Coin-flip net gain: " + str(coin_flip_profit))
                    print()

                if cho_han_wins >= 1 and cho_han_losses >= 1:

                    cho_han_w_l_ratio = cho_han_wins / (cho_han_losses + cho_han_wins)
                    cho_han_w_l_ratio = float(cho_han_w_l_ratio) * 100
                    cho_han_w_l_ratio = int(cho_han_w_l_ratio)

                    print("Cho-Han win/loss ratio: " + str(cho_han_w_l_ratio) + "%")

                elif cho_han_wins >= 1 and cho_han_losses == 0:
                    print("Cho-Han win/loss ratio: 100%")

                elif cho_han_losses >= 1 and cho_han_wins == 0:
                    print("Cho-Han win/loss ratio: 0%")

                if cho_han_wins >= 1 and cho_han_losses >= 1:
                    print("Cho-Han net gain: " + str(cho_han_profit))
                    print()

                if war_wins >= 1 and war_losses >= 1:

                    war_w_l_ratio = war_wins / (war_losses + war_wins)
                    war_w_l_ratio = float(war_w_l_ratio) * 100
                    war_w_l_ratio = int(war_w_l_ratio)

                    print("War win/loss ratio: " + str(war_w_l_ratio) + "%")

                elif war_wins >= 1 and war_losses == 0:
                    print("War win/loss ratio: 100%")

                elif war_losses >= 1 and war_wins == 0:
                    print("War win/loss ratio: 0%")

                if war_ties >= 1:
                    print("Amount of War ties: " + str(war_ties))

                if war_wins >= 1 and war_losses >= 1:
                    print("War net gain: " + str(war_profit))
                    print()

                if roulette_wins >= 1 and roulette_losses >= 1:

                    roulette_w_l_ratio = roulette_wins / (roulette_losses + roulette_wins)
                    roulette_w_l_ratio = float(roulette_w_l_ratio) * 100
                    roulette_w_l_ratio = int(roulette_w_l_ratio)

                    print("roulette win/loss ratio: " + str(roulette_w_l_ratio) + "%")

                elif roulette_wins >= 1 and roulette_losses == 0:
                    print("roulette win/loss ratio: 100%")

                elif roulette_losses >= 1 and roulette_wins == 0:
                    print("roulette win/loss ratio: 0%")

                if roulette_wins >= 1 and roulette_losses >= 1:
                    print("roulette net gain: " + str(roulette_profit))
                    print()

            elif int(game) == 6:
                rule = input("1:Coin-Flip, 2:Cho-Han, 3:War, 4:Roulette, 5:Back ")

                if int(rule) == 1:
                    print("""During a coin toss, the coin is thrown into the air such that it rotates edge-over-edge
                     several times. Either beforehand or when the coin is in the air, an interested party calls "heads"
                      or "tails", indicating which side of the coin that party is choosing. The other party is assigned
                       the opposite side. Depending on custom, the coin may be caught; caught and inverted; or allowed
                        to land on the ground. When the coin comes to rest, the toss is complete and the party who
                         called correctly or was assigned the upper side is declared the winner.""")
                elif int(rule) == 2:
                    print()
                    print("""Chō-Han Bakuchi or simply Chō-Han (丁半) is a traditional Japanese gambling game using dice.
The game uses two standard six-sided dice, which are shaken in a bamboo cup or bowl by a dealer. The cup is then
 overturned onto the floor. Players then place their wagers on whether the sum total of numbers showing on the two dice
  will be "Chō" (even) or "Han" (odd). The dealer then removes the cup, displaying the dice. The winners collect their
   money.""")
                elif int(rule) == 3:
                    print("""Cards are ranked as in poker, except aces are always high. The suit does not matter.
After the players have made a wager each player and the dealer shall get one card. Each player's card shall be compared
 with the dealer's card. If the player's card is higher he wins even money. If the dealer's card is higher the player
  loses.""")
                elif int(rule) == 4:
                    print("""Roulette is a casino game named after the French word meaning little wheel. In the game, 
players may choose to place bets on either a single number, various groupings of numbers, the colors red or
black, whether the number is odd or even, or if the numbers are high (19–36) or low (1–18).
To determine the winning number and color, a croupier spins a wheel in one direction, then spins a ball in the opposite
direction around a tilted circular track running around the outer edge of the wheel. The ball eventually loses
momentum, passes through an area of deflectors, and falls onto the wheel and into one of or 38 colored and numbered
pockets on the wheel. The winnings are then paid to anyone who has placed a successful bet.

A. ‘Straight Up’ (one specific number) 35 to 1 
B. ‘Split’ (one of two specific numbers) 17 to 1
C. ‘Street’(one of three specific numbers) 11 to 1
D. ‘Corner’ (one of four specific numbers) 8 to 1 
E. ‘First Four’ (one of numbers 0,1,2,3) 8 to 1 
F. ‘Six Line’(one of six specific numbers) 5 to 1
G. ‘Column’ (one of twelve specific numbers in a row) 2 to 1 
H. ‘Dozen’(one of twelve specific numbers in a block) 2 to 1
J. ‘Red or Black’ (one of eighteen specific numbers) 1 to 1
K. ‘Odd or Even’ (one of eighteen specific numbers) 1 to 1
L. ‘Low or High’ (one of eighteen specific numbers) 1 to 1
M. ‘Split Columns’ (one of 24 specific numbers in a row) 1 to 2
N. ‘Split Dozens’ (one of 24 specific numbers in a block) 1 to 2 
 _____________________________________________________________
| 0 |r3 |b6 |r9 |r12||b15|r18|r21|b24||r27|r30|b33|r36| row1  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|---|b2 |r5 |b8 |b11||r14|b17|b20|r23||b26|b29|r32|b35| row2  |
| 0 |---|---|---|---||---|---|---|---||---|---|---|---|       |
|   |r1 |b4 |r7 |b10||b13|r16|r19|b22||r25|b28|b31|r34| row3  |
 ---|---------------||---------------||---------------|-------
    |    1st  12    ||    2nd  12    ||    3rd  12    |
     -------------------------------------------------""")
                elif int(rule) == 5:
                    choose()


        except:
            if money > 0:
                print("Wrong input")
                choose()
    if money == 0:
        print("You are out of money.")
        time.sleep(1)
        print()

        if coin_flip_wins >= 1 and coin_flip_losses >= 1:

            coin_flip_w_l_ratio = coin_flip_wins / (coin_flip_losses + coin_flip_wins)
            coin_flip_w_l_ratio = float(coin_flip_w_l_ratio) * 100
            coin_flip_w_l_ratio = int(coin_flip_w_l_ratio)

            print("Coin-Flip win/loss ratio: " + str(coin_flip_w_l_ratio) + "%")

        elif coin_flip_wins >= 1 and coin_flip_losses == 0:
            print("Coin-Flip win/loss ratio: 100%")

        elif coin_flip_losses >= 1 and coin_flip_wins == 0:
            print("Coin-Flip win/loss ratio: 0%")

        if coin_flip_wins >= 1 or coin_flip_losses >= 1:
            print("Coin-flip net gain: " + str(coin_flip_profit))
            print()


        if cho_han_wins >= 1 and cho_han_losses >= 1:

            cho_han_w_l_ratio = cho_han_wins / (cho_han_losses + cho_han_wins)
            cho_han_w_l_ratio = float(cho_han_w_l_ratio) * 100
            cho_han_w_l_ratio = int(cho_han_w_l_ratio)

            print("Cho-Han win/loss ratio: " + str(cho_han_w_l_ratio) + "%")

        elif cho_han_wins >= 1 and cho_han_losses == 0:
            print("Cho-Han win/loss ratio: 100%")

        elif cho_han_losses >= 1 and cho_han_wins == 0:
            print("Cho-Han win/loss ratio: 0%")

        if cho_han_wins >= 1 or cho_han_losses >= 1:
            print("Cho-Han net gain: " + str(cho_han_profit))
            print()


        if war_wins >= 1 and war_losses >= 1:

            war_w_l_ratio = war_wins / (war_losses + war_wins)
            war_w_l_ratio = float(war_w_l_ratio) * 100
            war_w_l_ratio = int(war_w_l_ratio)

            print("War win/loss ratio: " + str(war_w_l_ratio) + "%")

        elif war_wins >= 1 and war_losses == 0:
            print("War win/loss ratio: 100%")

        elif war_losses >= 1 and war_wins == 0:
            print("War win/loss ratio: 0%")

        if war_ties >= 1:
            print("Amount of War ties: " + str(war_ties))

        if war_wins >= 1 or war_losses >= 1:
            print("War net gain: " + str(war_profit))
            print()


        if roulette_wins >= 1 and roulette_losses >= 1:

            roulette_w_l_ratio = roulette_wins / (roulette_losses + roulette_wins)
            roulette_w_l_ratio = float(roulette_w_l_ratio) * 100
            roulette_w_l_ratio = int(roulette_w_l_ratio)

            print("roulette win/loss ratio: " + str(roulette_w_l_ratio) + "%")

        elif roulette_wins >= 1 and roulette_losses == 0:
            print("roulette win/loss ratio: 100%")

        elif roulette_losses >= 1 and roulette_wins == 0:
            print("roulette win/loss ratio: 0%")

        if roulette_wins >= 1 or roulette_losses >= 1:
            print("roulette net gain: " + str(roulette_profit))
            print()
#choose()
roulette()

