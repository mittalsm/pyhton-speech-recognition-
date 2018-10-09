m1=[[1,3,9],[5,6,3],[2,5,8]]
m2=[[1,3,9],[5,6,3],[2,5,8]]
n=3
def sumamat(a,b):
    z=[]
    for i in range (n):
        for j in range (n):
            x=a[i][j]+b[i][j]
            z.append(x)
        return z
 
print(sumamat(m1,m2))
