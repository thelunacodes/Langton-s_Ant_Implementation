import time
from tkinter import *
import numpy as np

def delete_black_square(canvas:Canvas, ant_pos:list, bl_sq_arr:list):
    """Remove a black square based on the "ant's" coordinate.

    Args:
        canvas (Canvas): Canvas where the black squares and the "ant" are created.
        ant_pos (list): The "ant's" coordinate.
        bl_sq_arr (list): Array with all black square coordinates.

    Returns:
        None: This function does not return anything. 
    """

    #Run through all the canvas's itens 
    for item in canvas.find_all():
        #Check if item is a rectangle
        if canvas.type(item) == "rectangle":
            #Check if the black square is the one we're trying to remove
            if ant_pos == canvas.coords(item) and canvas.coords(item) in bl_sq_arr: 
                bl_sq_arr.remove(canvas.coords(item)) #Since the black square is going to be removed, its coordinates will be removed as well
                canvas.delete(item) #Remove the black square from the canvas
                print("[DEBUG] The black square was removed!") #BLACK SQUARE HAS BEEN REMOVED 
                return 

    print("[DEBUG] The black square wasn't found!") #BLACK SQUARE HASN'T BEEN REMOVED 
    return #The black square wasn't found, nothing will be removed 

def ant_movement_handler(a, aX:int, aY:int, canvas:Canvas, speed:int, dir:int, grid_array:list, bl_sq_arr:list):
    """Function responsible 

    Args:
        a (_type_): _description_
        aX (int): _description_
        aY (int): _description_
        canvas (Canvas): _description_
        speed (int): _description_
        dir (int): _description_
        grid_array (list): _description_
        bl_sq_arr (list): _description_
    """
    ant_coords = canvas.coords(a) #The "ant's" coordinates in the canvas
    posX = int(ant_coords[0] / 4) #X position of the "ant" in the canvas
    posY = int(ant_coords[1] / 4) #Y position of the "ant" in the canvas

    #Check if the "ant's" current cell is white
    grid_pos_is_white = grid_array[posY, posX] == "W" 

    #Change the "ant's" direction based on the current cell's color
    if grid_pos_is_white: 
        dir = (dir + 1) % 4 #Turn 90° clockwise
    else:
        dir = (dir - 1) % 4 #Turn 90° anticlockwise

    print(f"[DEBUG] Current ant direction: {dir}") #CURRENT DIRECTION DEBUG MESSAGE

    #Add or delete black squares
    if grid_pos_is_white:
        print(f"[DEBUG] The last square was WHITE") #LAST SQUARE COLOR DEBUG MESSAGE (WHITE)
        b = canvas.create_rectangle(int(ant_coords[0]), int(ant_coords[1]), int(ant_coords[2]), int(ant_coords[3]), fill="#000000", outline="#000000") #Adds the black square at the ant's coordinates
        bl_sq_arr.append(canvas.coords(b)) #Adds the black square coordinates to the array
        grid_array[posY, posX] = "B" #Update the grid state array position to "B" (black)
    else:
        print(f"[DEBUG] The last square was BLACK") #LAST SQUARE COLOR DEBUG MESSAGE (BLACK)
        delete_black_square(canvas, ant_coords, bl_sq_arr) #Removes the black square from the ant's coordinates
        grid_array[posY, posX] = "W" #Update the grid state array position to "W" (white)      

    #Update "ant's" position based on the current direction
    if dir == 0:
        #Move north  
        aY = (aY-4) % 800 #The "ant" will wrap around the canvas if necessary
    elif dir == 1:
        #Move east
        aX = (aX+4) % 800
    elif dir == 2: 
        #Move south
        aY = (aY+4) % 800
    elif dir == 3:
        #Move west
        aX = (aX-4) % 800 
        
    canvas.delete(a) #Remove "ant" from its old position
    a = canvas.create_rectangle(aX-2, aY-2, aX+2, aY+2, fill="#FF0200", outline="#FF0200") #Place the "ant" at the new position
    
    print(f"[DEBUG] The ant moved (x={aX},y={aY})") #CURRENT POSITION DEBUG MESSAGE

    canvas.after(speed, ant_movement_handler, a, aX, aY, canvas, speed, dir, grid_array, bl_sq_arr)
