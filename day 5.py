#Day :5

# !common functions of for list

#l1 = [6,7,8,9,0]
#print(len(l1))

#print(max(l1))
#print(min(l1))

#l1 = [6,8,9,"9","u"]
#print(max(l1)) #--> error coz its a combination of int and string
#print(min(l1)) #--> error coz its a combination of int and string

#l1 = [6,7,8,9,0,8.89,-5,0.78]
#index() -->to get index value of specific element
#print(l1.index(9))

#l1 = [6,7,8,9,0,8.89,-5,0.78]
#count() --> how many num of times an element is repeated
#print(l1.count(6))


# ! some functions which is specifically used for list

# To add element inside list
# ? insert(index_value, element) --> to add element at specific index position
#l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
#l1.insert(2,"cars")
#print(l1)


# ? To delete element from list
#l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
#pop() --> last element will be deleted
#l1.pop()
#print(l1)

# * pop(index_value --> used to delete element at specific index
#l1.remove(8.89)
#print(l1)

#* clear() --> to complete delete all element in list
#l1.clear()
#print(l1)

# del --> to delet the list
#del l1 #or del(l1)
#print(l1)

# ? ---->join 2 lists

#l1 = [9,0,8]
#l2 = ["p","0","t",34]
#print(l1+l2)

#or
#extend() --> to combine 2 list
#l1.extend(l2)
#print(l1)

# ? ----> copy()
#l1 = [6,7,8,9,3]
#l2 = l1.copy()
#print(l2)
#print(l1)

#print(id(l1)
#print(id(l2))

# ! diff between shllow copy amd deep copy
#shallow copy
#import copy
#l1 = [8,9,0,[5,6,],[3,2,1]]
#l2=copy .copy (l1)
#l1.append(89)
#print(l1)
#print(l2)

# * deep copy ---> used to copy the list with nested list
#l1 = [8,9,0,[5,6,],[3,2,1]]
#print(l1[-1]) ---> to index nested list

#l2=copy .copy (l1)
#l1[-1].append('cars')
#print(l1)
#print(l2)

# ? sort --> arrange elements  in list in assending or descending order
#l1 = [9,7,45,0,-6,5,12]
#l1.sort() # to arrange in ascending order
#print(l1)

#l1.sort(reverse=True) # to sort in descending order
#print(l1)

#l1 = ['z','i','o','p',9]
#l1.sort()
#print(l1) --> error

# ? list constructor
#* list() --> to conver other collection datatype to list
#l3 = ((8,9,0))
#print(list(l3))

#l4 = (8,9)
#print(list(l4))

# ! ---> nested list

#l1 = [8,9,[0,8,7],["p","o","y"],[8,'t']]
#print(l1[-2][1] # -->o

#print(l1[1:4])
#print(l1[1:-1])

# ? to delete "t" from l1
#l1[-1].remove('t')
#print(l1)

# ? combine these["p","o",'y'],[8,'t'] list in l1 to["p","o",'y',8,'t']
#l1 = ["p","o",'y']
#l2 = [8,'t']
#l1.extend(l2)
#print(l1)

# ! ----> Tuple
# characterstics of tuple

#1.) Tuple have to be surrounded bt ()
#2.) The element inside tuple are not changable
#3.) The element inside tuple are indexed
#4.) The element will execute in order
#5.) It is heterogenous
#6.) It allow duplicate elements

# Eg:
#t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
#print(t1)
#   print(type(t1))

# ? indexing,slicing are all same as list

#l1 = (8)
#print(type(l1)) #int

#l1 = (8,)
#print(type(l1)) #tuple

#t2 = 8,9
#print(type(t2)) #tuple

#len(),min(),max(),index(),count() --> all same as list


# To add element inside tuple -->cannot add
#cannot delete any element from tuple

# * join 2 tuples
#t1 = (8,9,0)
#t2 = (6,7,8)
#print(t1+t2)

#To add all element inside list
#sum()
#l1 = (8,9,7,6)
#print(sum(l1))

# * sort tuple
#t1 =(8,9,0,89,12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1,reverse=true)))

# * Iterate list and tuples

#l1 = [9,8,0,6,5]
#for i in l1:
#    print(i)

# * Iterate based on index valu
#l1 = [9,8,0,6,5,8,56]
#for i in range (0,len(l1)):
#    print(l1[i])

# ! ----> strings
#s1 = 'o'
#print(type(s1))

#s1 = "u"
#print(type(s1))

#s1 = "hello world"
# * To acess string
#print(s1)
#indexing and slicing -->same as list and tuple
#print(s1[0:5])

#------->common functions

#len(),min(),max(),index(),count()
#s1 = "hello world"
#print(len(s1))
#print(min(s1))
#print(max(s1))

#ord() ---> used to find the ASCII value of a character
#print(ord(s1))
#print(ord(s1))

# functions of string
#s1 = "ramesh"

# ? to convert all characters to upper case
#print(s1.upper())

# ? to convert to lower case
#s1 = "RAMESH"
#print(s1.lower())

# strip()-->to eliminate the space in begining and end of string
#s1 = " peoples comes from powerfull places "
#print(s1.rstrip()) ---->"rstrip" starting the word create space
#print(s1.lstrip()) -----> "lstrip" it is not create the space starting


# split() --> to split the words in string based on a character
#s1 = "i am from kadiri"
#print(s1.split())
#print(s1.split("a"))
#print(s1.split("m"))


# * replace() --> to replace a specific char in the string
#s1 = "om nama shivaya z"
#print(s1.replace('z','&&'))

# * swapcase() ---> to convert capital to small and small to capital at a time
#s1 = " belive yourself "
#print(s1.swapcase())


# * title () --> to write the string in format of title
#s1 = "never give up"
#print(s1.title())

# * capitalize() --> 1st char of string will be converted to capital
#s1 = "never give up"
#print(s1.capitalize())

# * join the strings
#s1 = "hello"
#s2 = " world"
#print(s1+s2)

#s1 = '''how are you  
#i am fine
#hey there

#print(s1.splitlines())

# * find() --> To find the index based on a character
#s1 = " hello my dear "
#print(s1.find('h'))
#print(s1.index('e'))

# * join() -->
#l1 = ["hii","who "]
#print(" ".join(l1))
#print("$".join(l1))

#s1 = " welcome to all "
#print(s1.endswith('l'))
#print(s1.isdigit('w'))


#s1 = "67"
#print(type(s1))
#print(s1.isdigit())

# * print the string in reverse manner
#s1 = "Welcome to all"
#print(s1[::-1])

# ! ---> Eg:1
#wap to find the number of lower case letters
#s1 = " mechanical engineering "
#count = 0
#for i in s1:
#    if i.islower():
#        count+=1
#print("the total num of lower case letters:",count)

# ! -----> Eg:2 r -->"$"
#s1 = 'restarter'
#fst = s1[0]
#bal = s1[1:]
#txt = bal.replace(fst,"$")
#print(fst+txt)

# ! -------> Eg  :3

#s1 = '''
#Paragraphs are the building blocks of papers. Many students
#define paragraphs in terms of length: a paragraph is a group
#of at least five sentences, a paragraph is half a page long,
#etc. In reality, though, the unity and coherence of ideas
#among sentences is what constitutes a paragraph.'''


#characters = len(s1)
#print(characters)

#words = s1.split(" ")
#print(len(words))


#sentenses = s1.split('.')
#for val in sentenses:
#    if val =='':
#        index = sentenses.index('')
#        sentenses.pop(index)
#print(len(sentenses))

#space=0
#for val in s1:
#    if val ==" ":
#        space=space+1
#print (space)



# Assesment :-
# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

























































































 

























         








































