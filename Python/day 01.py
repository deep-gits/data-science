#methods in pythom




#sum of numbers

# a=int(input("enter the numbers"))
# sum=0
# for i in range(a):
#     value=int(input())
#     sum=sum+value

# print(sum) 

#concatenate the strings

# a=int(input("enter the value"))
# str=" "
# for i in range(a):
#     str=str + input()

# print(str)   


#takes input in one line input(),readline(),map()

# a=input().split()
# sum=0
# for i in range(len(a)):
#     sum=sum+int(a[i])
# print(sum)   


# a=input().split(',')
# sum=0
# for i in range(len(a)):
#     sum=sum+int(a[i])

# print(sum)   


#Length of every word
a=input().split(',')
for i in range(len(a)):
    print(len(a[i]),end=' ')