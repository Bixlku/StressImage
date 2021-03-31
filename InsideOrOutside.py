import numpy as np
import math

def InsideOrOutside(points,Center,r):
    output=[]
    nppoints=np.array(points)
    for i in range(0,nppoints.shape[0]):
        if clength(points[i],Center) > r :
            output.append([points[i],i])



    return output


def clength(point,Center):
    l=math.sqrt((point[0]-Center[0])**2+(point[1]-Center[1])**2)
    return l
