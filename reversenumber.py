l=[]
n=54321
r=0
while n!=0:
    r=r*10
    r=r+int(n%10)
    n=int(n/10)
print(r)
