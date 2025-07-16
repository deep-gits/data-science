'''Devlop python function to calculate sum of squares of individual 
digits of a given number using iterattion'''

# def fun(N):
#     sum=0
#     while N!=0:
#         sum+=(N%10)**2
#         N//=10
#     print(sum)
# Num=int(input("write value"))
# fun(Num)        


'''Develop python function to print prime numbers up to given N value using recursion'''

# def Prime(N):
#     if N<=0:
#        return
#     count=0
#     i=2
#     while i<=N/2:
#        if N%i==0:
#            count=count+1
#            break
#        i=i+1
#     if count==0:
#         print(N)
#         Prime(N-1) 
#     else:
#         Prime(N-1)
# num=int(input())
# Prime(num)              

'''Devlop python function to print absolute differrence 
between the sum of even numbers and sum of odd numbers up to N value using iteration'''
# import math
# def even_odd_difference(N):
#     evensum=oddsum=0
#     for i in range(N+1):
#         if i%2==0:
#             evensum+=i
#         else:
#             oddsum+=i 
#     print(evensum,oddsum,abs(evensum-oddsum))
# N=int(input())
# even_odd_difference(N)              

'''Develop python function to accept the given string as input and
print in the step manner as given below
ip= GATE EXAM 2025
op=GATE
     EXAM
       2025'''

def fun(String):
  for i in range(len(String)):
        print(String[i])
        while i>=0:
            print('\t',end=' ')
            i=i-1
S=input().split()
fun(S)