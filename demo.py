num=29
fcount=0
for f in range(1,num+1):
    if(num%f==0):
        fcount+=1
print('pn' if fcount==2 else 'npn')
