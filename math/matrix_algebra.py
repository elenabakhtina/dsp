# Matrix Algebra

import numpy as np
from numpy import linalg as LA
import datetime

def AddTwoMatrices(X,Y,Xdim,Ydim):
    print("First matrix:"); print(X)
    print("Second matrix:"); print(Y)
    if Xdim == Ydim:
        print("The result of addition:")
        print(X+Y)
    else:
        print("An operation of matrix addition is defined only for matrices of the same dimension.")
        print("Result: NOT DEFINED")

def SubtractTwoMatrices(X,Y,Xdim,Ydim):
    print("First matrix:"); print(X)
    print("Second matrix:"); print(Y)
    if Xdim == Ydim:
        print("The result of subtraction:")
        print(X-Y)
    else:
        print("An operation of matrix subtraction is defined only for matrices of the same dimension.")
        print("Result: NOT DEFINED")

def MultiplyTwoMatrices(X,Y,Xdim,Ydim):
    print("First matrix:"); print(X)
    print("Second matrix:"); print(Y)
    if Xdim[1] == Ydim[0]:
        print("The result of multiplication:")
        print(X.dot(Y))
    else:
        print("An operation of matrix multiplication is defined only for matrices")
        print("when the number of columns in the 1st one equals the number of rows in the 2nd one.")
        print("Result: NOT DEFINED")

print("-"*10)
print(datetime.datetime.now())  # to smake sure I see the latest results
print("-"*10)
A = np.array([[1,2,3],[2,7,4]])
print("Matrix A:")
print(A)

B = np.array([[1,-1],[0,1]])
print("Matrix B:")
print(B)

C = np.array([[5,-1],[9,1],[6,0]])
print("Matrix C:")
print(C)

D = np.array([[3,-2,-1],[1,2,3]])
print("Matrix D:")
print(D)

u = np.array([[6,2,-3,5]])
print("Vector u:")
print(u)

v = np.array([[3,5,-1,4]])
print("Vector v:")
print(v)

w = np.array([[1],[8],[0],[5]])
print("Vector w:")
print(w)

print("-- 1. Matrix Dimensions")
print("A:", A.shape) #(2,3)
print("B:", B.shape) #(2,2)
print("C:", C.shape) #(3,2)
print("D:", D.shape) #(2,3)
print("u:", u.shape) #(1,4)
print("v:", v.shape) #(1,4)
print("w:", w.shape) #(4,1)

print("-- 2. Vector Operations")
u_vector = np.array([6,2,-3,5])
v_vector = np.array([3,5,-1,4])
print("u_vector + v_vector:", u_vector + v_vector) #[ 9  7 -4  9]
print("u_vector - v_vector:", u_vector - v_vector) #[ 3 -3 -2  1]
a = 6
print("a = ",a,", a * u_vector:", a * u_vector) #[ 36  12 -18  30]
print("u_vector * v_vector:", u_vector @ v_vector) # 51
print("||u_vector||:",LA.norm(u_vector)) # 8.60232526704
#why did I have to import a particular library from numpy (linalg) when I've already imported the whole numpy?
# why np.norm(u) didn't work?

print("-- 3. Matrix Operations")
print("- 3.1 A + C")
AddTwoMatrices(A,C,A.shape,C.shape)
# Not defined

print("- 3.2 A - C_transpose")
Ct = C.T
SubtractTwoMatrices(A,Ct,A.shape,Ct.shape)
# [[-4 -7 -3]
#  [ 3  6  4]]

print("- 3.3 C_transpose + 3*D")
AddTwoMatrices(Ct,3*D,Ct.shape,D.shape)
# [[14  3  3]
#  [ 2  7  9]]

print("- 3.4 B * A")
MultiplyTwoMatrices(B,A,B.shape,A.shape)
# [[-1 -5 -1]
#  [ 2  7  4]]

print("- 3.5 B * A_transpose")
At = A.T
MultiplyTwoMatrices(B,At,B.shape,At.shape)
# Not defined

print("-- Optional")
print("- 3.6 B * C")
MultiplyTwoMatrices(B,C,B.shape,C.shape)
# Not defined

print("- 3.7 C * B")
MultiplyTwoMatrices(C,B,C.shape,B.shape)
# [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]

print("3.8 B^4:")
B_square = B.dot(B)
print(B_square.dot(B_square))
# [[ 1 -4]
# [ 0  1]]

print("- 3.9 A * A_transpose")
At = A.T
MultiplyTwoMatrices(A,At,A.shape,At.shape)
# [[14 28]
#  [28 69]]

print("- 3.10 D_transpose * D") #
Dt = D.T
MultiplyTwoMatrices(Dt,D,Dt.shape,D.shape)
# [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]

