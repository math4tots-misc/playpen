from playpen import *


WIDTH, HEIGHT = get_screen_size()

triangle = Polygon([
    Vector(WIDTH / 2 - 30, HEIGHT / 2 + 20),
    Vector(WIDTH / 2 + 30, HEIGHT / 2 + 20),
    Vector(WIDTH / 2,      HEIGHT / 2 - 25),
])


@on_tick
def _():
    triangle.angle += 0.02

@on_click
def _(e: ClickEvent):
    triangle.position = Vector(e.x, e.y)

# This line makes your program wait for you to press
# a key or move stuff around with your mouse.
mainloop()
