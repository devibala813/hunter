import sys,string,math
n1=int(input())
l1=list(map(int,input().split()))
l2=[]
for i in range(n1):
   if l1[i]==i:
      l2.append(i)
l=sorted(l2)
if len(l)==0:
   print(-1)
else:
   print(*l)
   
