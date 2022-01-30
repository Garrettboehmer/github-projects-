#Garrett Boehmer
#Lab 4 Part 3
#Shipping Charges
#This program attempts to deliever a price when given a certain weight

import tkinter
import tkinter.font

main_window = tkinter.Tk()
main_window.title('Garrett Boehmers, Shipping Charges, Lab 4 part 3')


def calculate():
    #RPP for 2 pounds or less
    PRICE_1 = 1.50
    #RPP for 2 to 6 lbls
    PRICE_2 = 3.00
    #RPP for 6 to 10 lbls
    PRICE_3 = 4.00
    #RPP for 10lbls and over
    PRICE_4 = 4.75
    try:
        weight_num = float(weight_entry.get())
        if weight_num>=0:
            if weight_num <= 2:
                cost = PRICE_1 * weight_num
                value.set(f'Rate per pound: {PRICE_1: .2f}$\n\n Total shipping charges: {cost:,.2f}$')
                listbox.insert(0, f'{weight_num} pounds: {value.get()}')
            elif weight_num > 2 and weight_num <= 6:
                cost = PRICE_2 * weight_num
                value.set(f'Rate per pound: {PRICE_2: .2f}$\n\n Total shipping charges: {cost:,.2f}$')
                listbox.insert(0, f'{weight_num} pounds: {value.get()}')
            elif weight_num > 6 and weight_num <=10:
                cost = PRICE_3 * weight_num
                value.set(f'Rate per pound: {PRICE_3: .2f}$\n\n Total shipping charges: {cost:,.2f}$')
                listbox.insert(0, f'{weight_num} pounds: {value.get()}')
            elif weight_num > 10:
                cost = PRICE_4 * weight_num
                value.set(f'Rate per pound: {PRICE_4: .2f}$\n\n Total shipping charges: {cost:,.2f}$')
                listbox.insert(0, f'{weight_num} pounds: {value.get()}')
            else:
                print("none of the conditions have been met")
            
        else:
            value.set(f'Weight has to be greater than 0')
    except ValueError:
        value.set(f'Please enter a number')

def reset():
    weight_entry.delete(0, 'end')
    value.set(' ')


#width of the canvas
WIDTH = 25
#hieght of the canvas
HEIGHT = 25
canvas = tkinter.Canvas(main_window, width = WIDTH, height = HEIGHT)
#inside big frames and thier childeren

big_frame = tkinter.Frame(main_window)
top_frame = tkinter.LabelFrame(big_frame, text='User inputs', bg = 'white',borderwidth=3, relief='groove')
weight_frame = tkinter.Frame(top_frame,bg='white')
bottom_frame = tkinter.LabelFrame(big_frame,text='Result',borderwidth=3, relief='groove')
button_frame = tkinter.Frame(big_frame)
right_big_frame = tkinter.Frame(main_window)
past_entries_frame = tkinter.LabelFrame(right_big_frame, text = 'Past entries', borderwidth=3, relief='groove')
message_frame = tkinter.LabelFrame(right_big_frame,text='Directions',borderwidth=3, relief='groove')


#weight frame
weight_label = tkinter.Label(weight_frame, bg='white',text = 'Enter the weight: ',font=('Helvetica bold',15))
weight_label.pack(side = 'left')
weight_entry = tkinter.Entry(weight_frame, bg='white',width = 10, font=('Helvetica bold',15))
weight_entry.pack(side = 'left', padx=0)

#Bottom frame
price_per_pound = tkinter.Label(bottom_frame, text = ' ',font=('Helvetica bold',15))
price_per_pound.pack(side = 'left')
value = tkinter.StringVar()
answer_label = tkinter.Label(bottom_frame,textvariable=value,font=('Helvetica bold',15))
answer_label.pack( side = 'left')

#listbox inside right big frame
message = tkinter.Label(message_frame, text = 'Welcome to the shipping charges program please enter the weight of the package in the space indicated\n and click on calculate!', font=('Helvetica bold',10))
message.pack(side='top')
listbox  = tkinter.Listbox(past_entries_frame, width=65,bg = 'white')
listbox.pack(side = 'top')

#button frame
calculate_button = tkinter.Button(button_frame, text = 'Calculate', bg= 'green',font=('Helvetica bold',15), command = calculate)
calculate_button.pack(side = 'left')
quit_button = tkinter.Button(button_frame, text = '    Exit    ', bg=  'red',  font=('Helvetica bold',15), command= main_window.destroy)
quit_button.pack(side='left', padx=5)
reset_button = tkinter.Button(button_frame, text='     Clear    ', bg = 'yellow', font=('Helvetica bold',15),command = reset)
reset_button.pack(side = 'left')

#frame packs
big_frame.pack(side = 'left')
right_big_frame.pack(side = 'left', padx=5)
top_frame.pack(ipadx=5, ipady=5, pady = 8)
weight_frame.pack(side = 'top',pady = 5)
bottom_frame.pack(side= 'top',ipadx = 5,ipady= 5, pady = 8)
button_frame.pack(side = 'bottom',padx=5)
canvas.pack()
message_frame.pack()
past_entries_frame.pack(pady=5)

tkinter.mainloop()