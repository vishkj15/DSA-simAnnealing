import timeit
start=timeit.default_timer()
from os import system
import math
import random
import matplotlib.pyplot as plt
INF = 100000000
f=open("eil51.txt","r")
a=[]
l=f.read()
a=l.split()
x=[]
cor=[]
k=0
for i in range(0,len(a)):
	if(k==3):
		cor.append(x)
		k=1
		x=[]
		x.append(float(a[i]))
	else:
		x.append(float(a[i]))
		k+=1
cor.append(x)
dismat=[]
dismat.append(0)
for i in range(0,len(cor)):
	dista=[]
	dista.append(0)
	for j in range(0,len(cor)):
		if i==j:
			dista.append(INF)
		else:
			dist=round((((cor[i][1]-cor[j][1])**2)+((cor[i][2]-cor[j][2])**2))**0.5,4)
			dista.append(dist)
	dismat.append(dista)
n1=len(cor)
path=[]
for i in range(1,n1+1):
   	path.append(i)
print(path)
print(dismat)

def shuffle1(path):
        upper=len(path)
        lower=1
        no1=random.randint(0,n1-1)
        no2=random.randint(0,n1-1)
        temp=path[no1]
        path[no1]=path[no2]
        path[no2]=temp
def fitness(path):
        dis=0
        for i in range(n1-1):
                dis=dis+dismat[path[i]][path[i+1]]
                fit=1/dis
        return fit

for i in range(n1):
        shuffle1(path)
def two_opt(route):
     best1 = route
     improved = True
     while (improved):
          improved = False
          for q in range(1, len(route)-2):
                  for e in range(q+1,len(route)):
                          if e-q==1: continue # changes nothing, skip then
                          new_route = route[:]
                          new_route[q:e] = route[e-1:q-1:-1] # this is the 2woptSwap
                          if fitness(new_route)>fitness(best1):
                                  best1 = new_route
                                  improved = True
                                  route = best1
     return best1
def simulatedannealing(path):          
	       
        temperature=float(input("Enter the temperature: "))
        print("\n")
        n=int(input("Enter the no of iterations:"))
        coolingRate = 0.9999
        absoluteTemperature = 0.00001
        currpath=path
        bestpath=path
        bestfit=fitness(path)

        while(temperature>absoluteTemperature):
                for i in range(n):
                        r1=random.randint(int(n1/20),int(n1/10))
   	  
                        oldpath=currpath.copy()
                        oldfit=fitness(oldpath)
                        for i in range(r1):
                                shuffle1(currpath)
                                newfit=fitness(currpath)
                                if(newfit>bestfit):
                                        bestpath=currpath.copy()
                                        bestfit=newfit
                                if(newfit<oldfit):
                                        r2=random.random()
                                        dif=(newfit-oldfit)
                                        v=((-1)*dif)/temperature
                                        p=math.exp(v)
                                        if(r2<p):
                                                currpath=oldpath.copy()
									
								
                        temperature=temperature*coolingRate
        return bestpath
        
			

bpath=simulatedannealing(path)
tbpath=two_opt(bpath)
print("The best path is")
print(tbpath)
di=1/fitness(tbpath)
print("distance covered is",di)
stop=timeit.default_timer()
print('Time:',stop - start)
path2=tbpath
xp=[]
yp=[]
for i in range(len(path2)):
		xp.append(cor[path2[i]-1][1])
		yp.append(cor[path2[i]-1][2])
xp.append(cor[path2[1]-1][1])
yp.append(cor[path2[1]-1][2])
plt.plot(xp,yp,ls="--",marker='o')
plt.show()


