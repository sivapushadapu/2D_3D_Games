from ursina import *

app = Ursina()

ball = Entity(model='sphere', color=color.blue, scale=0.5, position=(0, 4, 0))
velocity = Vec3(0.08, 0.12, 0)


def update():
    global velocity
    ball.position += velocity
    # Check for window boundaries (simple 2D bounce)
    if abs(ball.x) > 6:
        velocity.x *= -1
    if ball.y < 0.5 or ball.y > 7:
        velocity.y *= -1
    # Gravity
    velocity.y -= 0.003


app.run()
