# a= 7,8
# print(a,b)
# print(type(a))

#a,b,c =9,8,7,8
#print(a,b,c)

#a,b=c=9,8
#print(a)
#print(b)
#print(c)

# a=b,c = 4,2
# print(a,b,c)

#----> swapping of variables
# a = 7
# b = 5
# temp = a
# a=b
# b=temp
# print(a,b)

# temp = is used to replace the a,b values

# Eg:2
# a= a+b #a=12
# b= a-b #b=12-5=7
# c=a-b  #a=12-7=5

# print(a,b)

# a,b=b,a#only in python
# a=a*b #a=35
# b=a/b #b35/7 = 5.0
# a=ab #a=35/5 =7.0
# print(int(a),int(b))

# id function; id()--> it is used to find memory address of the variable
# a = 7
# b = 8
# print(a)
# print(id(b))

#---->keywords
# keywords are reserved words which provides special meaning to
# compiler or interpretor

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# To check if the string is keyword or not

# print(keyword.is keyword("sid"))# false

   #if =8
#print(if)# error coz if is a keyword

# !--->literals
# literals is the constant value assigned to a variable
# A variable is consider  to be constant when it is defines
# in caps

# a=78 # a is variable
# A=78 # A i constant

# hash()-->it creates a hash value for constant datatypes and
# provides error for non contant datatypes
# n1 = 89+7j
# print(hash(n1)

# f1 = [7,8,9]
# print(hash(f1)) # error --> list is non-constant or mutable






#! ----> operators
# operators are symbols which is used to perform various operations
# between  2 or more operands

# arithmatic
# assignment
# Logical
# relation or comparison
# bitwise
# identity
# membership

# todo ---->Arithmatic -->+,-,*,/,%,//,**
#Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c)

# input() --> used to get the runtime input
# eval() -->used to get the runtime values of all datatype
# n1 = eval("Enter the value:")
#print(n1)

a=4
b=2
print(a/b)#is used to get the quotient value
print(a%b)# is used to get the remainder value

# ! // -->floor division

#a=765433
#b=19

#print(a/b)
#print(a/b) # -> the output will be in integer & the output will be
#based on floor value

#! ** -->used for power of a number
# Print(2*-4) # --> 16

# ! assignment --> +-=,//=,**=,&=,|=,%=

#a=8
#a+=2
#print(a)

#a=30
#a-=5
#print()

# ! comparision --> -=,>,<,!=,>=
#a=8
#b=7
#print(a>b) # true

#a=9
#b=5
#print(a==b)

#! bitwise operator --> &,|,^,~,<<,>>
#a=7
#b=4
#print(a&b)

#and
#a b a&b


# 2^4 2^3 2^2 2^1
# 8  4  2  1
# 0  1  1  1 #--> 7
# 0  1  0  0 #--> 4&
#---------------
# 0  1  1  1 # --> 7

# ~ --->
# a= 9876
#print(~a)

# a = 9

# 128 64 32 16 8 4 2 1
#  0  0   0 0  1 0 0 1 #-->  9

#  1  1   1 1  1 0 1 1 0 # --> -10

# 0 0 0 0 1 0 1 0 --> 10

# 1 1 1 1 0 1 -> 1 compliment of 10
           # 1 ->2s compliment
#------------------------
# 1 1 1 1 0 1 1 0 --> -10

# 256 128 64 32 16 8 4 2 1
#  0   0   0  0  0 0 1 0 1 3<
#  0   0   0  1  0 1 0 0 0 --> 40
# 107

# <<,>>
# print (5>>1)
# 16>4


# ! logical --> used to compare the expression
# and  or , not

#a = 6
# print(a is >3 and a is <10)
# print(a>7 or a<30)
# print(not (a>8 and a<10))

# ! Identity operator
# It is used to compare the memory location that the values are stored
# is, is not
#a = 8
#b = 8
#prin(a is b)
#print(a==b)

#a=[1, 2, 3]
#b=[1, 2, 3]
#print(a is not b)

# Membership operator
# in, not in
#11 = [7, 8, 0, 6, 5]
#num =55
#print(num in 11)

#11 = [7, 8, 9, 0, 6, 5]
#num = 55
#print(num not in 11)

#num = 678
#print(8 in num 0 # error

# ! 14 conditional statement
# if, elif, else

#--> c syntax
# if (condition){
#    statement;
#    statement;
#    statement;
#}
#python syntax
# if condition:
#    statement;
#    statement;
#    statement;

# Eg:2
#a = 6
# if a >3:
#print("yes")
#else:
#print("no")

#Eg:3
# if 7>8:
#print("hello")

#print("no")


#Eg:4
#a = 0
#a = none
#a = false
#a =""
#if a :
#print("yes")
#else :
#print("no")

#sum 1
# a number is even or odd
#n=int(input("enter the number:"))
#if n %2==0:
#       print(n, "is even")
#else:
#   print(n,"is odd")

#sum2
# name ,age, nationality
# 18 above,indian
#name=(input("enter your name:"))
#age=int(input("enter your age:"))
#nationality=(input("enter the nationality:"))

#if age >=18 and nationality=="indian":
#    print("eligiblefor vote")
#else:
#    print("not eligible")














































































































































 













      















































