from PIL import Image
import random
import math


def random_color(image_instance):
    for i in range(0, image_instance.width):
        for j in range(0, image_instance.height):
            image_instance.putpixel([i, j], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


# y = ax + b
def dda_method(image_instance, a=1, b=0):
    y = b
    for x in range(0, image_instance.width):
        image_instance.putpixel([x, image_instance.height-1-int(y)], (255, 255, 255))
        y += a


def circle_sdf(point, center, radius):
    ux, uy = point[0] - center[0], point[1] - center[1]
    return math.sqrt(ux*ux+uy*uy) - radius


# direction is a normalized 2d vector
# origin is a point
def trace(origin, target, radius, direction, intensity, max_steps=5, max_distance=200, tolerance=1e-6):
    distance = 0
    for idx in range(0, max_steps):
        step_length = circle_sdf((origin[0]+direction[0]*distance, origin[1]+direction[1]*distance), target, radius)
        distance += step_length
        if step_length < tolerance:
            return intensity
        if step_length > max_distance:
            return 0
    return 0


# def generate_random_direction():
#     temp = random.random()
#     return tuple([temp, math.sqrt(1-temp*temp)])


def get_directions(loop_num):
    result = []
    for i in range(0, loop_num):
        angle = math.pi * 2.0 * random.random()
        result.append((math.sin(angle), math.cos(angle)))
    return result


def render(image_instance):
    target = (200, 200)
    radius = 10
    sample_num = 100
    percentage = 0
    for i in range(0, image_instance.width):
        for j in range(0, image_instance.height):
            val = 0
            for direction in get_directions(sample_num):
                val += trace((i, j), target, radius, direction, 50)
            if val == 0:
                continue
            val /= float(sample_num * 4)
            val = min(int(val * 255), 255)
            image_instance.putpixel([i, image_instance.height-1-int(j)], (int(val), int(val), int(val)))
        if not percentage == i*100/image_instance.width:
            percentage = i*100/image_instance.width
            print('rendering {0}%'.format(percentage))


width, height = 400, 400
c = Image.new("RGB", (width, height))
render(c)
c.show()

