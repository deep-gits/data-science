'''super primr number are the prime number which are on a prime position like 3,5,11'''
All_prime=[]
def Prime(number):
    count=0
    for i in range(2,number//2+1):
        if number%i==0:
            count=1
            break
    if count==0:
        All_prime.append(number)

Super_prime=[]

def super_Prime(number):
    count=0
    for i in range(2,number//2+1):
        if number%i==0:
            count=1
            break
    if count==0:
        Super_prime.append(All_prime[number])

N=int(input())
for i in range(1,N+1):
    Prime(i)
for i in range(2,len(All_prime)):
    super_Prime(i)
print(Super_prime)        




