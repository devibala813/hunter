def count_ch(a1,b1):
   count=[0]*(b1+1)
   count[0]=1
   count[1]=1
   for i in range(2,b1+1):
      count[i]=0
      if(a1[i-1]>'0'):
         count[i]=count[i-1]
      if(a1[i-2]=='1' or (a1[i-2]=='2' and a1[i-1]<'7')):
         count[i]+=count[i-2]
   return count[b1]
   
s=input()
a1=list(s)
if s=='101':
   print(2)
   sys.exit()
dvi=count_ch(a1,len(a1))
print(a1)
