#Day:9

#2.)Find the uncommon words from 2 strings
#s1="hello how are you"
#s2 ="Hello how is"

#2.) problem ->solution
#s1="hello how are you"
#s2 ="Hello how is"

#s1 = s1.split(" ")
#s2 = s2.split(" ")

#for val in s1:
#    if val not in s2:
#         print(val)
#for val in s2:
#    if val not in s1:
#        print(val)

#3.)Write a code print the 8th fibanochi number
#0,1,1,2,3,5,8

#n1 =0
#n2 =1
#ans = 0+1 ==>1

#n1 = 1
#n2 = 1
#ans = 1+1===>2

#n1 =1
#n2 =2
#ans = 1+2==>3


#n1 =2
#n2 =3
#ans = 2+3==>5

# ! Find the 8th fibanochi number
#num = 5
#n1= 0
#n2 = 1

#for val in range(num):
#     ans = n1+n2
#     n1 = n2
#     n2 = ans
#print(ans)



# ! constructors
# Eg:2
# * unparametarised constructor
#class profile:
#    def __init__(self):
#        print("Hello world")

#obj = profile()
#obj.__init__()

# ? Eg:3
#parametarised constructor
#class profile:
#    def __init__(self,id,name,age):
#        print(id,name,age)

#obj = profile(1,"ram",20)

# ? Eg:4
#class c1:
#    email = "ram@gmail.com"
#    def m1(self):
#        name = "ram"
#        place = "rmp"
#        print(self.name,self.place)
#        print(self.email)

    
#object = c1()
#object.()

#Eg:5
#class c1:
#    def m1(self):
#        name = "ram"
#        age = 19
#        return name,age
#    def display(self):
        #print(name,age)
        #print(self.name,self.age)
#        print(self.m1())
        
#object = c1()
#object.display()

#Eg:6
#? To use the variable inside the constructor in anther methods
#class class1:
#    def __init__(self):
#        self.name = "ram"
#        self.email = "ram@gmail.com"
        #return name,email #error -->cannot use return with constructo

#    def display(self):# instantce method
#    print(self.name,self.email)


#c1 = class1()
#c1.display()



# ! -----> Inheritance
# The process of utilising the method and attributes of parent class
#through the object of child class it is called as inheritance

# 5types of Inheritance
#Single Inheritance
#Multilevel Inheritance
#Multiple Inheritance
#Hybrid Inheritance
#Heirarichal Inheritance


#Single Inheritance
#It has only one parent class and only one child class


# ! Eg:1
#class parent:
#    def m1(self):
#        print("Iam parent class")


#class child(parent):
#    def m2(self):
#        print("Iam child class")

#p = child()
#p.m1()



# ! Eg:2

#class c1:
#    def __init__(self):
#        print("Iam constructor from parent class")

#class child1(c1):
#    pass

#obj = child1()
'''
#Eg:3
class parent:
    name = "ram"

class child(parent):
    name ="name1"

    def display(self):
        print(self.name)

d = child()
d.display()
'''
# ! Multilevel inheritance
# ? Eg:1
'''
class voice:
    def sound(self):
        print("all the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")


class cat(dog):
    def cat_voice(self):
        print("Meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''
'''
# ? Eg:2
class honda_city:
    def honda_city_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def honda_city_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class civic(amaze):
    def civic_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def civic_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class amaze(Honda_city):
     def amaze_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def amaze_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)


class honda (civic):
    pass

honda = honda()
honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
honda.civic_body_specs("white",2000,5.5,8,"hatchback")
                       
        
'''
'''
# Multiple Inheritance
 #? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()
'''
'''
# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)

        
calc=division()
calc.add(3,4)
calc.mul(4,2)
'''
'''
# ! Heirarical inheritance
#? The one parent classe will asct as parent for all the child classes
class catagory:
def weight(self, weight): print(weight)
I
def display(self, color, taste): print(color, taste)
class Tomato(catagory):
def tomato_specs (self):
color="black"
taste "neutral taste"
self.display(color, taste)
class carrot (catagory):
def carrot_specs (self):
    color="green"
    
'''
'''

#Hybrid Inheritance
# The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("Class 3")
class c4(c2):
    def m4(self):
        print("Class 4")
        
    def m3(self):
        print("I am m3 from c4")
class c5(c4):
    def m5(self):
        print("Class 4")

class c6(c5,c3):
    def m6(self):
        print("Class 4")
obj = c6()
obj.m3()
'''
# ! ------------>polymorphism
# poly - many ,morph --->form
# A function which has the ability to perform more than 1 functionality
#then it is considered to be as polymorphism

# * polymorphism in builtin functions
#ken() --> Which is used to find the length of list,tuple,dict etc...
#Index()
#Max()
#Min()
#Count()
#pop()
#and more...


# * polymorphism in operators
# +
#Print(8+8)
#Print("k"+'1')
#Print([1,2,3]+[5,6])


# *
#print(6*7)
#l1 = {12,3,4,5,6}
#print(*l1)
#def f1(*args)
#l1 = [1,2,3,4]
#print(l1*10)


# Polymorphism in classes
# We can achieve polymorphism in 2 ways
#1.)Method overloading -->it is not possible in python
#2.)Method overriding

#) Tasks
#Write the code for the belwo tasks using function
#1.)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'

#2.) Find then 67, is strong number or not

#3.) 11 = [1,2,3,4,5,6]
#n=2 --> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]















