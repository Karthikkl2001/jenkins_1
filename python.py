num=29
fcount=0
for f in range(1,num+1):
    if(num%f==0):
        fcount+=1
print('primenumber' if fcount==2 else 'not primenumber')

