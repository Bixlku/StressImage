import numpy as np
import pandas as pd


i=3
filename="outerstep"+i.__str__()

f1=open("sortouter.csv",encoding='utf-8')
data1=pd.read_csv(f1,usecols=[0,1],header=None)

data1.insert(data1.shape[1],"", '', True)

f2=open("source/1.无空洞/output/"+filename+".dat",encoding='utf-8')
data2=pd.read_csv(f2,header=None)
data2.insert(data2.shape[1],"", '', True)

f3=open("source/2.新方法/output/"+filename+".dat",encoding='utf-8')
data3=pd.read_csv(f3,header=None)
data3.insert(data3.shape[1],"", '', True)

f4=open("source/3.老方法/output/"+filename+".dat",encoding='utf-8')
data4=pd.read_csv(f4,header=None)
#data4.insert(data4.shape[1],"", '', True)


new_line=["隧道轮廓","","","无空洞","","","新方法","","","老方法",""]
new_line1=["x","y","","xx","yy","","xx","yy","","xx","yy"]
line=pd.DataFrame([new_line])
line1=pd.DataFrame([new_line1])

result=pd.concat([data1,data1],axis=1)
result=pd.concat([data1,data2],axis=1)
result=pd.concat([result,data3],axis=1)
result=pd.concat([result,data4],axis=1)
#result=pd.concat([line,result],axis=0)
result = result.reset_index(drop=True)
result.columns=['0','1','2','3','4','5','6','7','8','9','10']
line.columns=['0','1','2','3','4','5','6','7','8','9','10']
line1.columns=['0','1','2','3','4','5','6','7','8','9','10']
line=line.append(line1)
result=line.append(result)


print(result)

writer = pd.ExcelWriter('my.xlsx')
result.to_excel(writer,float_format='%.5f',index=None,header=None)
writer.save()
