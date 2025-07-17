n=int(input())
reverse =0
Num=n
while Num!=0:
    reverse= reverse*10 + Num%10
    Num=Num//10
if reverse == n:
    print(n,'is a palindronr')
else:
    print(n,'is not a palindrone')
