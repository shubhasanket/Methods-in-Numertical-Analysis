"""The integration to be evaluated is x^2*ln(x)dx from 1 to 1.5
"""
import numpy as np
l = []
l.append([])
for i in range (20):
##     l.append([])
     l1 = np.linspace(1, 1.5, 2**i)
##     print("......................",l1)
     s = 0
     for j in range (len(l1)):
          if (j == 0) or (j == (len(l1)-1)):
               s += (l1[j]**2)*np.log(l1[j])
          else:
               s += 2*(l1[j]**2)*np.log(l1[j])
     l[0].append(s*(1.5-1)/(2**(i+1)))
##print(l)
##print(len(l[0]))

##for i in range (1, len(l[0])):
##     l.append([])
##     for j in range (1, len(l[0])):
##          if j <= i:
for k in range (1, len(l[0])):
     l.append([])
     for i in range (1, len(l[k-1])):
          s = l[k-1][i] + (1/(4**(k)-1))*(l[k-1][i] - l[k-1][i-1])
          l[k].append(s)
for i in range (len(l)):
     print(i+1, "   ", l[i])
##print(l)
