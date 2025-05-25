from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale=(1, 2, 1), position=(0, 0, 0))


def update():
    speed = 5 * time.dt
    if held_keys['a']:
        player.x -= speed
    if held_keys['d']:
        player.x += speed
    if held_keys['w']:
        player.z += speed
    if held_keys['s']:
        player.z -= speed


app.run()
