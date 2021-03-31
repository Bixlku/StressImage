import numpy as np
import CircleCenter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import graham_scan
from functools import reduce
import operator
import math
import InsideOrOutside

for i in range(3,9):
    #i=6
    filename = 'step'+i.__str__()

    start = 8
    end = 200
    r=5.65
    fin = open("source/1.无空洞/"+filename+'.dat', 'r')
    a = fin.readlines()
    fout = open("source/1.无空洞/"+filename+'1.dat', 'w')
    b = ''.join(a[start:end])
    fout.write(b)

    pt = np.loadtxt("source/1.无空洞/"+filename+'1.dat', skiprows=0,delimiter=" ",usecols=(1,2,3)) #numpy
    pts = np.loadtxt("source/1.无空洞/"+filename+'1.dat', skiprows=0,delimiter=" ",usecols=(1,2)) #numpy
    x=0        #x=0则是内部，x=1则是外部
    pt[:,2]= pt[:,2]/1000000

    points = []

    for i in range(0,end-start):
        point=[pt[i,0],pt[i,1]]
        points.append(point)

    xmax = np.max(pt, axis=0)[0]
    xmin = np.min(pt, axis=0)[0]
    ymax = np.max(pt, axis=0)[1]
    ymin = np.min(pt, axis=0)[1]
    Center=[(xmax+xmin)/2,(ymax+ymin)/2]

    results=InsideOrOutside.InsideOrOutside(points, Center,r)
    ##此时results代表外围的点
    #results=results.tolist()

    outernum=[]
    innernum = list(range(0,end-start))

    for pr in results :
        outernum.append(pr[1])
        innernum.remove(pr[1])


    # 从pt(也就是源列表)中得到innernum/outernum对应点的坐标和长度，将其放入outer和inner中，并分别输出为outer.csv和inner.csv
    outer = np.array([pt[outernum[0]]])
    count = range(1,len(outernum))
    for i in count:
        outer= np.append(outer,[pt[outernum[i]]],axis=0)

    inner = np.array([pt[innernum[0]]])
    count = range(1,len(innernum))
    for i in count:
        inner= np.append(inner,[pt[innernum[i]]],axis=0)

    np.savetxt('outer.csv',outer,fmt='%f',delimiter=',')
    np.savetxt('inner.csv',inner,fmt='%f',delimiter=',')

    '''
    temp=inner[0]
    temp1=inner[1]
    outer=np.r_[[temp],outer]
    outer = np.r_[[temp1], outer]
    inner=np.delete(inner,0,axis=0)
    inner = np.delete(inner, 0, axis=0)
    '''

    #####################   对outer/inner进行有序排序，排序从第一象限开始，逆时针旋转，得到的为sortinner和sortouter

    InnerPoint=inner
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), InnerPoint),
                       [len(InnerPoint)] * 2))
    arry = sorted(InnerPoint, key=lambda coord: (-135 - math.degrees(
        math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)
    InnerPoint = np.array(arry)

    OuterPoint = outer
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), OuterPoint),
                       [len(OuterPoint)] * 2))
    arry = sorted(OuterPoint, key=lambda coord: (-135 - math.degrees(
        math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)
    OuterPoint = np.array(arry)

    '''
    temp=InnerPoint[0]
    InnerPoint= np.r_[InnerPoint,[temp] ]
    temp = OuterPoint[0]
    OuterPoint = np.r_[OuterPoint, [temp]]
    #这里的OuterPoint/InnerPoint指的是存有内部和外部元数据的点
    '''




    OuterInDraw = np.empty([len(outer), 2])
    InnerInDraw = np.empty([len(inner), 2])
    count = np.arange(len(outer))
    for i in count:
        OuterInDraw[i]=CircleCenter.CircleCenter(Center,OuterPoint[i][2],[OuterPoint[i][0],OuterPoint[i][1]])

    count = np.arange(len(inner))
    for i in count:
        InnerInDraw[i]=CircleCenter.CircleCenter(Center,InnerPoint[i][2],[InnerPoint[i][0],InnerPoint[i][1]])
    OuterInDraw = np.append(OuterInDraw, [OuterInDraw[0]], axis=0)
    InnerInDraw = np.append(InnerInDraw, [InnerInDraw[0]], axis=0)
    OuterPoint = np.append(OuterPoint, [OuterPoint[0]], axis=0)
    InnerPoint = np.append(InnerPoint, [InnerPoint[0]], axis=0)


    '''
    for i in count:
        OuterInDraw[i] = CircleCenter.CircleCenter(OuterPoint[i], OuterPoint[i + 1], OuterPoint[i + 2])
    
    OuterInDraw[len(outer) - 2] = CircleCenter.CircleCenter(OuterPoint[len(outer) - 2],
                                                              OuterPoint[len(outer) - 1], OuterPoint[0])
    OuterInDraw[len(outer) - 1] = CircleCenter.CircleCenter(OuterPoint[len(outer) - 1], OuterPoint[0], OuterPoint[1])
    
    
    count = np.arange(len(inner) - 2)
    for i in count:
        InnerInDraw[i] = CircleCenter.CircleCenter(InnerPoint[i], InnerPoint[i + 1], InnerPoint[i + 2])
    
    InnerInDraw[len(inner) - 2] = CircleCenter.CircleCenter(InnerPoint[len(inner) - 2],
                                                              InnerPoint[len(inner) - 1], InnerPoint[0])
    InnerInDraw[len(inner) - 1] = CircleCenter.CircleCenter(InnerPoint[len(inner) - 1], InnerPoint[0], InnerPoint[1])
    point1=CircleCenter.CircleCenter(InnerPoint[len(inner) - 1], InnerPoint[0], InnerPoint[1])
    point2=CircleCenter.CircleCenter(InnerPoint[len(inner) - 2],InnerPoint[len(inner) - 1], InnerPoint[0])
    cs=23
    point3=CircleCenter.CircleCenter(InnerPoint[cs],InnerPoint[cs+1], InnerPoint[cs+2])
    
    
    OuterInDraw = np.append(OuterInDraw, [OuterInDraw[0]], axis=0)
    InnerInDraw = np.append(InnerInDraw, [InnerInDraw[0]], axis=0)
    OuterPoint = np.append(OuterPoint, [OuterPoint[0]], axis=0)
    InnerPoint = np.append(InnerPoint, [InnerPoint[0]], axis=0)
    '''




    #plt.plot(OuterPoint[:,0],OuterPoint[:,1], color="blue", linewidth=1.0, linestyle="-", label="stress")

    #plt.show()

    ################## 绘图
    plt.xlabel("X")
    plt.ylabel("Y")

    # 绘制颜色为蓝色、宽度为 1 像素的连续曲线 y1
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    np.savetxt("source/1.无空洞/output/inner"+filename+'.csv',InnerInDraw,fmt='%f',delimiter=',')
    np.savetxt("source/1.无空洞/output/outer"+filename+'.csv',OuterInDraw,fmt='%f',delimiter=',')
    np.savetxt("source/1.无空洞/output/sortouter"+filename+'.csv',OuterPoint,fmt='%f',delimiter=',')
    np.savetxt("source/1.无空洞/output/sortinner"+filename+'.csv',InnerPoint,fmt='%f',delimiter=',')





    if x==0 :

        plt.plot(InnerInDraw[:,0],InnerInDraw[:,1], color="blue", linewidth=1.0, linestyle="-", label="stress")
        # 绘制颜色为紫色、宽度为 2 像素的不连续曲线 y2
        plt.plot(InnerPoint[:,0],InnerPoint[:,1], color="orange", linewidth=2.0, linestyle="-", label="circle")
    else :
        plt.plot(OuterPoint[:,0],OuterPoint[:,1], color="orange", linewidth=2.0, linestyle="-", label="circle")
        #plt.plot(OuterInDraw[:,0],OuterInDraw[:,1], color="blue", linewidth=1.0, linestyle="-", label="stress")
        plt.plot(OuterInDraw[:, 0], OuterInDraw[:, 1], color="blue", linewidth=1.0, linestyle="-", label="stress")

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


'''
    #将outer和inner根据x坐标从大到小排列
    outer=outer[np.argsort(outer[:,0])]
    inner=inner[np.argsort(inner[:,0])]
    sortouter=np.empty([len(outernum),3])
    sortinner=np.empty([len(innernum),3])

    #筛选排序
    count =np.arange(len(outernum))
    t=0
    s=0
    for i in count :
        if outer[i][1] >= outer[0][1]:
            sortouter[t]=outer[i]
            t=t+1
        else :
            s = s + 1
            sortouter[len(outernum)-s]=outer[i]

    outerpoint=np.empty([len(outernum),2])
    #np.savetxt('sortouter.csv',sortouter,fmt='%f',delimiter=',')

    count =np.arange(len(innernum))
    t=0
    s=0
    for i in count :
        if inner[i][1] >= inner[0][1]:
            sortinner[t]=inner[i]
            t=t+1
        else :
            s = s + 1
            sortinner[len(innernum)-s]=inner[i]

    innerpoint=np.empty([len(innernum),2])
    #########################
'''
'''
    ###############  输出outside和inside点对应的应力图像的点
    count =np.arange(len(outernum)-2)
    for i in count :
        outerpoint[i]=CircleCenter.CircleCenter(sortouter[i],sortouter[i+1],sortouter[i+2])

    outerpoint[len(outernum)-2]=CircleCenter.CircleCenter(sortouter[len(outernum)-2],sortouter[len(outernum)-1],sortouter[0])
    outerpoint[len(outernum)-1]=CircleCenter.CircleCenter(sortouter[len(outernum)-1],sortouter[0],sortouter[1])


    count =np.arange(len(innernum)-2)
    for i in count :
        innerpoint[i]=CircleCenter.CircleCenter(sortinner[i],sortinner[i+1],sortinner[i+2])

    innerpoint[len(innernum)-2]=CircleCenter.CircleCenter(sortinner[len(innernum)-2],sortinner[len(innernum)-1],sortinner[0])
    innerpoint[len(innernum)-1]=CircleCenter.CircleCenter(sortinner[len(innernum)-1],sortinner[0],sortinner[1])

    outerpoint=np.append(outerpoint,[outerpoint[0]],axis=0)
    innerpoint=np.append(innerpoint,[innerpoint[0]],axis=0)
    sortouter=np.append(sortouter,[sortouter[0]],axis=0)
    sortinner=np.append(sortinner,[sortinner[0]],axis=0)

    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), innerpoint.tolist()),
                       [len(innerpoint.tolist())] * 2))
    arry = sorted(innerpoint.tolist(), key=lambda coord: (-135 - math.degrees(
        math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)
    innerpoint = np.array(arry)
    #################



    ################## 绘图
    plt.xlabel("X")
    plt.ylabel("Y")

    # 绘制颜色为蓝色、宽度为 1 像素的连续曲线 y1
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    np.savetxt("source/1.无空洞/output/inner"+filename+'.csv',innerpoint,fmt='%f',delimiter=',')
    np.savetxt("source/1.无空洞/output/outer"+filename+'.csv',outerpoint,fmt='%f',delimiter=',')
    np.savetxt("source/1.无空洞/output/sortinner"+filename+'.csv',sortinner,fmt='%f',delimiter=',')
    np.savetxt("source/1.无空洞/output/sortouter"+filename+'.csv',sortouter,fmt='%f',delimiter=',')

    plt.scatter(sortinner[:,0],sortinner[:,1], color="blue", label="stress")
    #plt.scatter(outerpoint[:,0],outerpoint[:,1], color="blue",  label="stress")

    plt.show()

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
    '''