#!/usr/bin/env python
# encoding: utf-8
# Demonstration of a draggable magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
w = 1521
h = 1818

# Map scale
sc = 3

# Magnifier scale and position
r = 20
p = [w // (2*sc), h // (2*sc)]

# Create Window for Map
frame = simplegui.create_frame("Map magnifier", w//sc, h//sc)

# Move magnifier to clicked position
def click(pos):
    p[0] = pos[0]
    p[1] = pos[1]

frame.set_mouseclick_handler(click)

# Allow magnifier to be dragged
def drag(pos):
    p[0] = pos[0]
    p[1] = pos[1]

frame.set_mousedrag_handler(drag)

# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image, (w//2,h//2), (w,h), 
                      (w//sc//2,h//sc//2), (w//sc,h//sc))

    # Draw magnifier    
    maprectangle = (2*sc*r,2*sc*r)
    mapcenter = (sc*p[0],sc*p[1])
    magrectangle = (2*sc*r,2*sc*r)
    magcenter = p
    canvas.draw_image(image, mapcenter, maprectangle,
                             magcenter, magrectangle)

    # Draw outline around magnifier
    magleft = magcenter[0] - magrectangle[0] // 2
    magright = magcenter[0] + magrectangle[0] // 2
    magtop = magcenter[1] - magrectangle[1] // 2
    magbottom = magcenter[1] + magrectangle[1] // 2
    magtopleft = (magleft, magtop)
    magtopright = (magright, magtop)
    magbotleft = (magleft, magbottom)
    magbotright = (magright, magbottom)
    box = [magtopleft, magbotleft, magbotright, 
           magtopright, magtopleft]
    canvas.draw_polyline(box, 4, "Blue")
    
frame.set_draw_handler(draw)

# Slowly move magnifier automatically
def tick():
    p[0] += 1
    p[1] += 1

timer = simplegui.create_timer(60.0,tick)

# Start timer and window animation
timer.start()
frame.start()


