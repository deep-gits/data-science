num=input()
power_value =len(num)
n=int(num)
num=int(num)
sum=0
while n!=0:
    sum=sum+(n%10)**power_value
    n=n//10
if (sum==num):
    print("true")   
else:
    print("false")