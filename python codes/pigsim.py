#Garrett Boehmer
#Python Pig sim
#This program takes two computers and makes them play pig
import random

#this function is called by both the player and the computer to select a random number form 1-6 and return that random number
def die_roll():
    LOWER_LIMIT = 1
    UPPER_LIMIT = 6
    roll  = random.randint(LOWER_LIMIT,UPPER_LIMIT)
    return roll

#This is the computers turn. it rolls until it stops at the designated value
def computer1_turn_score(end):
    total_score = 0
    END = 1
    NO_SCORE = 0
    while total_score <= end:
        roll = die_roll()
        if roll != END:
            total_score += roll
        elif roll == END:
            total_score = NO_SCORE
            return total_score
    return total_score

#This is the computers turn. it rolls until it stops at the designated value
def computer2_turn_score(end):
    total_score = 0
    END = 1
    NO_SCORE = 0
    while total_score <= end:
        roll = die_roll()
        if roll != END:
            total_score += roll
        elif roll == END:
            total_score = NO_SCORE
            return total_score
    return total_score

#this function checks after the play and the omputer have done thier turns to see i there is a winner yet
def check_for_win(comp1, comp2):
    MAX_SCORE = 100
    if comp1 >= MAX_SCORE:
        return False
    elif comp2 >= MAX_SCORE:
        return False
    else:
        return True

#this function starts after each game and tallie up the wins and returns the values
def add_up_the_wins(comp1_score, comp2_score,comp1_win,comp2_win):
    PLUS_WIN = 1
    MAX_SCORE = 100
    if comp1_score>= MAX_SCORE:
        comp1_win += PLUS_WIN
    elif comp2_score >= MAX_SCORE:
        comp2_win += PLUS_WIN
    return comp1_win, comp2_win

def main():
    #controls the inner loop
    win = True
    #keeping a running total of when the computer either rolls a 1 or stop rolling
    comp1_score = 0
    comp2_score = 0
    #keeps track of the wins each computer has
    comp2_win = 0
    comp1_win = 0
    #running total that stops the first loop after a certain amount of games have been played
    wins = 0
    #This is how many games are being played in one run of the sim
    AMOUNT_OF_SIMS = 1000
    #this is where the computers stop rolling on each of thier turn
    comp1_end = 23
    comp2_end = 20
    MAX_SCORE = 100
    END_GAME = 1
    while wins != AMOUNT_OF_SIMS:
        #resetting the values that control the inner loop
        comp1_score = 0
        comp2_score = 0
        win = True
        while win:
            comp1_score += computer1_turn_score(comp1_end)
            if comp1_score < MAX_SCORE:
                comp2_score += computer2_turn_score(comp2_end)
            win = check_for_win(comp1_score, comp2_score)
        comp1_win, comp2_win = add_up_the_wins(comp1_score, comp2_score, comp1_win, comp2_win)
        wins +=END_GAME
    print(f'Computer 1 [{comp1_end}] total wins: {comp1_win} times')
    print(f'Computer 2 [{comp2_end}] total win: {comp2_win} times')

main()