import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
import math


n=int(input("put n number by list: "))

x1=np.random.randint(-180,180,n)
x2=np.random.uniform(-180,180,n)

x1.sort()
x2.sort()

r=math.pi/180

def sin(x,r):
  
  return np.sin(x*r)

Y1 = sin(x1,r)
Y2 = sin(x2,r) 

#Classification of negative and positive angle values

X1=x1[x1<=0]
X1_=x1[x1>0]
X2=x2[x2<=0]
X2_=x2[x2>0]

#Conversion of a List to a Table

lista={"All values of x1": pd.Series(x1), 
       "Negative values x1": pd.Series(X1),
       "Positive values x1": pd.Series(X1_),
       "All values of x2": pd.Series(x2),
       "Negative values x2": pd.Series(X2),
       "Positive values x2": pd.Series(X2_)}

plist=pd.DataFrame(lista)

print(f"######----GENERAL TABLE----###### \n{plist}")

#PLOTS

plt.plot(x1*r,Y1, "-", color="blue", label="N int",linewidth=2)
plt.plot(x2*r,Y2,"-", color="red", label="N uniform", linewidth=2)
plt.title("Differences between int and uniform values")
plt.xlabel("Pi values")
plt.ylabel("Periodic function")
plt.grid()
plt.ylim(-1,1)
plt.legend()
plt.show()
