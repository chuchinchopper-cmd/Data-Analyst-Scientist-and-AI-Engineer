#Objective: You will be able to estimate the value of pi using the Monte Carlo Method
import numpy as np
import random

N=int(input("put n int by monte carlo: "))

def piestimation(nosim):

   inside_circle=0

   for _ in range(nosim):
       
       x=np.random.uniform(0,1)
       y=np.random.uniform(0,1)

       if x**2+y**2<=1:

          inside_circle += 1

   piestimate=4*(inside_circle/nosim)
   return piestimate

simulations=N
result= piestimation(simulations)

print(f"The result was: \n{result}")
