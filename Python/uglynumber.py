import math
f=[1]

def factors(num):
    for i in range (2,num+1//2):
        if num%i==0:
            f.append(i)
    print(f)

def isprime(n):
    count =0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False 

ugly=[]
def prime_factors(f):
    status=0
    for i in f:
        if isprime(i) and i!=2 and i!=3 
           