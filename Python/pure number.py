def even(num):
    if len(num)%2==0:
        return True
    else:
        return False


def check_4_or_5(num):
    status=1
    for i in range(len(num)):
        if num[i]=='4' or num[i]=='5' :
            status=1
        else:
            status =0
    if status==1:
        return True
    else:
        return False

def palindrone(num):
    n1=int(num)
    num=int(num)
    rev =0
    while n1!=0:
        rev=rev*10+n1%10
        n1=n1//10
    if rev==num:
        return True
    else:
        return False

n=input()
if(even(n) and check_4_or_5(n) and palindrone(n)):
    print('pure')
else:
    print('not pure')        
