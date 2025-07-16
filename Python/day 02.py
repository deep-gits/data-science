#Output formating in python



#WAP that accept a string as input and find min and max length of words
# string=input().split(',')
# min=max=len(string[0])
# for i in range(1,len(string)):
#     if len(string[i])<min:
#         min=len(string[i])
#     elif len(string[i])>max:
#         max=len(string[i])

# print(min,max)


# a,b,c,d=input().split(',')
# print(a,b,c,d)
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# e=a*b*c*d
# print(e)

#using map function

# a,b,c,d=map(int,input().split(','))
# e=a*b*c*d
# print(e)


#usinng stdin.readline()
# import sys
# a=sys.stdin.readline(3)
# b=sys.stdin.readline(4)
# c=sys.stdin.readline(2)
# d=sys.stdin.readline(1)
# e=sys.stdin.readline()
# print('a=',a,'b=',b,'c=',c,'d=',d,'e=',e)


#code to seperate even number and odd numbers into lists(list comprehension)

# l1=l2=[]
# N=int(input())
# for i in range(N+1):
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)

# print(l1)
# print(l2)            

# n=int(input())
# x=[i for i in range(n+1) if i%2==0]
# y=[i for i in range(n+2) if i%2!=0]
# print('even list=',x)
# print('odd list=',y)

# n=int(input())
# x=[i for i in range(n+1) if i%2==0]
# y=[i for i in range(n+2) if i not in x]
# print('even list=',x)
# print('odd list=',y)



'''Format specifier in python'''

# a=12
# b=32.4325
# c='student'
# print('a=%-9d,b=%8.3f,c=%s'%(a,b,c))
# print('{0} roll number is {1}and percentage is {2}'.format(c,a,b))

'''HW  #wap that accepts strings as input and 
print their un9icode values of each character in seperate line
sample input : GATE
sample output: G: 71               chr(value)->unicode charactr of given value
               A: 65               chr(character)->unicode value of given character
               T: 84
               E: 69
'''
str=input()
for i in range(len(str)):
    print(str[i],':',ord(str[i]))
    