import sys
import numpy as np

# getting the matrix as input from the console
n = int(input())

# creating the augmented matrix for our equations
a = np.zeros((n,n+1)) 
# creating a list of size n for our solutions 
x = np.zeros(n)


# scan the coefficients as inputs (vector a:nxn)
for i in range(n):
    str = input().split()
    for j in range(len(str)):
        a[i,j] = float(str[j])


# scan the last line which is vector b:nx1
str = input().split()
for j in range(len(str)):
    a[j,n] = float(str[j])

print('\nInput matrix:')
print(a)


# finding the row echelon form of the matrix
for i in range(n):
    pivot = a[i,i]
    for j in range(i + 1, n):
        a[j,:] = a[j,:] - (a[j,i]/pivot) * a[i,:]
    
    print(a)

print('\nEchelon form of the matrix:')
print(a)


# handling exceptions 
if a[n-1,n] != 0 and a[n-1][n-1] == 0:
    sys.exit('This matrix has no answer :(')
elif a[n-1,n] == 0 and a[n-1][n-1] == 0:
    sys.exit('This matrix has infinity number of solutions :)')


# row reduction
for i in range(n - 1, 0, -1):
    pivot = a[i,i]
    for j in range(i - 1, -1, -1):
        a[j,:] = a[j,:] - (a[j,i]/pivot) * a[i,:]

    a[i,n] = a[i, n] / a[i,i]
    a[i,i] = 1


# first row -> pivot pos := 1
a[0, n] = a[0, n] / a[0,0]
a[0,0] = 1


print('Row reduction algorithm applied to the matrix:')
print(a)


print('Final solution:')
x = a[:,n]
print(x)
