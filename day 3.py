#day 3
# ! Eg:3
#? take a values of length and breadth of a
# ? from user and check if it is square or not.
#length =int(input(" enter the length:"))
#breadth = int(input(" enter the breadth:"))
#if length==breadth:
#    print("this is square")
#else:
#    print ("this is not square")


# Eg:4
# python progrm to check whether the
#given integer is a multiple of both 5 and 7
#n= int(input("enter the number:"))
#if n%5==0 and n%7==0:
#    print("yes")
#else:
#    print("no")


# ! Eg:5
#write a program to accept the cost price of a bike and display the
#road tax to be paid
#according to thefollowing criteria;

#    cost price(in Rs)                Tax
#    >100000                          15%+discount 6%
#    <100000                          5%

#price =int(input(" enter the bike value:"))
#amount =0
#if price>=100000:
#    discount = price*(6/100)
#    value = price-discount
#    tax = value*(15/100)
#    total =(value+tax)
#else:
#    tax = price*(5/100)
#    total = price+tax
#print("the onroad cost of bike is:",total)

# ! -------> if elif else
# Eg:1
#a = 7
#b = 9
#c = 0
#if a>b and a>c:
#    print(" a is greater")
#elif b>a and b>c:
#    print("b is greater")
#elif c>a and c>b:
#    print("c is greater")

# Eg :2
# a school has following rules for grading system :
#a.Below 25 -F
#b.25 to 45 -E
#c.45 to 50 -D
#d.50 to 60 -C
#e.60 to 80 -B
#f.above 80 -a
#ask user to enter marks and print the corresonding grade.

#mark = int(input("enter mark:"))
#if mark>=80 and mark<=100:
#    print("A")
#elif mark>=60 and mark<80:
#    prinr("B")
#elif mark>=40 and mark<50:
#    print("C")
#elif mark>=40 and mark<50:
#    print("D")
#else:
#    print("fail")


# ! --> short hand if else
#Eg :1
#a = 90
#b =60
#if a>b:
#    print("A")
#else:
#    print("B")


#? --> using short hand if else
# * rules
#1.) statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) always it have to end with else

#print ("A") if a>b else print ("B")

# ! code to check the given char is vowel or consonent
#char = input ("Enter the char:")
#if char =="a" or char =="e" or char =="i" or char =="o" or char=="u":
#  print("is vowel")
#else:
#  print("is consonent")

# ? or

#str1 ="aeiouAEIOU"
#if char in str1:
 #   print("vowel")
#else:
 #   print("consonent")


# ! shorthand if else
#char = input("Enter the char: ")
#str1 = "aeiouAEIOU"
#print("vowels") if char in str1 else print("consonent")

# ! -----> elif ladder using short hand if else
# Eg:1
# ? fin greatest among 3 variables using short hand if else
#b = 5
#c = 9

#print ("A is greater") if a >b and a>c else print("B is greater ") if b>a and b>c else print("C is greater")


# ! ------------> looping
# looping can be implemented using
# for loop
# while loop

#--> for loop
# ? for loop is used for iteration,if we know the number of times the loop have to run
# ? it is used iterate the iterables eg(string,list,tuple,etc...)

# todo --> syntax for loop

# for syntax in c
#for(i=0,i<10;i++){
#    printf("hello");
#}

# ! for syntax in python
# for userdefined_variable in range(start,end,step): default setp value is 1
#  statement
#  statement
#  statement

# ? Eg:1
# To print the value from 1 to 10 using for loop

#for i in range(0,10): #(n ,n-1)
#    print(i)
#    print("hello")

#Eg:2
#for value in range (23, 50, 2):
#   print(value)

# for value in range (1,50,3):
#  print(value)

#Eg:3
# for decrement the values
#for val in range (10,2,-1):
#    print(val)

# ? Eg: 4
# ! print the output of 7th multipliction table from 21 to 40
#for val in range (1,10+1,):
#    print ('20','x',val,'=',val*20)--> method 1

# -->method 2
#    ans="7x{}={}"
#    print (ans.format(val,val*7))

# -->method 3
#for val in range(1,10+1):
#    print(f"7 x {val}={val*7}")

# Eg:5
#break statement --> which is used to terminate the loop
#for val in range (1,10):
#    if val==6:
#        break
#    print(val)
        
# Eg:6
#for val in range (1,10):
#    print(val)
#    if val ==6:
#        break

# Eg:7    
#for val in range (1,10):
#    if val  ==6:
#        print(val)
#        break

#continue statement
#Eg :1
#for val in range(1,10):
#    if val ==6:
#        continue
#    print(val)

# ! practice problems
# ? print the even numbers between 20 to 40
#for val in range (20,40):
#    if val %2==0:
#        print (val)   

#? print odd numbers between 20 o 40
#for val in range (20,40):
#    if val %2!=0:
#        print (val)

#! --------> while loop
#while is used when we do not know the numbr of times the loop have to run
#? To iterate the non iteratable elements while loop is used

# todo syntax

# initialisation
# while condition
#   statement
# increase or decrease

# | Eg:1
# to iterate number from 1 to 10

#i=0
#while i<11:
#    print(i)

# for loop practice
#write a program to display sum of odd numbers and even
#numbers that fall between
#12 and 37 (including both numbers)

#for value in range (12,37):
#    if value %2==0:
#        print(value)


# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432




#assessment problem-3
#for value in range (12,37):
#    if value %2==0:
#        print(value)

        
#n=int(input("enter the number"))
#sum=0
#for val in range(1, n+1):
#    sq=val*val
#    if val %2!=0:
#        sum=sum+sq
#    else:
#        sum=sum-sq
#print(sum)

# assesment , problem 3

#for all in range(12,37):
 # if val %2==0:
# print(val)

#for val in range (12,37+1):
#    if val %2!=0:
#        print(val)



#assesment , problem5
# reversed command is used to change the values from left to rig
#n1=input("Enter the number:")
#n1_reversed=n1[::-1]
#print(n1_reversed)
















































        














































 

























































    


























