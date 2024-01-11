import numpy as np
import array as arr
from scipy.special import kn
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import math
import matplotlib.ticker
from matplotlib.ticker import (MultipleLocator, 
                               FormatStrFormatter, 
                               AutoMinorLocator) 
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()



def cluster(y,x):
    global energyvalue
    global usedlist
    global pixelnumber
    global meanenergy
    global medianenergy
    global maxenergy
    global minenergy
    global trackx
    global tracky
    energydep=[]
    tochecklist=[[y,x]]
    count=0
    sumx=[]
    sumy=[]
    while len(tochecklist)>0:
        y=tochecklist[0][0]
        x=tochecklist[0][1]
        tochecklist.remove([y,x])
        for j in range(y-1,y+2):
            
            if j>255 or j<0:
                continue
            sumy.append(j)
            
            for i in range(x-1,x+2):
                
                if i>255 or i<0:
                    continue
                sumx.append(i)
                #print("i:",i,"j:",j)
                #print("HERE:",energyvalue[j][i])
                if energyvalue[j][i]>0 and str(usedlist).find("[%d, %d]"%(j,i))<0:
                    energydep.append(energyvalue[j][i])
                    count=count+1
                    #print("HERE:",energyvalue[j][i])
                    usedlist.append([j,i])
                    tochecklist.append([j,i])
    #print("energies:",energydep)
    
    pixelnumber.append(count)
    averagex=np.mean(sumx)
    averagey=np.mean(sumy)
    #print("mean x:", averagex, "mean y:", averagey)
    #print("pixel count:", pixelnumber)
    meanenergy.append(np.mean(energydep))
    medianenergy.append(np.median(energydep))
    maxenergy.append(np.max(energydep))
    trackx.append(averagex)
    tracky.append(averagey)
            





#usedlist=np.array([[1,2,3]])
#print(usedlist)
pixelnumber=[]
energyvalue=[[]]
usedlist=[]
meanenergy=[]
medianenergy=[]
maxenergy=[]
minenergy=[]
trackx=[]
tracky=[]
#usedlist.append([1,2])
#usedlist=np.append(usedlist,[[1,2,3]],axis=0)
#print(usedlist)


x=[]
y=[]
linenumber=0
path="/Users/lukecalvin/2023/ELI-NP DATA/ump43_timepixPC/ieap_timepix/20231128/run_03/"
file="28_11_23_run3_shot4_J.csv"
f = open('%s%s'%(path,file),'r')
for line in f.readlines():
    #print(line)
    columns=(line.split(','))
    
    for i in range(len(columns)):
        #print(i)
        energyvalue[linenumber].append(float(columns[i]))
        #print(float(columns[i]))
#        if columns[i] >0 :
#            cluster(i,linenumber,columns,f)
    #print(energyvalue)
    #print("length:",len(energyvalue[linenumber]))
    if linenumber==255:
        break
    energyvalue.append([])
    #print(energyvalue)
    linenumber=linenumber+1
#print(energyvalue)
#print(type(line))
#print(line.split(','))
#print(len(energyvalue))

for y in range(len(energyvalue)):
    for x in range(len(energyvalue[y])):
        if energyvalue[y][x]>0 and str(usedlist).find("[%d, %d]"%(y,x))<0:
            #print(energyvalue[y][x])
            #print("x:",x,"y:",y)
            cluster(y,x)



'''y=3
x=3

energydep=[]
tochecklist=[[y,x]]
tochecklist.append([4,4])
tochecklist.append([5,5])
tochecklist.remove([4,4])
print(tochecklist[0][0])
#print(str(tochecklist))

j=3
i=3
#print("[%d, %d]"%(j,i))
#print(str(tochecklist).find("[%d, %d]"%(j,i)))
for j in range(y-1,y+1):
    for i in range(x-1,x+1):
        if energyvalue[j][i]>0 and usedlist.find("[%d, %d]"%(j,i))<0:
            energydep.append(energyvalue[j][i])
            usedlist.append([j,i])
            tochecklist.append([j,i])'''

for g in range(len(trackx)):
    print("track x position:",trackx[g],'\n',"track y position:",tracky[g],'\n',
          "mean energy deposited:",meanenergy[g],'\n',"median energy deposited:",medianenergy[g],'\n',
          "max energy deposited:",maxenergy[g])

