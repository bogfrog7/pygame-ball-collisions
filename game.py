import pygame
import pymunk

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
window = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 100)


def simulate_dynamic_obj():
    body = pymunk.Body(mass=1, moment=100, body_type=pymunk.Body.DYNAMIC)  # note: the movement parameter is the
    # resistance of movement
    body.position = (300, 0)
    shape = pymunk.Circle(body, 30)
    space.add(body, shape)
    return shape


def simulate_static_obj():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (400,500)
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape

def draw(obj_list):
    for obj in obj_list:
        pygame.draw.circle(window, (0, 0, 0), (obj.body.position.x, obj.body.position.y), obj.radius)

obj_list = []
obj_list.append(simulate_dynamic_obj())
obj_list.append(simulate_static_obj())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(-1)

    space.step(1/50) # updates our simulation
    draw(obj_list)
    clock.tick(180)
    pygame.display.update()
    window.fill("white")

