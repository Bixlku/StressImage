import numpy as np


def GetAngle(x,y):
    Lx = np.sqrt(x.dot(x))
    Ly = np.sqrt(y.dot(y))
    # 相当于勾股定理，求得斜线的长度
    cos_angle = x.dot(y) / (Lx * Ly)
    # 求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度，初中知识。。
    print(cos_angle)
    angle = np.arccos(cos_angle)
    angle2 = angle * 360 / 2 / np.pi
    # 变为角度
    return (angle2)