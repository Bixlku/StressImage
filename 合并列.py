import numpy as np
import pandas as pd


for i in range(3,9):

    filename="innerstep"+i.__str__()
    filename2="InnerPoint"

    f1=open("InnerPoint.csv",encoding='utf-8')
    data1=pd.read_csv(f1,usecols=[0,1],header=None)
    data1.insert(data1.shape[1],"", '', True)

    f2=open("source/1.无空洞/output/"+filename+".csv",encoding='utf-8')
    data2=pd.read_csv(f2,header=None)
    data2.insert(data2.shape[1],"", '', True)

    f3=open("source/2.新方法/output/"+filename+".csv",encoding='utf-8')
    data3=pd.read_csv(f3,header=None)
    data3.insert(data3.shape[1],"", '', True)

    f4=open("source/3.老方法/output/"+filename+".csv",encoding='utf-8')
    data4=pd.read_csv(f4,header=None)
    data4.insert(data4.shape[1],"", '', True)


    sha3 = open( filename2 + "3.csv", encoding='utf-8')
    data5 = pd.read_csv(sha3, header=None)
    data5.insert(data5.shape[1], "", '', True)

    sha6 = open(filename2 + "6.csv", encoding='utf-8')
    data6 = pd.read_csv(sha6, header=None)
    data6.insert(data6.shape[1], "", '', True)

    sha9 = open(filename2 + "9.csv", encoding='utf-8')
    data7 = pd.read_csv(sha9, header=None)
    data7.insert(data7.shape[1], "", '', True)

    sha12 = open(filename2 + "12.csv", encoding='utf-8')
    data8 = pd.read_csv(sha12, header=None)



    new_line=["隧道轮廓","","","无空洞","","","新方法","","","老方法","","","同心圆3","","","同心圆6","","","同心圆9","","","同心圆12",""]
    new_line1=["x","y","","xx","yy","","xx","yy","","xx","yy","","xx","yy","","xx","yy","","xx","yy","","xx","yy"]
    line=pd.DataFrame([new_line])
    line1=pd.DataFrame([new_line1])

    result=pd.concat([data1,data1],axis=1)
    result=pd.concat([data1,data2],axis=1)
    result=pd.concat([result,data3],axis=1)
    result=pd.concat([result,data4],axis=1)
    result = pd.concat([result, data5], axis=1)
    result = pd.concat([result, data6], axis=1)
    result = pd.concat([result, data7], axis=1)
    result = pd.concat([result, data8], axis=1)
    #result=pd.concat([line,result],axis=0)
    result = result.reset_index(drop=True)
    result.columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
    line.columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
    line1.columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
    line=line.append(line1)
    result=line.append(result)


    print(result)

    writer = pd.ExcelWriter(filename+'.xlsx')
    result.to_excel(writer,float_format='%.5f',index=None,header=None)
    writer.save()
