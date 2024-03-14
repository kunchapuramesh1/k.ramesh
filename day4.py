#day4
# ---->while loop
# ---->break using while loop
#Eg:1
#1.) Iterate from 20 to 30 and break the loop in 27
#i=20
#while i<31:
#    if i==27:
#        break
#    print(i)
#    i+=1

#Eg:2
#i=20
#while i<31:
#    print(i)
#    if i==27:
#        break
#    i+=1 
     
    

#Eg:3
#i=20
#while i<31:
#    print(i)
#    i+=1
#    if i==27:
#       break


#Eg:4
#i=20
#while i<31:
#    if i==27:
#        print(i)
#        break
#    i+=1


#! ------>continue using while loop
#Eg:5
#i=20
#while i<31:
#    if i==27:
#        continue
#    print(i)
#    i=i+1

#Eg:6
#while to iterate from 12 to 22
#find the sum of all numbers
#i=12
#sum=0
#while i<23:
#    sum=sum+i
#    i+=1
#print(sum)

#Eg:7
#i=1
#sum=0
#while i<4:
#    sum=sum+i
#    i+=1
#print(sum)

#!Eg:8
# find the average of value from 20 to 25
#i=20
#sum=0
#count=0
#while i<=25:
#    sum=sum+i
#    count+=1
#    i+=1
#print(sum/count)

# ------> nested for loop
#Eg:1
#for row in range(1,10):
#    for col in range(2,90):
#        print(row,col)

#Eg:2
        # * * * *
        # * * * *
        # * * * *
        # * * * *

#rows=int(input("enter the row"))
#cols =int(input("enter the col:"))

#for row in range (rows):
#     for col in range (cols):
#         print("*",end="")
#         print()


#sum=0
#for row in range (5):
#     for col in range(5):
#          sum=sum+1
#          print(sum,end="")
#          print()


#! to print starts in right angled triangle

#Eg:1
#for row in range(0,6):
#     for col in range(0,row+1):
#          print("*",end="")
#     print()

#Eg:2
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

#for row in range (0,6):
#    for col in range(row,6):
#          print("*",end= "")
#     print()

#Eg:3
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

#for row in range(5):
#     for col in range(5):
#          if col==0 or col==5-1 or row==0  or row==5-1:
#               print("*",end=" ")
#          else:
#               print(" ",end=" ")
#     print()

#Eg:4
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

#for row in range (0,5):
#     for col in range (0,6):
#          if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
#               print("*",end=" ")
#          else:
#               print(" ", end=" ")
#     print()

#Eg:5
#  0 1 2 3 4 5 
#0 *
#1 * *
#2 *   *
#3 *     *
#4 *       *
#5 * * * * * * ----> pending


# ! datatypes
# primary

# number -->int,float complex
# string
# boolean
# none

# collection
# list
# tuple
# set
# dictionary

# ? ---> List

# 1.) if the collection of elements are sorrounded by square brackets, it is considerd to be list

#Eg:
  #l1 = [4, 7 , 9.89, "hello", 7+9j,[8,9,0]]

# characterstics of list
#1.) list have to be sorrounded by []
#2.) It is mutable (the elements in the list are changable)
#3.) Every element inside list is indexed
#4.) The element inside list will be ordered format
#5.) It can hold duplicate values
#6.) Its heterogenous

# To access the element in list
#l1= [1,4,1,7,89.7,7.5,"p","i"]
#print(l1)

# --> Indexing
# In the collection data types like list,tuple ,string,the element will be alloted with predefined unique value called index value

# we have 2types of indexing
# positive indexing--> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side

#? ---> positive
#lst1 = [1,4,1,7,89.7,7.5,"p","i"]
#print(lst1[0])
#print(lst1[4])
#print(lst1[20])---> error

# ? Negative indexing
#Lst1 = [1,4,1,7,89.7,7.5,"p","i"]
#print(lst1[-1])
#print(lst1[-5])

# ? ----> Slicing
#lst1 = [ 1,4,1,7,89.7,7.5,"p","i"]
#lst1[start_index:end_index:step]

#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])


#print(lst1[0:7:2]) # Lst1[0:7] --> both are same
#print(lst1[0:7:2])

# trail = int(input())

lst1 = [1,4,1,7,89,7.5,"p","i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4]) 
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

#To insert or add element inside list

# append()
#l1 = [9,8,0,6]
#l1.append("car")
#print(l1)

#n= int(input("enter the number of input:"))
#for i in range(0,n):
#     a,b = list(map(int,input().split()))
#     print(a,b)











           



















#s1="hello world all"

























     
