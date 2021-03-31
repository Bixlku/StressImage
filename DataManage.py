import numpy as np


filename="step3"


fin = open("source/1.无空洞/"+filename+'.dat', 'r')
a = fin.readlines()
fout = open("source/1.无空洞/"+filename+'1.dat', 'w')
b = ''.join(a[8:200])
fout.write(b)

