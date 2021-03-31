def isin(pi,pj,pk,p0):
    x1 = float(p0[0])
    x2 = float(pj[0])
    x3 = float(pi[0])
    x4 = float(pk[0])
    y1 = float(p0[1])
    y2 = float(pj[1])
    y3 = float(pi[1])
    y4 = float(pk[1])

    k_j0=0
    b_j0=0
    k_k0=0
    b_k0=0
    k_jk=0
    b_jk=0
    perpendicular1=False
    perpendicular2 = False
    perpendicular3 = False
    #pj,p0组成的直线，看pi,pk是否位于直线同一侧

    if x2 - x1 == 0:
    #pj,p0组成直线垂直于X轴时
        t1=(x3-x2)*(x4-x2)
        perpendicular1=True
    else:
        k_j0 = (y2 - y1) / (x2 - x1)
        b_j0 = y1 - k_j0 * x1
        t1 = (k_j0 * x3 - y3 + b_j0) * (k_j0 * x4 - y4 + b_j0)

    #pk,p0组成的直线，看pi,pj是否位于直线同一侧

    if x4 - x1 == 0:
    #pk,p0组成直线垂直于X轴时
        t2=(x3-x1)*(x2-x1)
        perpendicular2=True
    else:
        k_k0 = (y4 - y1) / (x4 - x1)
        b_k0 = y1 - k_k0 * x1
        t2 = (k_k0 * x3 - y3 + b_k0) * (k_k0 * x2 - y2 + b_k0)

    # pj,pk组成的直线，看pi,p0是否位于直线同一侧

    if x4 - x2 == 0:
    # pj,pk组成直线垂直于X轴时
        t3=(x3-x2)*(x1-x2)
        perpendicular3 = True
    else:
        k_jk = (y4 - y2) / (x4 - x2)
        b_jk = y2 - k_jk * x2
        t3 = (k_jk * x3 - y3 + b_jk) * (k_jk * x1 - y1 + b_jk)
    #如果pk，p0,pj，三点位于同一直线时，不能将点删除
    if (k_j0 * x4 - y4 + b_j0)==0 and (k_k0 * x2 - y2 + b_k0)==0 and  (k_jk * x1 - y1 + b_jk)==0 :
          t1=-1
    #如果pk，p0,pj，三点位于同一直线时且垂直于X轴，不能将点删除
    if perpendicular1 and perpendicular2 and perpendicular3:
          t1=-1

    return t1,t2,t3
