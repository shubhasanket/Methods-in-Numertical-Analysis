""" Implementing the RK order 4 method
"""
from tabulate import tabulate
x = 0
y = 0
# One has to define the function
def f(x,y): # here f = dy/dx
    
    return (-0.01*y)

a,b = eval(input("Enter the endpoints a and b: "))
y_in = eval(input("Set the initial value of y: "))
N = eval(input("Enter the number of points for which the value should be calculated (N): "))
d = {}

# Step 1
h = (b-a)/N
t = a
w = y_in

d[a] = round(w,5)

#Step 2
for i in range (1, N+1):
    # Step 3
    k1 = h*f(t,w)
    k2 = h*f(t + h/2, w + k1/2)
    k3 = h*f(t + h/2, w + k2/2)
    k4 = h*f(t + h, w + k3)

    # Step 4
    w += (k1 + 2*k2 + 2*k3 + k4)/6
    t = a + i*h

    # Step 5
    d[t] = round(w,5)

# Step 6
l = [[x,y] for (x,y) in d.items()]
##for i in d:
##    l.append([i,d[i]])

head = ["x","y"]
print(tabulate(l, headers = head, tablefmt = "grid"))
##print(l)


