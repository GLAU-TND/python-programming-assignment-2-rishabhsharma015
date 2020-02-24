n=int(input())
b=bin(n)
k=b[2: : ]
s=list(map(str,k.split("0")))
t=max(s)
l=len(t)
print(l)
