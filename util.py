import numpy
SDF = 0
EMISSIVE = 1
# Jittered Sampling
def get_random_angle_matrix_list(x, y, sample_num, method):
    res = []
    pi_div = numpy.pi/sample_num
    for i in range(0, sample_num):
        res.append((numpy.random.ranf((x,y))+i)*pi_div)
    return res

def union_op(a, b):
    return a[SDF] > b[SDF] and a or b

print(numpy.zeros((2, 2, 3))+0.1)