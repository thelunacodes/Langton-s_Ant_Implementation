from tkinter import *
from funcs import *
import numpy as np

SPEED = 1 #The interval of the "ant's" moves, in seconds

window = Tk() #Window of the program
window.title("Langton's Ant Implementation (by thelunacodes)") #Title of the window
window.resizable(False, False) #Make so the window can't be resized

win_width = 800 #Width of the window
win_height = 800 #Height of the window
sc_width = window.winfo_screenwidth() #Width of the screen
sc_height = window.winfo_screenheight() #Height of the screen

x = int((sc_width/2)-(win_width/2))
y = int((sc_height/2)-(win_height/2))

window.geometry(f"{win_width}x{win_height}+{x}+{y}") #Sets the window's size and makes it open on the center of the screen

grid_canvas = Canvas(window, width=win_width, height=win_height, bg="#ffffff") #Canvas used to show the "ant" and the black squares
grid_canvas.pack()

#Array to keep track of the grid's state
grid_array = np.array([["W" for w in range(win_width//4)] for h in range(win_height//4)])

#Array of coordinates (X,Y) of each black square in the grid
black_square_array = []

#"Ant's" starting coordinate 
ant_x = win_width//2 
ant_y = win_height//2

#The "Langton's Ant" (a 4x4 square)
ant = grid_canvas.create_rectangle(ant_x-2, ant_y-2, ant_x+2, ant_y+2, fill="#FF0200", outline="#FF0200") 

#The function responsible for the moviment of the "ant"
window.after(1000, move_ant, ant, ant_x, ant_y, grid_canvas, SPEED, 3, grid_array, black_square_array)

window.mainloop()
