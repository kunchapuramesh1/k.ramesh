# Day:8
#--->Assesment
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number



#n=int(input("Enter the number"))
#n1=n*n
#print("n:",n1)

#!Eg:4
# ? Function with return statement

#return
#1.)A variable declared inside the function can be acccessed outside the function
#using return
#2.)Returb does not print anything
#3.)We cannot write any below return statement


#def f1():
#    z = 8
#f1()
#print(z) # Error -->cannot use outside the function

#def f1(a,b):
#    c =a*b
#    return c
#print(f1(6,8))
#obj = f1(6,8)
#obj1 = f1(4,6)


#def gracemark(object):
#    print(object+4)
#gracemark(obj)
#gracemark(obj1)


# ? problem:1
#def palindrome(n):
#    string = str(n)
#    rev = str(n)[::-1]
#    if string==rev:
#        print(n,"palindrome")
#    else:
#        print("not palindrome")
#a =int(input("Enter the value:"))
#palindrome(a)

#Based on the declaration of parameters and args
#Functions are divided into 5 catagories

#positional args
#keyword args
#default args
#variable length args
#keyword variable length args


# positional args
#? The position of parameter achive to same as position as arguments
#Eg:1
#def profile(name,phone,mark):
#    txt ="My name is{}.My phone number is {}. I got {} marks."
#    print(txt.format(name,phone,mark))

#profile(8074884522,"Ramesh",95) # Unexpected output

# * Keyword args
# ! Eg:1
# ?To overcome the disadvantages of position args,we use keyword args
# ? It is the process of intialising the parameter with the args while calling the
# ? function
#def profile(name,phone,mark):
#    txt ="My name is {}.My phone number is {}. I got {} marks."
#    print(txt.format(name,phone,mark))

#profile (name ="ramesh",mark=95,phone=7894561230)



# todo ---> Exception of keyword args function
#def profile(name,phone,mark):
#    txt ="My name is{}.My phone number is {}. I got {} marks."
#    print(txt.format(name,phone,mark))

#profile(name="Ramesh",1234567890,mark=99)# error -->positional args follow keywordargs
#profile(7894561230,name="Ramesh",mark=99)#error -->name has multiple values
#profile("Ramesh",mark=99,phone=7894561230)


# * Default args
#The method of assigning the argument to parameter while declaring the
#Function
# ! Eg:1
#def profile(name,phone,place="Kadapa"):
#    txt ="My name is {}.My phone number is {}. I am from {}."
#    print(txt.format(name,phone,place))

#profile("Ramesh",78945661230)


# ! Eg:1
#def profile(name,phone,place="Kadapa"):
#    txt ="My name is {}.My phone number is {}. I am from {}."
#    print(txt.format(name,phone,place))

#profile("Ramesh",78945661230,"visakapatanam")


#Eg:2
#def profile(name,phone,place="Ramapuram"):
#    if place!="Ramapuram" or place=="Ramapuram" or place=="Ramapuram":
#       txt="My name is {}.My phone number is {}. I am from {}."
#       print(txt.format(name,phone,place))
#    else:
#       print("yor are not eligible to signup")
#profile("ramesh",789456123)


# ! Exception
#def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
#    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,place))
#    else:
#        print("You are not eligible to Signup")
#file("Ramesh",9876543210)


# * Variable length parameter
# !Eg:1
# To pass more then 1 arg to a parameter means we use variable length args
# To convert normal parameter to variable length param,add*to ther prefix of param
#name="ram",'name2','name3'
#def profile(*name):
#    for val in name:
#        print("My name is",val)
#profile("ram",'name2','name3')



# | Eg:2 
#def profile(*name,age):
#    for val in name:
#        print("My name is",val,"may age is",age)
#profile("ram",'name2','name3',20)#Error -->age has no args


#def profile(age,*name):
#    for val in name:
#        print("My name is",val,"may age is",age)
#profile(20,"ram",'name2','name3')

# * Keyword variable length args
# ! Eg:1
#def price(**price_list):
#    print(price_list)

#price(shirt=1000,iphone=80000)

#d1 = {"a":100,"b":200,"c":300}
#d1 = dict(a=100,b=200,c=300)
#print(d1)



#n=5
#n=int(input("Enter the value"))
#d1={}
#for val in range(1,n+1):
#    d1[val] = val**2
#print(d1)

#or?

#def dict1(n):
#    d1={}
#    for val in range(1,n+1):
#        d1[val] = val**2
#    print(d1)
#dict1(5)


#| ---------> object oriented programming
# The paradigms of objects oriented programming are

#class
#object
#inheritance
#polymorphism
#abstraction
#encapsulation

# ! class is a blue print of an object

#l1=[1,2,3,4,5,6]

# ?Eg:1
#class c1:
#    name1="Ramesh"
#    print(name1)


# Eg:2
#class person:
#    name="Ramesh"

#c=person() #c as object
# The process of creation of an object is called as instantiation
#print(c.name)

# ? Eg:3
#create of a method
#when the function is created with a class is called as method

#Method without parameter
#class person:
#    def display(person):
#        print("Hello welcome to classes")

#p = person()
#p.display()

# ? Eg:48


#Method with parameter
#class person:
#    def display(person,name,age):
#        print(name,age)


#p = person()
#p.display("ramesh",20)

#Eg:5
#class person1:
#    fname = "Ramesh" #attribute or static variable
#    lname = "R"

#    def first_name(self):
#        print(self.fname)


#    def full_name(self):
#        print(self.fname+""+self.lname)

#p = person1()
#p.first_name()
#p.full_name

# ? Eg:6
# constructors --> __init__()
# This is a special method which has the ability to excute itself without
#Calling it manually through the process of instantation

#class profile:
#    def __init__(self):#constructormethod
#        print("Hey")

#p = profile()#execution of constructor through this process



    













































    



    
