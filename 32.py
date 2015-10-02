A=[1,2,3,2,1]
m=0
k=0
for i in range (len(A)):
    if A[i]>m:
        m=A[i]
        k=i 
print(m,k)