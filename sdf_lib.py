

def circle_sdf(point, center, radius):
    ux, uy = point[0] - center[0], point[1] - center[1]
    return (ux * ux + uy * uy)**0.5 - radius