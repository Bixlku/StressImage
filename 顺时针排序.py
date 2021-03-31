from functools import reduce
import operator
import math
coords = [(0, 1), (1, 0), (1, 1), (0, 0),(0.5,2)]
center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
arry=sorted(coords, key=lambda coord: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)
print(arry)