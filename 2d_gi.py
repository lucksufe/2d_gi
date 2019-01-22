from PIL import Image
# from pylab import *
import random
import math
import sys
import numpy as np

def circle_sdf(point, center, radius):
    ux, uy = point[0] - center[0], point[1] - center[1]
    return math.sqrt(ux * ux + uy * uy) - radius


# direction is a normalized 2d vector
# origin is a point
def trace(origin, target, radius, direction, intensity, max_steps=10, max_distance=1000, tolerance=1e-6):
    distance = 0
    for idx in range(0, max_steps):
        step_length = circle_sdf((origin[0]+direction[0]*distance, origin[1]+direction[1]*distance), target, radius)
        distance += step_length
        if step_length < tolerance:
            return intensity
        if step_length > max_distance:
            return 0
    return 0



def get_directions(loop_num):
    result = []
    for i in range(0, loop_num):
        angle = math.pi * 2.0 * random.random()
        result.append((math.sin(angle), math.cos(angle)))
    return result


def render(image_instance):
    target = (256, 256)
    radius = 51
    sample_num = 64
    percentage = 0
    for i in range(0, image_instance.width):
        for j in range(0, image_instance.height):
            val = 0
            for direction in get_directions(sample_num):
                val += trace((i, j), target, radius, direction, 2)
            if val == 0:
                continue
            val /= sample_num
            val = min(int(val * 255), 255)
            image_instance.putpixel([i, image_instance.height-1-int(j)], (int(val), int(val), int(val)))
        if not percentage == i*100/image_instance.width:
            percentage = i*100/image_instance.width
            print('rendering {0}%'.format(percentage))


width, height = 2, 4
c = Image.new("RGB", (width, height))
# render(c)
# c.show()
# sys.exit(0)
print(np.asarray(c))
print(np.zeros((4,2,3)))
