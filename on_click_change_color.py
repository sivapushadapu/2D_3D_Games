from ursina import *

app = Ursina()

cube = Entity(model='cube', color=color.azure, scale=2)


def input(key):
    if key == 'left mouse down':
        cube.color = color.random_color()
    if key == 'space':
        cube.color = color.random_color()


Text("Click or press SPACE to change color", origin=(0, 7))

app.run()
