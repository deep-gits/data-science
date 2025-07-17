
def perfect(num):
    sum=0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i
    if (sum==num):
        print(num,end=' ')        

N=int(input())
for i in  range(2,N+1):
    perfect(i)
