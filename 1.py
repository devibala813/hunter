no=int(input())
hi=list(map(int,input().split()[:no]))
count=0
fp=[]
for i in range(0,no+1):
   if(hi.count(i)>1):
      fp.append(i)
if(len(fp)==0):
   print("unique")
ew=sorted(fp)
print(' '.join(map(str,ew)))
   
   
      
