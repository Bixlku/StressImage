import numpy as np
from scipy import spatial
import GetAngle
import CircleCenter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


#df=pd.read_csv('无空洞.csv')
filename = '有空洞-非线性接触'
pt = np.loadtxt(filename+'.txt', skiprows=0,delimiter=" ",usecols=(1,2,3)) #numpy
pts = np.loadtxt(filename+'.txt', skiprows=0,delimiter=" ",usecols=(1,2)) #numpy
x=0          #x=0则是内部，x=1则是外部
pt[:,2]= pt[:,2]/1000000

#pts = np.random.rand(100_000,2)
#print(pts)

#找到最远的那一对
candidates = pts[spatial.ConvexHull(pts).vertices]
dist_mat = spatial.distance_matrix(candidates,candidates)
i,j = np.unravel_index(dist_mat.argmax(),dist_mat.shape)
print(candidates[i],candidates[j])

#记录最远的一对
recordout=np.array([[candidates[i][0],candidates[i][1]]])
recordout=np.append(recordout,[candidates[j]],axis=0)

#删掉了距离最远的一对
m1=np.where(pts == candidates[i])[0][0]
m2=np.where(pts == candidates[j])[0][2]#此处需要改进，扩展程序的适用范围#大修


ptsc = np.array(pts)
#找到角度最大的那个向量
#角度已得出

#设置锚点 锚点用于记录前两个点
anchor1=candidates[i]
anchor2=candidates[j]

#得出使向量角度最大的那个点

#删去n1中最远的那一堆向量
n1=np.arange(192) #n1用于记录有哪些点还没有被选择过
n1=np.delete(n1, np.where(n1 == m1))
n1=np.delete(n1, np.where(n1 == m2))

#前置变量
l=0

#得到外围点的坐标和序号

# innernum,outernum用于记录内部/外部点在源文件中的序号

#### 得出innernum/outernum
for m in n1:
    # 得出向量角度最小
    angle = 360
    for n in n1:
        point=ptsc[n]
        #得到两个向量的夹角，得出所有夹角中最大的那个向量并记录
        vector1=np.array([point[0]-anchor1[0],point[1]-anchor1[1]])
        vector2=np.array([anchor1[0]-anchor2[0],anchor1[1]-anchor2[1]])
        getangle=GetAngle.GetAngle(vector1,vector2)
        if getangle < angle :
            angle = getangle
            record = n

    #改变锚点的位置让循环得以进行
    anchor2=anchor1
    anchor1=ptsc[record]

    #记录innernum
    recordout=np.append(recordout,[ptsc[record]],axis=0)
    l=l+1
    count=np.arange(192)
    while l==95:
        innernum=np.array([record])
        break
    if l >95:
        innernum=np.append(innernum,record)

    #删除
    n1 = np.delete(n1, np.where(n1 == record))


#从arrange(192)中删去innernum，得到outernum
outernum = np.arange(192)
count = np.arange(96)
for i in count :
    outernum = np.delete(outernum, np.where(outernum == innernum[i]))


# 从pt(也就是源列表)中得到innernum/outernum对应点的坐标和长度，将其放入outer和inner中，并分别输出为outer.csv和inner.csv
count = np.arange(96)
for i in count:
    if i==0 :
        outer = np.array([pt[outernum[0]]])
    else :
        outer= np.append(outer,[pt[outernum[i]]],axis=0)

count = np.arange(96)
for i in count:
    if i==0 :
        inner = np.array([pt[innernum[0]]])
    else :
        inner= np.append(inner,[pt[innernum[i]]],axis=0)

np.savetxt('outer.csv',outer,fmt='%f',delimiter=',')
np.savetxt('inner.csv',inner,fmt='%f',delimiter=',')


#####################   对outer/inner进行有序排序，排序从第一象限开始，逆时针旋转，得到的为sortinner和sortouter
#将outer和inner根据x坐标从大到小排列
outer=outer[np.argsort(outer[:,0])]
inner=inner[np.argsort(inner[:,0])]
sortouter=np.empty([96,3])
sortinner=np.empty([96,3])

#筛选排序
count =np.arange(96)
t=0
s=0
for i in count :
    if outer[i][1] >= outer[0][1]:
        sortouter[t]=outer[i]
        t=t+1
    else :
        s = s + 1
        sortouter[96-s]=outer[i]

outerpoint=np.empty([96,2])
#np.savetxt('sortouter.csv',sortouter,fmt='%f',delimiter=',')

count =np.arange(96)
t=0
s=0
for i in count :
    if inner[i][1] >= inner[0][1]:
        sortinner[t]=inner[i]
        t=t+1
    else :
        s = s + 1
        sortinner[96-s]=inner[i]

innerpoint=np.empty([96,2])
#np.savetxt('sortinner.csv',sortinner,fmt='%f',delimiter=',')
#########################


###############  输出outside和inside点对应的应力图像的点
count =np.arange(94)
for i in count :
    outerpoint[i]=CircleCenter.CircleCenter(sortouter[i],sortouter[i+1],sortouter[i+2])

outerpoint[96-2]=CircleCenter.CircleCenter(sortouter[96-2],sortouter[96-1],sortouter[0])
outerpoint[96-1]=CircleCenter.CircleCenter(sortouter[96-1],sortouter[0],sortouter[1])


count =np.arange(94)
for i in count :
    innerpoint[i]=CircleCenter.CircleCenter(sortinner[i],sortinner[i+1],sortinner[i+2])

innerpoint[96-2]=CircleCenter.CircleCenter(sortinner[96-2],sortinner[96-1],sortinner[0])
innerpoint[96-1]=CircleCenter.CircleCenter(sortinner[96-1],sortinner[0],sortinner[1])


outerpoint=np.append(outerpoint,[outerpoint[0]],axis=0)
innerpoint=np.append(innerpoint,[innerpoint[0]],axis=0)
sortouter=np.append(sortouter,[sortouter[0]],axis=0)
sortinner=np.append(sortinner,[sortinner[0]],axis=0)
#################

################## 绘图
plt.xlabel("X")
plt.ylabel("Y")
# 绘制颜色为蓝色、宽度为 1 像素的连续曲线 y1
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
np.savetxt(filename+'inner.csv',innerpoint,fmt='%f',delimiter=',')
np.savetxt('sortinner.csv',sortinner,fmt='%f',delimiter=',')
np.savetxt('sortouter.csv',sortouter,fmt='%f',delimiter=',')

if x==0 :
    plt.plot(innerpoint[:,0],innerpoint[:,1], color="blue", linewidth=1.0, linestyle="-", label="stress")
    # 绘制颜色为紫色、宽度为 2 像素的不连续曲线 y2
    plt.plot(sortinner[:,0],sortinner[:,1], color="orange", linewidth=2.0, linestyle="-", label="circle")
else :
    plt.plot(sortouter[:,0],sortouter[:,1], color="orange", linewidth=2.0, linestyle="-", label="circle")
    plt.plot(outerpoint[:,0],outerpoint[:,1], color="blue", linewidth=1.0, linestyle="-", label="stress")

plt.legend(loc="upper left")
if x==0:
    plt.title(filename+'inside', fontsize=12, color='r')
else :
    plt.title(filename+'outside', fontsize=12, color='r')

if x==1:
    plt.savefig(filename+'outside'+'.jpg')
else :
    plt.savefig(filename +'inside' + '.jpg')
plt.show()
###################


print('hello')#编译用，可以无视