#Garrett Boehmer
#this program attempts to create a random number and have the user guess it


#function that rounds up the amount of tries it took and the best tries ever done and it tells you what the random number was.
def completion(ran, count, count_ulti):
    if (ran % 2) == 0:
        print(" ")
        print("*************************************************************") 
        print("You did it,", f'the number was {ran} which is an even number') 
        print('It took you', f"{count}", 'tries to do. Your best is', f'{count_ulti}', 'tries')
        print("*************************************************************")
        print(" ")
    else:
        print(" ")
        print("*************************************************************") 
        print("You did it,", f'the number was {ran} which is an odd number') 
        print('It took you', f"{count}", 'tries to do. Your best is', f'{count_ulti}', 'tries')
        print("*************************************************************")
        print(" ")

#function used to generate the random number
def random_number(LOWER_LIMIT,UPPER_LIMIT):
    import random
    ran = random.randint(LOWER_LIMIT,UPPER_LIMIT)
    return ran

def play_game(EXIT, guess, ran, count, count_ulti):
    while guess != EXIT and guess != ran:
        guess = int(input("Pick a number between 1 and 100: "))
        count += 1
        if guess == ran:
            #checking to see if we have a new best score
            if count_ulti > count:
                count_ulti = count
            else:
                count_ulti = count_ulti
            # completion message once they guess the correct number
            completion(ran, count, count_ulti)
        elif guess > ran and guess != EXIT:
            print('the number to guess is lower')
        elif guess < ran:
            print("the number to guess is higher")
    return count_ulti, count

#I needed a way to "save" the information stored and unfortunetely making abunch of varibles, testing them and then spitting them back out was the only solution i am aware of.
#If i could make some kind of "shift register" with multiple functions i would but i dont know how to go about that.
#This function takes in the current count and compares it with top scores for a leaderboard feature. if the count is greater than all top 5 scores then it will just display the
#leaderboard
#This leaderboard actaully works properly it stores the top 5 scores
#EX. if all 5 slots are filled up but then someone gets a 3rd place finish 4th place shifts to 5th and 5th gets pushed off the leaderboard
#It also asks you for your name and the name is stored along with your score!
def leaderboard(top_1, top_2, top_3, top_4, top_5, count, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name):
    if count < top_1 or count == top_1:
        top_5 = top_4
        top_4 = top_3
        top_3 = top_2
        top_2 = top_1
        top_1 = count
        top_5_name = top_4_name
        top_4_name = top_3_name
        top_3_name = top_2_name
        top_2_name = top_1_name
        top_1_name = input("enter your name for first place ")
    elif count< top_2 or count== top_2:
        top_5 = top_4
        top_4 = top_3
        top_3 = top_2
        top_2 = count
        top_1 = top_1
        top_5_name = top_4_name
        top_4_name = top_3_name
        top_3_name = top_2_name
        top_2_name = input("enter your name for second place ")
        top_1_name = top_1_name
    elif count < top_3 or count == top_3:
        top_5 = top_4
        top_4 = top_3
        top_3 = count
        top_2 = top_2
        top_1 = top_1
        top_5_name = top_4_name
        top_4_name = top_3_name
        top_3_name = input("enter your name for third place ")
        top_2_name = top_2_name
        top_1_name = top_1_name
    elif count < top_4 or count == top_4:
        top_5 = top_4
        top_4 = count
        top_3 = top_3
        top_2 = top_2
        top_1 = top_1
        top_5_name = top_4_name
        top_4_name = input("enter your name for fourth place ")
        top_3_name = top_3_name
        top_2_name = top_2_name
        top_1_name = top_1_name
    elif count < top_5 or count == top_5:
        top_5 = count
        top_4 = top_4
        top_3 = top_3
        top_2 = top_2
        top_1 = top_1
        top_5_name = input("enter your name for fifth palce ")
        top_4_name = top_4_name
        top_3_name = top_3_name
        top_2_name = top_2_name
        top_1_name = top_1_name
    print('  ')
    #this is where the leader board is displayed out
    #lined up the titles along with the name and scores!
    print('Leaderboard\t\t\tName:\t\t\tScore:')
    print(f'The top scorer is \t\t{top_1_name}\t\t\t{top_1}')

    print(f'In second place is \t\t{top_2_name}\t\t\t{top_2}')

    print(f'In third place is \t\t{top_3_name}\t\t\t{top_3}')

    print(f'In fourth place is \t\t{top_4_name}\t\t\t{top_4}')

    print(f'In fifth place we have \t\t{top_5_name}\t\t\t{top_5}')
    print('  ')

    return top_1, top_2, top_3, top_4, top_5, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name

def main():
    #top score varialbes that start at 1000 at the guarentee to catch the first 5 scores
    top_1 = 1000
    top_2 = 1000
    top_3 = 1000
    top_4 = 1000
    top_5 = 1000
    #top score names that that set to N/A until they are overridden 
    top_1_name = 'N/A '
    top_2_name = 'N/A '
    top_3_name = "N/A "
    top_4_name = "N/A "
    top_5_name = "N/A "
#random number
    ran = 0
#user input to guess the random number
    guess = 0
#user input to either play or exit
    choice = " "
#variable to count how many tries it took to reach the random number
    count = 0
#string varible for the Players choice to either play or leave the game
    YES = 'Play'
    NO = 'EXIT'
#this is the best count it took to guess the number correctly i set it to 5000 in hopes that it doesnt take 5000 tries to guess a number between 1-100
#also its put to 5000 so that when the user guesses the number the first time its guarenteed to save the best count, unless it takes them more than 5000 guesses.
    count_ulti = 5000
#lower limit for the random number
    LOWER_LIMIT = 1
#upper limit for the random number
    UPPER_LIMIT = 100
#varible used to reset the counter
    ZERO = 0
#varible to go back while to previous options while in game
    EXIT = 101
    #user input that is needed to enter the leaderboard
    lead = 'Leaderboard'
    #we need this for only if the player decides to look at the leaderboard instead of playing then going reaching the leaderboard. or else a score of '0' would be entered
    VARIABLE_TO_NOT_ENTER_A_SCORE_TO_SEE_LEADERBOARD = 100000000000000000000000000
#welcoming message pops up only once
    input("Welcome to the Guessing Game press enter to play ")

    while choice != NO:
        ran = random_number(LOWER_LIMIT, UPPER_LIMIT)
        print("Enter 'Play' to play and 'Exit' to exit: ")
        choice = input('Or Enter Leaderboard to see the highscores!: ')
        #resets count back to zero each loop
        count = ZERO
        if choice == YES:
                count_ulti, count = play_game(EXIT, guess, ran, count, count_ulti)
                top_1, top_2, top_3, top_4, top_5, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name = leaderboard(top_1, top_2, top_3, top_4, top_5, count, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name)
        #this is where the game is skipped to if the player wants to look at the leaderboard. i put in varible to not enter... for count so that when leader board is opened there isnt a chance 
        #that a score would be entered
        elif choice == lead:   
            leaderboard(top_1, top_2, top_3, top_4, top_5, VARIABLE_TO_NOT_ENTER_A_SCORE_TO_SEE_LEADERBOARD, top_1_name, top_2_name, top_3_name, top_4_name, top_5_name)
        elif choice == NO:
            print("Ok have a nice day! ")

main()