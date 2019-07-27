s=int(input())
d=list(map(int,input().split()))
for i in range(len(d)):
   if d.count(d[i])==1:
      print(d[i])
      break
