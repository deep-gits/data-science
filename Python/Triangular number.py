n=int(input())
sum=0
status=0
for i in range(1,n+1):
    sum=sum+i
    if sum==n:
        status=1
        break

if status==1:
    print('yes')
else:
    print('no')