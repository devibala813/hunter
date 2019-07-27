s1=int(input())
d1=list(map(int,input().split()))
flags=1
for i in range(len(d1)):
   if d1.count(d1[i])>1:
      print(d1[i])
      flags=0
      break
if flags==1:
   print('unique')
