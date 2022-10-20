import random

n1 = int(input("Введите размерность массива X: "))
n2 = int(input("Введите размерность массива R: "))
X=[]
R=[]

def function(n1, X):
    for c in range(n1):
        X.append(round(random.random() * 10 - 5))

function(n1, X)
function(n2, R)
print(X)
print(R)
b=0
for c in range(1, n1):
    for j in range(1, n2):
             if X[c]==R[j]:
                 print(X[c])   
