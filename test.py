from vpython import *

def collision(a, b, r):
    dx = a.pos.x - b.pos.x
    dy = a.pos.y - b.pos.y

    dist = sqrt(dx * dx + dy * dy)

    if dist <= 2 * r:
        cosA = dx / (2 * r)
        sinA = dy / (2 * r)
        # iloczyn skalarny wektorów
        a.velocity = a.velocity - (dot(a.velocity - b.velocity, a.pos - b.pos) / dist ** 2) * (a.pos - b.pos)
        tempA = a
        b.velocity = b.velocity - (dot(b.velocity - tempA.velocity, b.pos - tempA.pos) / dist ** 2) * (b.pos - tempA.pos)
        print("****COLLISION****")
        print("a v = ", a.velocity)
        print("b v = ", b.velocity)
        while dist <= 2:
            a.pos += a.velocity
            b.pos += b.velocity
            dx = a.pos.x - b.pos.x
            dy = a.pos.y - b.pos.y
            dist = sqrt(dx * dx + dy * dy)

radius = 2

scene = canvas()

ball_1 = sphere(pos=vector(0, 5, 0), radius=radius, color=color.cyan)
ball_2 = sphere(pos=vector(0, 0, 0), radius=radius, color=color.red)

ball_1.velocity = vector(0.1, 0, 0)
ball_2.velocity = vector(0.05, 2, 0)

t = 0
dt = 0.05
while t < 700:
    rate(100)
    collision(ball_1, ball_2, radius)
    ball_1.pos += ball_1.velocity
    ball_2.pos += ball_2.velocity
    if ball_1.pos.x >= 15 or ball_1.pos.x <= -15:
        ball_1.velocity.x = -ball_1.velocity.x
        ball_1.pos += ball_1.velocity
    if ball_1.pos.y >= 15 or ball_1.pos.y <= -15:
        ball_1.velocity.y = -ball_1.velocity.y
        ball_1.pos += ball_1.velocity
    if ball_2.pos.x >= 15 or ball_2.pos.x <= -15:
        ball_2.velocity.x = -ball_2.velocity.x
        ball_2.pos += ball_2.velocity
    if ball_2.pos.y >= 15 or ball_2.pos.y <= -15:
        ball_2.velocity.y = -ball_2.velocity.y
        ball_2.pos += ball_2.velocity

    t += dt
    print("____POSITIONS_____")
    print("ball_1.pos = ", ball_1.pos)
    print("ball_2.pos = ", ball_2.pos)