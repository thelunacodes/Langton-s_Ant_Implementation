import time
from tkinter import *
import numpy as np

def delete_black_square(canvas:Canvas, old_pos:list, bl_sq_arr:list):
    """Remove a black square based on the "ant's" old position.

    Args:
        canvas (Canvas): Canvas where the black squares and the "ant" are created.
        old_pos (list): The "ant's" old position.
        bl_sq_arr (list): Array with all black square coordinates.

    Returns:
        None: This function does not return anything. 
    """

    #Run through all the canvas's itens 
    for item in canvas.find_all():
        #Check if item is a rectangle
        if canvas.type(item) == "rectangle":
            #Check if the black square is the one we're trying to remove
            if old_pos == canvas.coords(item) and canvas.coords(item) in bl_sq_arr: 
                bl_sq_arr.remove(canvas.coords(item)) #Since the black square is going to be removed, its coordinates will be removed as well
                canvas.delete(item) #Remove the black square from the canvas
                print("[DEBUG] The black square was removed!") #BLACK SQUARE HAS BEEN REMOVED 
                return 

    print("[DEBUG] The black square wasn't found!") #BLACK SQUARE HASN'T BEEN REMOVED 
    return #The black square wasn't found, nothing will be removed 

def move_ant(a, aX:int, aY:int, canvas:Canvas, speed:int, dir:int, grid_array:list, bl_sq_arr:list):
    old_ant_coords = canvas.coords(a) #Old "ant" coordinates
    oldX = int(old_ant_coords[0] / 4) #Old X position in the grid
    oldY = int(old_ant_coords[1] / 4) #Old Y position in the grid

    #Check if the grid position is white
    old_grid_position_is_white = grid_array[oldY, oldX] == "W" 

    #Turn the "ant" based on the current grid's color
    if old_grid_position_is_white: 
        dir = (dir + 1) % 4 #Turn "ant" 90° clockwise
    else:
        dir = (dir - 1) % 4 #Turn "ant" 90° anticlockwise

    print(f"[DEBUG] Current ant direction: {dir}") #CURRENT DIRECTION DEBUG MESSAGE

    #Update "ant's" position based on the new direction
    if dir == 0:
        #Move north 
        aY -= 4   
        aY = aY % 800 #The "ant" will wrap around the canvas if necessary
    elif dir == 1:
        #Move east
        aX += 4 
        aX = aX % 800
    elif dir == 2: 
        #Move south
        aY += 4 
        aY = aY % 800
    elif dir == 3:
        #Move west
        aX -= 4
        aX = aX % 800 
        
    canvas.delete(a) #Remove "ant" from its old position
    a = canvas.create_rectangle(aX-2, aY-2, aX+2, aY+2, fill="#FF0200", outline="#FF0200") #Place the "ant" at the new position
    
    print(f"[DEBUG] The ant moved (x={aX},y={aY})") #CURRENT POSITION DEBUG MESSAGE

    #Add or delete black squares
    if old_grid_position_is_white:
        print(f"[DEBUG] The last square was WHITE") #LAST SQUARE COLOR DEBUG MESSAGE (WHITE)
        b = canvas.create_rectangle(int(old_ant_coords[0]), int(old_ant_coords[1]), int(old_ant_coords[2]), int(old_ant_coords[3]), fill="#000000", outline="#000000") #Adds the black square at the old position
        bl_sq_arr.append(canvas.coords(b)) #Adds the black square coordinates to the array
        grid_array[oldY, oldX] = "B" #Update the grid state array position to "B" (black)
    else:
        print(f"[DEBUG] The last square was BLACK") #LAST SQUARE COLOR DEBUG MESSAGE (BLACK)
        delete_black_square(canvas, old_ant_coords, bl_sq_arr) #Removes the black square from its old position
        grid_array[oldY, oldX] = "W" #Update the grid state array position to "W" (white)      
     
    canvas.after((speed*10), move_ant, a, aX, aY, canvas, speed, dir, grid_array, bl_sq_arr)
