import numpy as np
from scipy import spatial
import GetAngle
import CircleCenter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.interpolate import make_interp_spline


pt1 = np.loadtxt('有空洞-非线性接触inner.csv', skiprows=0,delimiter=",",usecols=(0,1)) #numpy
pt2 = np.loadtxt('有空洞-不考虑接触inner.csv', skiprows=0,delimiter=",",usecols=(0,1)) #numpy
pt3 = np.loadtxt('无空洞空格inner.csv', skiprows=0,delimiter=",",usecols=(0,1)) #numpy
circle = np.loadtxt('sortinner.csv',skiprows=0,delimiter=",",usecols=(0,1))




plt.plot(pt1[:,0],pt1[:,1], color="blue", linewidth=1.0, linestyle="-", label="有空洞-非线性接触")
    # 绘制颜色为紫色、宽度为 2 像素的不连续曲线 y2
plt.plot(pt2[:,0],pt2[:,1], color="red", linewidth=1.0, linestyle="-", label="有空洞-不考虑接触")
plt.plot(pt3[:,0],pt3[:,1], color="green", linewidth=1.0, linestyle="-", label="无空洞")
plt.plot(circle[:,0],circle[:,1], color="orange", linewidth=2.0, linestyle="-", label="外轮廓")
plt.legend(loc="upper left")
plt.title('内表面', fontsize=12, color='r')
plt.savefig( 'outside' + '.jpg')
plt.show()