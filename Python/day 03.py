#Practice methods,Classes,functions

'''write a python code that accept string of N eods as input(N>=2)and print Output given below
i/p:GATE EXAM 2025
o/p:GATE
    EXAM
    2025'''

# str=input().split(' ')
# for i in range( len (str)):
#     print('\t',str[i])


'''write python code to print 'N' values , N times using recurson'''
# def Print_recursion(N):
#     if N==0:
#         return
#     print(N1,end=' ')
#     Print_recursion(N-1)   
# N=int(input())
# N1=N
# Print_recursion(N)        

'''Using iteration'''
# N=int(input())
# for i in range(N):
#     print(N,end=' ')


'''Write a python code to print factorial of given number using recursion'''
# def fact_recursion(N):
#     if N==0 or N==1:
#        return 1
#     return N*fact_recursion(N-1)

# N=int(input())
# print(fact_recursion(N))

'''write python code using class and methods such that nput are taken by parent class each single
input and output is printed by child class (Develod multiple inheritence) '''

class A:
     n=0
class B:
     count=0
class C(A,B):
    def Output(self):
        for i in range(1,self.count+1):
            print(self.n,'*',i,'=',self.n*i)

ob=C()
ob.n=int(input())
ob.count=int(input())
ob.Output()