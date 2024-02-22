import numpy as np

def det(n,lam,A):
    return np.linalg.det(lam * np.identity(n) - A)

def C(n):
    C = []
    for i in range(1, n):
        C.append([])
        for j in range(n-1,0,-1):
            C[-1].append(i**j)

    return np.array(C)

def D(n,A):
    D = []
    D0 = det(n,0,A)
    for i in range(1,n):
        D.append(det(n,i,A) - D0 - i**n)

    return np.array(D)

def main():
    A = np.array([[1, 0, -1], [0, -2, -3], [4, 5, 0]])
    n = np.shape(A)[0]
    c = C(n)
##    print(c)
    d = D(n,A)
##    print(d)
    P = np.dot(np.linalg.inv(c),d)
##    print(P)
    P = np.append(P,det(n,0,A))
##    print(P)
    P = np.insert(P,0,1)
    print(P)

if __name__ == "__main__":
    main()
