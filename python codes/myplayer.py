#Garrett Boehmer
#python project #3 "music player"
#This program hopes to make a player that can play music


import tkinter
import tkinter.font
MAIN_WINDOW = tkinter.Tk()
import tkinter.filedialog
from pygame import mixer
import pygame
import os
mixer.init()

#this button asks the user to pick a file with music in it and it only displays files that are .mp3 in the listbox
#then it switches the user directory to the one chosen by the user
#also if you choose a different directory the listbox is destroyed
def open(listbox):
        count = 0
        listbox.delete(0, 'end')
        music_path = tkinter.filedialog.askdirectory()
        music_list = os.listdir(music_path)
        for music in music_list:
            if music.endswith('.mp3'):
                count =+ 1
                listbox.insert(0, music)
        if count ==0:
            listbox.insert(0, 'NO .mp3 ARE IN THIS DIRECTORY')
        os.chdir(music_path)
    
#this play button goes through what is selected by the user and then takes what is selected and searches the directory that is currently being used for the selecting in the list box. 
def play(listbox, value):
    try:
        #retrieving what is selceted by the user
        indexes_music = listbox.curselection()
        #searches through current directory and finds a match for the selected item in listbox
        for i in indexes_music:
            file = listbox.get(i)
        mixer.music.load(file)
        mixer.music.play()
        #sending this music file into the .sound method
        song_length = pygame.mixer.Sound(file)
        #extracting the amount of time it takes
        value.set(f'{int((song_length.get_length())/60):,.2f}')
    except:
        listbox.insert(0, 'Cant play a song if theres no .mp3')

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

#had to make this outside of main() to get the clock to work
top_big_frame = tkinter.Frame(MAIN_WINDOW)
left_big_frame = tkinter.LabelFrame(top_big_frame, text='Song info', bg = 'white', borderwidth=3, relief='groove')
current_time = tkinter.Label(left_big_frame,font=('Helvetica bold',15))
current_time.pack( side = 'left', padx=5)


#i found .config and .after in a youtube video and i tried my best to make it my own but i couldnt find a way
#i found those methods at https://www.youtube.com/watch?v=1zPyYf_XBD4&t=828s
#i had to pull some things out of main() in order for it to work
def get_time():
    internal_clock = pygame.mixer.music.get_pos()
    minutes = int(((internal_clock))/(1000*60))%60
    seconds = int((internal_clock)/1000)%60
    whole_time = f'{minutes:,.0f}:{seconds:,.0f}'
    current_time.config(text = whole_time)
    current_time.after(1000, get_time)

def main():

    right_big_frame = tkinter.LabelFrame(top_big_frame, text='Song list', bg = 'white', borderwidth=3, relief='groove')
    right_right_big_frame = tkinter.LabelFrame(top_big_frame, text='Playlist', bg = 'white', borderwidth=3, relief='groove')
    
    MAIN_WINDOW.title('Garrett Boehmers music player')

    #frames
    bottom_big_frame =tkinter.LabelFrame(MAIN_WINDOW, text='Buttons', bg = 'white', borderwidth=3, relief='groove')
    button_big_frame = tkinter.Frame(bottom_big_frame, bg = 'white', borderwidth=3, relief='groove')

    #stuff in button frame
    play_button = tkinter.Button(button_big_frame, text = 'Play', bg= 'green',font=('Helvetica bold',15), command=lambda:play(listbox, value))
    play_button.pack(side = 'left')
    pause_button = tkinter.Button(button_big_frame, text = 'Pause', bg= 'green',font=('Helvetica bold',15), command = pause)
    pause_button.pack(side = 'left', padx=5)
    unpause_button = tkinter.Button(button_big_frame, text = 'Unpause', bg= 'green',font=('Helvetica bold',15), command = unpause)
    unpause_button.pack(side = 'left')
    open_folder = tkinter.Button(button_big_frame, text = 'Open folder', bg= 'green',font=('Helvetica bold',15), command=lambda:open(listbox))
    open_folder.pack(side = 'left')
    quit_button = tkinter.Button(button_big_frame, text = '    Quit    ', bg=  'red',  font=('Helvetica bold',15), command= MAIN_WINDOW.destroy)
    quit_button.pack(side='left', padx=5)
    #listbox
    listbox  = tkinter.Listbox(right_big_frame, width=65,bg = 'white')
    listbox.pack(side = 'left',padx=5)

    #sad attempt at retrieving the total time of the song
    value = tkinter.StringVar()
    answer_label = tkinter.Label(left_big_frame,textvariable=value,font=('Helvetica bold',15))
    answer_label.pack(side = 'left')

    #packing
    top_big_frame.pack(side = 'top')
    left_big_frame.pack(side='left')
    right_big_frame.pack(side='left', padx=5)
    right_right_big_frame.pack(side = 'left')
    bottom_big_frame.pack(side= 'top', pady=5)
    button_big_frame.pack()

    #constantly running and checking the position of where the song is at
    get_time()

    tkinter.mainloop()

main()