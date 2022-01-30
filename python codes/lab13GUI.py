#Garrett Boehmer
#API
#This program takes in a user input and from that lists a certain amount of suggestions.

import tkinter
import tkinter.font
import urllib.request 
import urllib 
import json
main_window = tkinter.Tk()
main_window.title('Garrett Boehmer lab 13')
def search (entry,output,number,type,found):
    try:
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
        item = entry.get()
        output.delete(0, 'end')
        payload={'q':item}
        item=urllib.parse.urlencode(payload)
        api_url = "https://tastedive.com/api/similar?" + item 
        page=urllib.request.Request(api_url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile=urllib.request.urlopen(page).read()
        decoded = infile.decode('utf8')
        the_dictionary = json.loads(decoded)
        user_dictionary = the_dictionary
        #getting the type of input
        type_of_input = user_dictionary[SIMILAR_KEY][INFO_KEY][TYPE_INDEX][TYPE_KEY]
        if type_of_input != NOT_FOUND and item != "":
            user_amount_search = number.get()
            if user_amount_search != '':
                user_amount_search = int(user_amount_search)
            #resetting the list incase the user wants to do another search
            results_list = []
            #printing it out
            print(f'The type of entry you asked about is: {type_of_input}\n')
            type.set(type_of_input)
            #retrieving the result list
            results = user_dictionary[SIMILAR_KEY][RESULTS_KEY]
            #printing out the recommended list
            for num in range(0, len(results)):
                results_list.append(results[num][NAME_KEY])
            #telling the user how many results i found
            print(f'I found {len(results_list)} results from your input')
            found.set(len(results_list))
            if user_amount_search != '':
                for num in range(0,user_amount_search):
                    print(f'{num+1}.\t{results_list[num]}')
                    output.insert(0, f'{results_list[num]}')
            elif user_amount_search == '':
                for num in range(0,len(results_list)):
                    print(f'{num+1}.\t{results_list[num]}')
                    output.insert(0, f'{results_list[num]}')
        elif item == '':
            print('Ok have a nice day!')
        #sees if the users entry was found or not
        elif type_of_input == NOT_FOUND:
            print('We do not recognize your input please check your entry and try again.')
            output.insert(0, 'We do not recognize your input please check your entry and try again.')
    except IndexError:
        print('Asked amount of searches exceeded total search')

def main():

    #left big frame frames
    Left_big_frame = tkinter.LabelFrame(main_window, text='User inputs', bg = 'white',borderwidth=3, relief='groove')
    Left_big_frame.pack(side = 'left')
    top_frame_in_left = tkinter.Frame(Left_big_frame)
    top_frame_in_left.pack(side = 'top')
    mid_frame_in_left = tkinter.Frame(Left_big_frame)
    mid_frame_in_left.pack(side = 'top')
    bottom_frame_in_left = tkinter.Frame(Left_big_frame)
    bottom_frame_in_left.pack(side = 'top')

    #right big frames
    right_big_frame = tkinter.LabelFrame(main_window, text='OUTPUT', bg = 'white',borderwidth=3, relief='groove')
    right_big_frame.pack(side = 'left')
    top_frame_in_right = tkinter.Frame(right_big_frame)
    top_frame_in_right.pack(side = 'top')
    mid_frame_in_right = tkinter.Frame(right_big_frame)
    mid_frame_in_right.pack(side = 'top')
    bottom_frame_in_right = tkinter.Frame(right_big_frame)
    bottom_frame_in_right.pack(side = 'top')

    #listbox
    listbox  = tkinter.Listbox(right_big_frame, width=65,bg = 'white')
    listbox.pack(side = 'top')

    #top frame in left
    search_label = tkinter.Label(top_frame_in_left, bg='white',text = 'Enter what you would like to search: ',font=('Helvetica bold',15))
    search_label.pack(side = 'left')
    search_entry = tkinter.Entry(top_frame_in_left, bg='white',width = 10, font=('Helvetica bold',15))
    search_entry.pack(side = 'left')

    #mid frame in left
    search_label_number = tkinter.Label(mid_frame_in_left, bg='white',text = 'Enter the amount of searchs you want out of 20: ',font=('Helvetica bold',15))
    search_label_number.pack(side = 'left')
    search_entry_number = tkinter.Entry(mid_frame_in_left, bg='white',width = 10, font=('Helvetica bold',15))
    search_entry_number.pack(side = 'left')

    #buttons - its in bottom frame in left
    search_button = tkinter.Button(bottom_frame_in_left, text = 'Search', bg= 'green',font=('Helvetica bold',15), command = lambda: search(search_entry, listbox, search_entry_number, type_value, found_value))
    search_button.pack(side = 'top')

    #top frame in right
    type_label= tkinter.Label(top_frame_in_right, bg='white',text = 'Type of input: ',font=('Helvetica bold',15))
    type_label.pack(side = 'left')
    type_value = tkinter.StringVar()
    type_value_label = tkinter.Label(top_frame_in_right,textvariable=type_value,font=('Helvetica bold',15))
    type_value_label.pack( side = 'left')

    #mid frame in right
    found_label= tkinter.Label(mid_frame_in_right, bg='white',text = 'Amount of searches found: ',font=('Helvetica bold',15))
    found_label.pack(side = 'left')
    found_value = tkinter.StringVar()
    found_value_label = tkinter.Label(mid_frame_in_right,textvariable=found_value,font=('Helvetica bold',15))
    found_value_label.pack( side = 'left')

    tkinter.mainloop()

main()