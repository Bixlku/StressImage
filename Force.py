import  isintriangle

def force(lis,n):
    #集合S中点个数为3时，集合本身即为凸包集
    if n==3:
        return  lis
    else:
        #集合按纵坐标排序，找出y最小的点p0
        lis.sort(key=lambda x: x[1])
        p0=lis[0]
        #除去p0的其余点集合lis_brute
        lis_brute=lis[1:]
        #temp是用来存放集合需要删除的点在lis_brute内的索引，四个点中如果有一个点在其余三个点组成的三角形内部，则该点一定不是凸包上的点
        temp=[]
        #三重循环找到所有这样在三角形内的点
        for i in range(len(lis_brute)-2):
            pi=lis_brute[i]
            #如果索引i已经在temp中，即pi一定不是凸包上的点，跳过这次循环
            if i in temp:
                continue
            for j in range(i+1,len(lis_brute) - 1):
                pj=lis_brute[j]
                #如果索引j已经在temp中，即pj一定不是凸包上的点，跳过这次循环
                if j in temp:
                    continue
                for k in range(j + 1, len(lis_brute)):
                    pk=lis_brute[k]

                    #如果索引k已经在temp中，即pk一定不是凸包上的点，跳过这次循环
                    if k in temp:
                        continue
                    #判断pi是否在pj,pk,p0构成的三角形内
                    (it1,it2,it3)=isintriangle.isin(pi,pj,pk,p0)
                    if it1>=0 and it2>=0 and it3>=0:
                        if i not in temp:
                           temp.append(i)
                    # 判断pj是否在pi,pk,p0构成的三角形内
                    (jt1,jt2,jt3)=isintriangle.isin(pj,pi,pk,p0)
                    if jt1>=0 and jt2>=0 and jt3>=0:

                        if j not in temp:
                           temp.append(j)

                    # 判断pk是否在pj,pi,p0构成的三角形内
                    (kt1, kt2, kt3) = isintriangle.isin(pk, pi, pj, p0)
                    if kt1 >= 0 and kt2 >= 0 and kt3 >= 0:

                        if k not in temp:
                            temp.append(k)
       #listlast是最终选出的凸包集合
        lislast=[]
        for coor in lis_brute:
            loc = [i for i, x in enumerate(lis_brute) if x == coor]
            for x in loc:
                ploc = x
            if ploc not in temp:
                lislast.append(coor)
        #将p0加入凸包集合
        lislast.append(p0)
        return  lislast
