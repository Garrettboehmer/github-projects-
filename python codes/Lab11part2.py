#Garrett Boehmer
#Miles Per Gallon Caluculator
#GUI program that asks the user for two inputs for number of miles and amount of gallons and it tells the user how many miles they are estimated to go.

import tkinter
import tkinter.font

def calculate():
    #the answer that is going to put in after the calculation
    miles_per_gallon = 0.0
    #user input retrieved from the gallons frame
    gallon_num = 0.0
    #user input retrieves from the miles frame
    miles_num = 0.0

    #past_entries = {}
    try:
        if float(gallons_entry.get()) > 0 and float(miles_entry.get()) > 0:
            gallon_num = float(gallons_entry.get())
            miles_num = float(miles_entry.get())
            miles_per_gallon = float(miles_num/ gallon_num)
            value.set(f'{miles_per_gallon:,.2f} Miles Per Gallon')
            #past_entries[gallons_entry.get()] = [miles_entry.get()]
            listbox.insert(0, f'{miles_entry.get()} miles / {gallons_entry.get()} gallons  = {value.get()}')
            #for keys in past_entries:
                #for values in past_entries[keys]:
                    #listbox.insert(0,f'{keys} gallons, {values}miles = {value.get()}')

        else:
            value.set('Please enter a number greater than zero')
    except ValueError:
        value.set('Please enter a number in both fields')

def reset():
    miles_entry.delete(0, 'end')
    gallons_entry.delete(0, 'end')
    value.set(' ')

WIDTH = 25
HEIGHT = 25
main_window = tkinter.Tk()

main_window.title('Garrett Boehmers Miles Per Gallon')
canvas = tkinter.Canvas(main_window, width = WIDTH, height = HEIGHT)

#frames
big_frame = tkinter.Frame(main_window)
right_big_frame = tkinter.Frame(main_window)
top_frame = tkinter.LabelFrame(big_frame, text='User inputs', bg = 'white',borderwidth=3, relief='groove')
gallon_frame = tkinter.Frame(top_frame,bg='white')
miles_frame = tkinter.Frame(top_frame,bg='white')
bottom_frame = tkinter.LabelFrame(big_frame,text='Result',borderwidth=3, relief='groove')
button_frame = tkinter.Frame(big_frame)
past_entries_frame = tkinter.LabelFrame(right_big_frame, text = 'Past entries', borderwidth=3, relief='groove')
message_frame = tkinter.LabelFrame(right_big_frame,text='Directions',borderwidth=3, relief='groove')


#gallon frame stuff
gallons_label = tkinter.Label(gallon_frame, bg='white',text = 'Enter the number of gallons: ',font=('Helvetica bold',15))
gallons_label.pack(side = 'left')

gallons_entry = tkinter.Entry(gallon_frame, bg='white',width = 10, font=('Helvetica bold',15))
gallons_entry.pack(side = 'left', padx=0)

#miles frame stuff
miles_label = tkinter.Label(miles_frame,bg='white', text = 'Enter the number of miles:    ',font=('Helvetica bold',15))
miles_label.pack(side = 'left')
miles_entry = tkinter.Entry(miles_frame,bg='white', width=10, font=('Helvetica bold',15))
miles_entry.pack(side = 'left')

#listbox stuff
message = tkinter.Label(message_frame, text = 'Welcome to the Miles Per Gallon program please enter the the amount of gallons of gasoline and the miles\n and click on calculate!', font=('Helvetica bold',10))
message.pack(side='top')
listbox  = tkinter.Listbox(past_entries_frame, width=65,bg = 'white')
listbox.pack(side = 'top')

#bottom frame stuff
miles_per_gallon_label = tkinter.Label(bottom_frame, text = ' ',font=('Helvetica bold',15))
miles_per_gallon_label.pack(side = 'left')
value = tkinter.StringVar()
answer_label = tkinter.Label(bottom_frame,textvariable=value,font=('Helvetica bold',15))
answer_label.pack( side = 'left')

#button frame
calculate_button = tkinter.Button(button_frame, text = 'Calculate', bg= 'green',font=('Helvetica bold',15), command = calculate)
calculate_button.pack(side = 'left')
quit_button = tkinter.Button(button_frame, text = '    Exit    ', bg=  'red',  font=('Helvetica bold',15), command= main_window.destroy)
quit_button.pack(side='left', padx=5)
reset_button = tkinter.Button(button_frame, text='     Clear    ', bg = 'yellow', font=('Helvetica bold',15),command = reset)
reset_button.pack(side = 'left')

#canvas.create_text(0,0,text='User input')
#packing frames
big_frame.pack(side = 'left')
right_big_frame.pack(side = 'left', padx=5)
top_frame.pack(ipadx=5, ipady=5, pady = 8)
gallon_frame.pack(pady = 5)
miles_frame.pack()
bottom_frame.pack(ipadx = 5,ipady= 5, pady = 8)
button_frame.pack()
canvas.pack()
message_frame.pack()
past_entries_frame.pack(pady=5)

tkinter.mainloop()