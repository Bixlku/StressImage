import numpy as np
import math

def CircleCenter(p1, p2, p3):
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]
    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]
    x21 = p2[0] - p1[0]
    y21 = p2[1] - p1[1]
    x32 = p3[0] - p2[0]
    y32 = p3[1] - p2[1]
    # three colinear
    if (x21 * y32 - x32 * y21 == 0):
        return None
    xy21 = p2[0] * p2[0] - p1[0] * p1[0] + p2[1] * p2[1] - p1[1] * p1[1]
    xy32 = p3[0] * p3[0] - p2[0] * p2[0] + p3[1] * p3[1] - p2[1] * p2[1]
    y0 = (x32 * xy21 - x21 * xy32) / ( 2 * (y21 * x32 - y32 * x21))
    x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)

    f = np.array([x2 - p2[2] * ((x2 - x0) / math.sqrt((x2 - x0) ** 2 + (y2 - y0) ** 2)),
                  y2 - p2[2] * ((y2 - y0) / math.sqrt((x2 - x0) ** 2 + (y2 - y0) ** 2))])
    R = ((p1[0] - x0) ** 2 + (p1[1] - y0) ** 2) ** 0.5
    return f
