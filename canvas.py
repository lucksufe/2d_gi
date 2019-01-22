import numpy
from PIL import Image
from util import *

class Canvas:
    def __init__(self, width, height, *args, **kwargs):
        self.array = numpy.zeros((height, width, 3))
        self.image = Image.fromarray(numpy.uint8(self.array))
        self.scene = None
        self.max_steps = kwargs.get('max_step', 10)
        self.step_distance = kwargs.get('step_distance', (width**2+height**2)**0.5)

    def add_scene(self, scene):
        self.scene = scene
    
    def render(self):

        
# class Scene:
#     def __init__(self):
#         pass

# def circle_sdf(point, center, radius):
#     ux, uy = point[0] - center[0], point[1] - center[1]
#     return (ux * ux + uy * uy)**0.5 - radius

# def trace():
#     pass

# get_random_angle_matrix_list(5,5,2,0)
# print (union_op({'sd':2}, {'sd':3}))