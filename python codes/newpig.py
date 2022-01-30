#Garrett Boehmer
#Python Pig
#this prorgam pits a human against a computer in the game of pig which is a dice game


import random

#this function is called by both the player and the computer to select a random number form 1-6 and return that random number
def die_roll():
    LOWER_LIMIT = 1
    UPPER_LIMIT = 6
    roll  = random.randint(LOWER_LIMIT,UPPER_LIMIT)
    return roll
#this function just aks the user if they want to continue or not and return thats choice.
def roll_or_end():
    choice = int(input('Enter 1 to roll or enter a 2 to end your turn: '))
    print(' ')
    return choice

#this is the players turn it gives the palyer multiple options on what they might want to do. 
#it asks through number inputs if they want to stop rolling or roll again.
def user_turn_score():
    total_score = 0
    choice = 1
    quit = ' '
    print(f"Your turn!!\n")
    while choice != quit:
                                            #getting the roll and the players choice
        roll = die_roll()
        choice = roll_or_end()
        if choice == 1 and roll != 1:
            total_score += roll
            print(f'Your roll was a: {roll}\nCurret score for this turn: {total_score}\n')
        elif roll == 1 and choice != 2:
            total_score = 0
            print('****************************************************')
            print('Whoops you rolled a 1 you get 0 points this round')
            print('****************************************************')
            return total_score
        elif choice == 2:
            return total_score
    return total_score

#This is the computers turn. it builds up a dictionary each round and the dictionary is written over every turn.
#during the computers turn it stops at the point the user chose as per the difficulty.
#if the computer rolls a 1 the turn is over and the score is set to 0
def computer_turn_score(stop):
    COMPUTER_END_TURN_SCORE = stop
    total_score = 0
    comp_dic = {}
    count = 0
    while total_score <= COMPUTER_END_TURN_SCORE:
        count += 1
        roll = die_roll()
        if roll != 1:
                                                #adding the roll to the total score and then adding it to the dictionary
            total_score += roll
            comp_dic[count] = roll
        elif roll == 1:
            total_score = 0
            comp_dic[count] = roll
                                                #sending the dictionary and the total score off to be printed
            print_out_computers_rolls(comp_dic, total_score)
            return total_score
                                                #sending the dictionary and the total score off to be printed
    print_out_computers_rolls(comp_dic, total_score)
    return total_score

#This function takes in the total score and the dictionary build while the computer rolled and spits it out for the user to see how many times it took for the computer to 
#get where it got.
#it also display the computers score for that round.
def print_out_computers_rolls(comp_dic, total_score):
    print('The computers rolls were: ')
    count = 0
                                                #this goes through each key and displays each value
    for key in comp_dic:
        count += 1
        print(f'{count}.\t{comp_dic[key]}')
    print(f'For a total score of {total_score}\n')

#this function checks after the play and the omputer have done thier turns to see i there is a winner yet
def check_for_win(player, computer):
    if player >= 100:
        print('**********************************')
        print('Player won\n**********************************')
        return False
    elif computer >= 100:
        print('**********************************')
        print('Computer won\n**********************************')
        return False
    else:
        return True
def big_window():
    for key in dic:
        comp_list = 
    print('**************************')


#this function takes in the user input for difficutly and uses it to determine which number the computer stops rolling at and returns that value
def comp_level(difficulty):
    stop = 0
    if difficulty == 1:
        stop = 5
    elif difficulty == 2:
        stop = 15
    elif difficulty == 3:
        stop = 23
    return stop

def main():
    #controls the inside loop that checks if a play has won yet
    win = True
    #the players score thats a running total
    player_score = 0
    #computers score thats a running total
    comp_score = 0
    #choice thats a string that asks the play if they want to play or not
    choice = ' '
    #this is the return varible fom the difficulty level
    stop = 0
    #running total that is the returned value from computers turn
    total_comp_score = 0
    #user input for choosiong what difficulty they would liek to play on
    difficulty = 0
    #controls the outside loop that asks if the user wants to play again
    again = True
    #user input that asks the user if they want to play again
    ask_again = ' '

    print('*****************************************************************')
    print('Welcome to Python Pig!\n*****************************************************************')

    while choice != 'play' and choice != 'quit':
        try:
            choice = str(input('Please enter any of the options\n1.Enter play to play\t2.Enter quit to leave the game:\n'))
        except ValueError:
            print('Please enter one of the options')
    if choice == 'quit':
        again = False
    print(' ')
    #outside loop that allows the player to play again
    while again:
        #inside loop 'game loop'
        while win and choice!='quit':
            #choosing difficulty
            while difficulty != 1 and difficulty != 2 and difficulty != 3:
                try:
                    difficulty = int(input('Please enter from 1-3 for level of difficulty:\n1. Steve \t= \tEASY\n2. Garrett \t= \tMedium\n3. Ryan \t= \tHard: '))
                except ValueError:
                    print('Please enter an integer')
                stop = comp_level(difficulty)

            player_score += user_turn_score()
            if player_score < 100:
                comp_score = computer_turn_score(stop)
                total_comp_score += comp_score
            win = check_for_win(player_score, total_comp_score)
            print(f'Current totals:\nPlayer score: {player_score}\nComputer score: {total_comp_score}\n')
        #asking the player if they want to play again
        ask_again = input("Enter yes or no if you would like to play again\n")
        if ask_again == 'yes' or ask_again == 'Yes':
            again = True
            win = True
            player_score = 0
            total_comp_score = 0
            difficulty = 0
        elif ask_again == 'no' or ask_again == 'No':
            again = False
            win = False
            choice = 'quit'
    print('Thank you for playing\nHave a good day')
main()