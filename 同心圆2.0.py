import CircleCenter
import numpy as np
import InsideOrOutside

r=-2

pt=np.loadtxt("OuterPoint.csv", skiprows=0,delimiter=",",usecols=(0,1))
xmax = np.max(pt, axis=0)[0]
xmin = np.min(pt, axis=0)[0]
ymax = np.max(pt, axis=0)[1]
ymin = np.min(pt, axis=0)[1]
Center=[(xmax+xmin)/2,(ymax+ymin)/2]

count=np.arange(pt.shape[0])
putout = np.empty([pt.shape[0], 2])
for i in count:
    putout[i] = CircleCenter.CircleCenter(Center, r, [pt[i][0], pt[i][1]])
putout=np.append(putout, [putout[0]], axis=0)

np.savetxt("OuterPoint"+(r*-1).__str__()+".csv",putout,fmt='%f',delimiter=',')

print('x')
