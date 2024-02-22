from Regression import LeastSquaresCurveFitting
import numpy as np

data = [[-1,0,1,2,3,4,5,6],
        [-17.5, 2.5, 4, 3.3, 2.3, 4, 10.5, 24]]
def R(dim, l, c, p = 1):
     y_mean = sum(l[1])/len(l[1])
##     print("mean =", y_mean)
     numerator = 0
     denominator = 0
     for i in range (len(l[0])):
          s = 0
          for j in range (dim):
               s += c[j]*((l[0][i])**(j*p))
          numerator += (s - y_mean)**2
##          print("...............", numerator)
          denominator += (l[1][i] - y_mean)**2
##     print("numerator =", numerator)
##     print("denominator =", denominator)
     return numerator/denominator


data2 = [[0.4,0.8,1.2,2,2.8,3.6,4.8,6.0,8.0],
         [-66.1,-3.77, 1.44, 2.38, 2.20, 2.00, 1.79, 1.64, 1.49]]

def execute(dim):
     l1 = []
     for i in range(len(data2[0])):
          l1.append(1/data2[0][i])
##     print("l1 =", l1)
##     l1 = data2[0]
     l2 = data2[1]

     A = []
     for i in range(dim):
          A.append([])
          for j in range(dim):
               s = 0
               for k in range(len(l1)):
                    s += l1[k]**(i+j)
               A[i].append(s)
##     print("..........",A)

     b = []
     for m in range (dim):
          s = 0
          for n in range (len(l1)):
              s += (l1[n]**m)*l2[n]
          b.append(s)
##     print(b)
##     print(sum(l2))
##     print(A)
     A = np.array(A)
     b = np.array(b)
     x = np.dot(np.linalg.inv(A), b)
     print("x =",x)
     print("R(g) =", R(dim=dim, l=[data2[0],l2], c=x, p=(-1)))

def main():
     print("DATA SET 1")
     print("3rd degree polynomial")
     a = LeastSquaresCurveFitting(data=data, dim=4)
     print("x hat =", a.x_hat)
     print("R(g) =", R(dim=4, l=data, c=a.x_hat))
     a.plot()
     print("4th degree polynomial")     
     b = LeastSquaresCurveFitting(data=data, dim=5)
     print("x hat =", b.x_hat)
     print("R(g) =", R(dim=5, l=data, c=b.x_hat))
     b.plot()
     c = LeastSquaresCurveFitting(data=data, dim=6)
     print("x hat =", c.x_hat)
     print("R(g) =", R(dim=6, l=data, c=c.x_hat))
     c.plot()
     
     print("DATA SET 3")
     print("2nd degree")
     execute(3)
     print("3rd degree")
     execute(4)
     print("4th degree")
     execute(5)
          
main()    
     
##execute(4)
     

