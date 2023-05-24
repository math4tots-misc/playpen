from playpen import *


WIDTH, HEIGHT = get_screen_size()

triangle = Polygon([
    Vector(WIDTH / 2 - 30, HEIGHT / 2 + 20),
    Vector(WIDTH / 2 + 30, HEIGHT / 2 + 20),
    Vector(WIDTH / 2,      HEIGHT / 2 - 25),
])


# This line makes your program wait for you to press
# a key or move stuff around with your mouse.
mainloop()
