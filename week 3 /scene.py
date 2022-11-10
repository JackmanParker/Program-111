# Import the functions from the Draw 2-D library
# so that they can be used in this program.

import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, 400, 200, 200)
    draw_cloud(canvas, 200, 300, 100)
    for i in range(random.randint(0,6)):
        draw_cloud (canvas, random.randint(100, 800), random.randint(150, 800), 200)
    draw_cactus(canvas, 200, 50, 200 )
    draw_cactus(canvas, 100, 25, 100)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 6,
        scene_width, scene_height, width=0, fill="indian red")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 5,
        width=0, fill="tan")

def draw_cloud(canvas, center_x, bottem, height):
    cloud_width = height / 2
    cloud_heighth = height / 4
    cloud_left = center_x - cloud_width / 2
    cloud_right = center_x + cloud_width /2
    cloud_top = bottem + cloud_heighth
    draw_oval(canvas, cloud_left, cloud_top, cloud_right, bottem, outline="gray", width=1, fill="gray")

def draw_cactus(canvas, center_x, bottem, height):
    cactus_body = height 
    cactus_width = height / 3
    cactus_left = center_x - cactus_width /2
    cactus_right = center_x + cactus_width /2
    cactus_top = bottem + cactus_body
   #body of the cactus
    draw_rectangle(canvas, cactus_left, cactus_top, cactus_right, bottem, outline='green', fill='green')
   #Draw the arm
    draw_rectangle(canvas, cactus_left, cactus_right * .5 , cactus_left * .7 , bottem * 2.8, outline='green', fill='green')

    #nub of the arm
    draw_rectangle(canvas, cactus_left * .7, cactus_right  * .5, cactus_left * .9, bottem * 4, outline='green', fill='green')
    
# Call the main function so that
# this program will start executing.
main()
