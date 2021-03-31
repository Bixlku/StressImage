import numpy as np
import CircleCenter
import pandas as pd
"""
p2=np.array([1,2,1])
p1=np.array([-1,5,0])
p3=np.array([1,-1,1])
print(CircleCenter.CircleCenter(p1,p2,p3))
print()
"""

dic=pd.DataFrame({
        'cos_value':[1,2,3,6,6,6],
        'norm_list':[1,2,3,7,5,6]
        })

dic=dic.sort_values(by=['cos_value', 'norm_list'], ascending=False)
print(dic)
#DYX = np.zeros((1,8))
#HXH = np.ones((1,8))
#XH = np.append(DYX, HXH,axis=0)
#x=np.array([[1,2,3,4,5,6,7,8]])
#y=np.array([1,1])
#x=np.append(y,x,axis=1)
#print("?")

