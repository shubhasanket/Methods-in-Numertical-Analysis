"""
Crank Nicolson the general case
"""
import sys
import numpy as np
from tabulate import tabulate
import math

class CrankNicolson:
    def __init__(self,l,T,alpha,m,N):
        if m < 3:
            print("m should be >= 3")
            sys.exit()
        if N < 1:
            print("N should be >= 1")
            sys.exit()

        # Step 1
        h = l/m
        k = T/N
        lamda = alpha**2*k/(h**2)
        print("lamda =", lamda)
##        print(lamda)
        # u(0,j) = u1
        u1 = 100
        # u(l,j) = u2
        u2 = 200
        # initialising w (w0)
        w = np.array([u1])
        l1 = [0]
        for i in range(1,m):
            l1.append(i*h)
            w = np.append(w,self.f(i*h))
        w = np.append(w,u2)
        l1.append(l)
        print(w)
        self.w = w
        self.A = []
        self.B = []
        self.createA(lamda,m)
        self.createB(lamda,m)
        self.A = np.array(self.A)
        self.B = np.array(self.B)
        self.A_inv = np.linalg.inv(self.A)
        head = ["x(i)","t(j)","w(i,j)"]
##        print(len(l))
##        print(len(self.w))
        
        for j in range(1,N+1):
            self.t = j*k
            self.w = np.dot(np.dot(self.A_inv,self.B),self.w)
            data = []
            for i in range(len(l1)):
                data.append([l1[i],self.t,self.w[i]])
##            print(data)
##            print("At t =", self.t)
            print(tabulate(data, headers = head, tablefmt = "grid"))
            print()
        

    def createA(self,lamda,m):
        for i in range (m+1):
            self.A.append([])
            if i == 0:
                self.A[-1].append(1)
                self.fill_zeros(m,"A")
            elif 0<i<m:
                self.fill_zeros(i-1,"A")
                self.A[-1].append(-lamda/2)
                self.A[-1].append(1+lamda)
                self.A[-1].append(-lamda/2)
                self.fill_zeros(m-(i-1)-2,"A")
            else: # i == m
                self.fill_zeros(i,"A")
                self.A[-1].append(1)

    def createB(self,lamda,m):
        for i in range (m+1):
            self.B.append([])
            if i == 0:
                self.B[-1].append(1)
                self.fill_zeros(m)
            elif 0<i<m:
                self.fill_zeros(i-1)
                self.B[-1].append(lamda/2)
                self.B[-1].append(1-lamda)
                self.B[-1].append(lamda/2)
                self.fill_zeros(m-(i-1)-2)
            else: # i == m
                self.fill_zeros(i)
                self.B[-1].append(1)

    def fill_zeros(self,m,s = "B"):
        if s == "A":
            for j in range (m):
                self.A[-1].append(0)
        else:
            for j in range (m):
                self.B[-1].append(0)

    # define f(x)
    def f(self,x):
        if 1<=x<=10:
            return 10*(10-x)
        elif 11<=x<=19:
                return 20*(x-10)
##        return math.sin(math.pi*x/2)
        
        

def main():
    a = CrankNicolson(l = 20,T = 20, alpha = 1 ,m = 20,N = 100)
##    a = CrankNicolson(2,0.1,1,4,2)
##    print(a.A)
##    print(a.w)
##    for u in a.B:
##        print(u)
##    print(a.A)
    
main()        
