#Garrett Boehmer
#Nested dictionaries from the internet
#This program hopes to take a request from a user and give back a list of suggestions based on the input

import urllib.request 
import urllib 
import json 

def get_data(item): 
        payload={'q':item} 
        item=urllib.parse.urlencode(payload) 
        api_url = "https://tastedive.com/api/similar?" + item 
        page=urllib.request.Request(api_url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile=urllib.request.urlopen(page).read() 
        decoded = infile.decode('utf8') 
        the_dictionary = json.loads(decoded) 
        return the_dictionary

def main():
    print('Welcome to Find Me Something.. powered bt TasteDive!')
    #controller for the loop
    request = True
    #setting the user input to something thats not a space so it hits the first boolean
    item = 'not space'
    #dictionary where i am putting the results of what comes back from the get_data function
    results = {}
    #easy string varible that stores the type of input that comes back from the get_data
    type_of_input = ' '
    #simple list that will be using the append method and then reset at the top of the loop once it loops back around
    results_list = []
    #place holder that indicates the index within the info dictionary 
    TYPE_INDEX = 0
    #input value that the user gives to us to limit the amount of searches depending on what the user gives
    user_amount_search = 0
    #constant for if the user input results in something the get_data doesnt recognize
    NOT_FOUND = 'unknown'
    #constants for the keys used in return dictionary from get_data
    SIMILAR_KEY = 'Similar'
    INFO_KEY = 'Info'
    TYPE_KEY = 'Type'
    RESULTS_KEY = 'Results'
    NAME_KEY = 'Name'
    while request:
        try:
            item = input('please enter something to search or hit enter to exit: ')
            user_dictionary = get_data(item)
            #getting the typ of input
            type_of_input = user_dictionary[SIMILAR_KEY][INFO_KEY][TYPE_INDEX][TYPE_KEY]
            if type_of_input != NOT_FOUND and item != "":
                user_amount_search = input('\nEnter the number of searches you would like or hit "ENTER" for no filter:')
                print(' ')
                if user_amount_search != '':
                    user_amount_search = int(user_amount_search)
                #resetting the list incase the user wants to do another search
                results_list = []
                #printing it out
                print(f'The type of entry you asked about is: {type_of_input}\n')
                #retrieving the result list
                results = user_dictionary[SIMILAR_KEY][RESULTS_KEY]
                #printing out the recommended list
                for num in range(0, len(results)):
                    results_list.append(results[num][NAME_KEY])
                #telling the user how many results i found
                print(f'I found {len(results_list)} results from your input')
                if user_amount_search != '':
                    for num in range(0,user_amount_search):
                        print(f'{num+1}.\t{results_list[num]}')
                elif user_amount_search == '':
                    for num in range(0,len(results_list)):
                        print(f'{num+1}.\t{results_list[num]}')
            elif item == '':
                request = False
                print('Ok have a nice day!')
            #sees if the users entry was found or not
            elif type_of_input == NOT_FOUND:
                print('We do not recognize your input please check your entry and try again.')
        except IndexError:
            print('the amount of searches you wanted exceeded the total amount actaully gathered')

main()