num=int(input())
hii=list(map(int,input().split()[:num]))
count=0
fp=[]
for i in range(0,num+1):
   if(hii.count(i)>1):
      fp.append(i)
if(len(fp)==0):
   print("unique")
ew=sorted(fp)
print(' '.join(map(str,ew)))
