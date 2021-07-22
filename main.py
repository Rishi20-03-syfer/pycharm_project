# types of data
"""
a = 5
b = "string"
c = True
d = 5.0
print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""

# if, eles,elif,
# a = int(input("entre a number"))

"""
if a==1:
    print("one")
elif a==2:
    print("Two")
elif a==3:
    print("three")
elif a==5:
    print("five")
else:
    print("no value")
"""
# string methods
'''
print(bin(5))
a = ["Rishi", "Raja", "Aiditay", "Priyesh", "Aman"]
a.append("rahi")
print(a)
a.clear()
print(a)
a.count("i")
print(a)
'''

# while loop
''' 
x = 1
while x<=5:
    print("Rishi ", end="")
    b = 1
    while b<=5:
        print("Vyas ", end="")
        b = b + 1
    x = x + 1
    print()
'''
# for loop
'''
a = "Rishi is not only good but also best"
for i in a:
    print(i)
'''

# dictonary
'''

dict = {"rishi ":"brave ",'sakshi':"not so ","rashi":""}
print(dict["rishi "])
print(dict["rashi"])
print(dict['rashi'])
print(dict["sakshi"])
print(dict["rishi "])
'''

# python data types
'''
Numbers=["int","float","complex"]
valuse =[25, 2.5, 2+5 ]
data = dict(zip(Numbers,valuse))
print(data)
'''
# pass, break, continue.
'''
x = ("candy")
i = int(input("how many candy you want"))
while i<10:
    print(x,i)
    if i>10:
        break
    i = i + 1
print("bye")
'''
'''

s = ["rishi", "rashi", "sakshi"]
a = []

for x in s:
    if "k" in x:
        a.append(x)
        print(a)d
'''
"""
a = int(input("put a number"))
b = int(input("put your birth date"))

if a==9:
    print("bye rishi")
elif b==27:
     print("good night rishi")
elif b==14:
    print("good night rashi")
elif b==6:
    print("good night sakshi")

"""
# numpy
"""
from numpy import *

arr1 = array([1,2,9,4])
arr2 = array([5,7,8,9])
arr2 = arr1.copy()
arr2[2] = 4
print(arr2)
print(arr1)
print(id(arr1))
print(id(arr2))
"""

# function
"""
def rishi(*a):
    return a[2]
print(rishi("Rishi ","vyas",5))

def dog(*name):
    return name[int(input("type a number"))]
print(dog("emli","chillo","tiger"))
"""
"""
def name(foods):
    for x in foods:
        print(x)

fruits = ["apple","banana","mango"]
name(fruits)

"""
# introducing to numpy
"""
from numpy import *
arr = array([
            [2,4,5,4,5,7],
            [1,3,6,8,9,0]
            ])
print(arr.shape)  #2 means row ,3 means colum
print(arr.dtype)
print(arr.ndim) #give a dimension of array
print(arr.shape)
print(arr.flatten()) #convert into 2d into 1d
print()
print()
print(arr.reshape(3,4))
print()
print()
print(arr.reshape(2,2,3))   #here frist 2 is for two 2d array ,second 2 is for 2 row and 3 is for number coloumns

"""
"""
from numpy import *
#matrises

m = matrix('1,2;3,4')

print(m)
"""
# Recurrsion
"""
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result = fact(7)
print(result) 
"""
# kwargs **
"""


def perinfo(name,**data):
    print(name)
    for i,j in data.items():
        print(i,":",j)

perinfo("Rishi",age = 17,city = "Amravati",mob = 7020954189)
"""
"""
from array import *
arr = array('i',[3,4,5,6,7])
newarr = array(arr.typecode,(a*a for a in arr))
for e in newarr:
    print(e)
"""

"""
from array import *
arr = array('i',[])

n = int(input("How many values you want"))
for a in range(n):
    x = int(input('Enter value'))
    arr.append(x)

print(arr)

val = int(input("Enter a number for search"))
k = 0
for g in arr:
    if g==val:
        print(k ,"is the index number")
    else:
     print("Not found")
    k = k + 1
    
name = []
r = int(input("type"))
"""
# global keyword and global() function

#
# a = 10
# print(id(a))
# def somthing():
#
#
#     a = 5
#
#     x = globals()["a"]
#     print(id(x))
#     print(x)
#     print(a)
#     print("in fun",a)
# somthing()
# print("out of",a)


# pass a list into a function

"""

list = [21,22,23,24,25,26,27,28]
def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("even:{},odd:{}".format(even,odd))

count(list)
"""
# fibonachi number
"""


def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fib(10)
"""
# how to find factorial
"""
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    print(f)

fact(5)
"""
# factorial using recurison
# def fact(n):
#
#     if n ==0:
#        return 1
#     else:
#         return n*fact(n-1)
# a = fact(5)
# print(a)

# expriment
"""
data = {"rishi":27,"rashi":14,"sakshi":6,"shivani":7,"jayu":1,"Aditya":29}
print(data.keys())
print(data.__getitem__("rishi"))
"""
"""
import datetime
a = datetime.datetime.now()

b = datetime.datetime(2003,3,271 )

c =. a - b
print(c)

"""
# Decorators
"""

def div(a,b):
    print(a/b)
# This tecnquie is called as decorators
def outer(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div = outer(div)
div(4,2)
"""
# class
"""

class Rishi:
    def __init__(self,cpu,ram):
        self.cpu =cpu
        self.ram =ram

    def last_name(self):
        print("vyas",self.cpu,self.ram)
    def middle_name(self):
        print("mahendra",self.cpu,self.ram)
blueprint1 = Rishi("i5",8)
blueprint2= Rishi("i7",16)


blueprint1.last_name()
blueprint2.middle_name()
"""
"""
class car_info:
	def __init__(mysillyobject, name, speed):
		mysillyobject.name = name
		mysillyobject.speed = speed
	def info(mysillyobject):
		print("my car info is",mysillyobject.name,mysillyobject.speed)

mycar = car_info("volvo 350",450)
myfrcar = car_info("BMW",400)

mycar.info()
myfrcar.info()

class car(car_info):
    pass

x = car("Maruti x1",200)
x.info()
print(id(car_info))
print(id(car))
"""
# types of variables
# mainly two types of var is instance var and class var
"""
class schoole:
    name = "kela hindi high schoole"   #this is class var


    def __init__(self,classes,section):
        self.classes =classes
        self.section = section

sch1 = schoole(int(input("type your class for sch1")),input("type your sec for sch1"))
sch2 = schoole(int(input("type your class for sch2")),input("type your sec for sch2"))

print(sch1.classes, sch1.section, sch1.name)
print(sch2.classes, sch2.section, sch2.name)
"""
# types of methods
# three types methods 1.instance , 2.class , 3.statics methods
"""
class student:
    schoole = "IIT pawai"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):         #here this is instance method
        print((self.m1+self.m2+self.m3)/3)
        
    @classmethod
    def info(cls):          #here this is class method
        print(cls.schoole)
        
    @staticmethod
    def get_schoole_name():   #here this is statics method
        print("hello ")
        
s1 = student(23,32,43)

s1.info()
s1.avg()
s1.get_schoole_name()
"""
# inner function
"""
class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap =self.laptops()

    def info_stu(self):
        print(self.name,self.rollno)
        self.lap.config()

    class laptops:
        def __init__(self):
            self.brand = "hp"
            self.ram = 8
            self.cpu = "i5"

        def config(self):
                print(self.brand,self.ram,self.cpu)


s1 = student('Rishi',25)
s2 = student("ram",30)

s1.info_stu()
s2.info_stu()

lap = student.laptops()
"""
# inhertance in classes
"""
class phone:
    def realme(self):
        print("realme phone")
    def oppo(self):
        print("oppo phone")

class cellphone(phone): #here you can accecs phone class or you can create a tree of 
    def realme1(self):   # inhert classes by creating a chain of it 
        print("realme phone 1")
    def oppo2(self):
        print("oppo phone 2")
p1 = phone()


p1.realme()
p1.oppo()


c1 = cellphone()

c1.realme()
c1.realme1()
c1.oppo2()
c1.oppo()
"""
# constructor in python
"""
class phone:
    def __init__(self):
        print("hello phone")

class cellphone(): #here you can accecs phone class or you can create a tree of
    def __init__(self):
        print("hello cellphone")
    def fectur(self):
        print("hello rishi")

class smart_phone(cellphone,phone):  # below second init() give ans from first argument of s
    def __init__(self):
        super().__init__()         
        print("hello smartphone")
    def feat(self):
        super().fectur()    #use super() for acceces methods

a1 = phone()
b1 = cellphone()
c1 = smart_phone()
c1.feat()
"""
# Polymorphisim
# 1.Duck typing
"""
class Pycharm:
    def execute(self):
        print("compling coad")
        print("run coad")

class laptops:
    def coad(self,ide):
        ide.execute()

class Mycharm:
    def execute(self):
        print("compling coad")
        print("run coad")
        print("hello user")
        print("wlecome user")

ide = Pycharm()     # here you can use Mycharm() insted of Pycharm()
                     #the main question is what is duck typing
lap1 = laptops()      # it mean a single variable can have different type of data 
lap1.coad(ide)          # means here execute has no meant the only mean is to the data type 
"""
# oparator overloading (add,sub,multi,divide classes)
"""
class student:
    def __init__(self,m1,m2):   #here self is for unknown object which is after s1 and s2
        self.m1 = m1 #1    #here self reffers to s1 and s2
        self.m2 = m2 #2    #here self reffers to s1 and s2
    def __add__(self, other):
        m1 = self.m1 + self.m2
        m2 = self.m1 + other.m2
        s3 = student(m1,m2)
        return s3

s1 = student(34,67)
print(s1.m1)         #see the syntax to co-relate between self and written object (s1)
print(s1.m2)
s2 = student(56,78)  #this two arguments reffers to 1 and 2
print(s2.m1)
print(s2.m2)         #see the syntax to co-relate between self and written object (s2)
s3 = s1 + s2

print(s3.m1)
"""
#  itrators
"""
nums = [1,2,3,4,5]
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
"""
# create a own itrator
"""
class toptwenty:
    def __init__(self):
        self.m1= 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.m1 <= 20:
            values = self.m1
            self.m1 += 1
            return values
        else:
            raise StopIteration
s1 = toptwenty()

for i in s1:
    print(i)
"""
# self example
"""
class topfive:
    def __init__(self):
        self.m1 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.m1<= 5:
            gve = self.m1
            self.m1 += 1
            return gve
        else:
            raise StopIteration
s1 = topfive()

for i in s1:
    print(i)
"""
# Genrators
# what is genrators = genrators are itrator cerateators ex
"""
def topfive():
    yield 1
    yield 2     #here yield is very important you can say it as keyword
    yield 3
    yield 4
    yield 5

value = topfive()

print(value.__next__())
print(value.__next__())
print(value.__next__())
"""
# some complex example for genrators
"""
def perfect_square():

    n = 1
    while n <= 10:    
        sq = n*n
        yield sq
        n+= 1

valuse = perfect_square()

for i in valuse:
    print(i)
"""
# Exception handling (try,except,finally)
"""
a = 5
b = 4      # Here if you put 0 insted of any other number than you will get an error
            # which is an zeroDivisionError (try it )
try:
    g = int(input("give a number"))
    print(g)
    print(a/b)

except ZeroDivisionError:
    print("take any other number insted of zero")
except ValueError:
    print("Give a number")
except Exception as e:
    print("going in wrong way",e)
finally:
    print("close pycharm")
"""
"""
# Modulest
import mymodule as rishi
print(rishi.a)
"""
# Threading
# example for
"""
from threading import *
from time import sleep
class hello(Thread):              #Threading in python is used to run multiple threads (tasks, function calls) at the same time.
    def run(self):
        for i in range(5):
            print("hello")          #here this two class are run on two different core but run at same time or say exicute at same time parallely
            sleep(2)

class hi(Thread): def run(self): for i in range(5): print("hi") sleep(2)                        #if you don't give a 
2 sec sleep to exicution it will jumble them (Try without sleep). r1 = hello() r2 = hi() 

r1.start()
sleep(1)
r2.start()
r1.join(-4)
r2.join()
print("bye")
"""
"""
# Date and time
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.ctime())
print(x.isoweekday())
print(x.fromisocalendar(2003,4,5))
print(x.isoformat())
"""
# json in python
"""
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
if __name__ == '__main__':
    print("yes")
# the result is a JSON string:
print(y)
"""
# file handling
"""
f = open("test.txt")
print(f.read())
print(f.errors)
print(f.mode)
print(f.seek(4))
print(f.buffer)
print(f.name)
print(f.fileno())
print(f.flush())
print(f.read())
print(f.buffer)
print(f.)
"""
# Types of searches in python

# 1 . simple search in Python
"""
lis = [1,3,5,6,7,8,9,10]

search = int(input("type a number"))

for i in lis:
    if i==search:
        print(i)
        break
else:
    print("not found")
"""
# 2 . linear search in python
"""
def search(lis, n):
    i = 0
    while i<len(lis):
        if lis[i]==n:
            return True
        i = i  + 1
    else:
        return False

lis = [1,3,5,6,7,8,9,10]
n = int(input("search a number"))

if search(lis,n):
    print("found ")
else:
    print("not found")
"""
# Binary search in python



import re
#(RegularExpressino)regular expressino written in a pattern
"""
txt  = "Hello world hell is here"
x = re.search("^H.*e$",txt)
if x:
    print("yes found")
else:
    print("not found")
y = re.search("^Hello.*here$",txt)
print(y,"found")
"""
"""
r = {"Rishi":"first year","Rashi":"second year","sakshi":"M.sc"}
price =int(input("give price"))
txt = "Car is of price {}"
print(txt.format(price))
"""
"""
#        types of algorithems
#        1. Guss and cheak
#         2. Bisection search
#           3. Approximation
"""
# 1 guss and check
"""
#
# cube = int(input("give a perfect cube "))           # don't use (,) for long values like values for base 1,00,00,000 simply remove them and try.
#
# for i in range(cube):
#     if i**3 == cube:
#         print("found cube root it is ", i )
#         break
# else:
#     print("opps it is not a perfect square")
"""
 # 2.Approximation solution
"""
# cube = int(input("give a number "))
# constant = 0.01
# incriment = 0.0001
# gusses = 0.0
# num_guss = 0
# while abs(gusses**3-cube) >= constant:
#     gusses += incriment
#     num_guss += 1
# if abs(gusses**3-cube) >= constant:
#     print("no cube root of ", cube)
# else:
#     print("found", cube,gusses)
"""
# 3 Bisection search
"""
# cube = int(input("give me a cube "))
# epselon = 0.01
# num_gusses = 0
# low = 0
# high = cube
# guss = (high + low)/2.0
# while abs(guss ** 3 - cube) >= epselon and guss <= cube:
#     if guss**3 < cube:
#         low = guss
#     else:
#         high = guss
#     guss = (high + low) / 2.0
#     num_gusses += 1
# print("num_guss = ", num_gusses)
# print("cloest valu for cube is" , guss)
"""
# Docstring
"""
# def addtion(a, b):
#     """  #This function add two values    """
#     c = a + b
#     return c
#
# result = addtion(3, 4)
#
# print(result)
# print(addtion.__doc__)
"""
# Behaviour of function towards print and return
"""
# def add(x, y):
#     return x + y
#
# def mutliply(x , y):
#     print(x*y)
#
# add(3,4)              # if you call function(a func with return but not print stament in it) it will give you nothing.
# mutliply(3,4)         # if you simple call a function(a func which has print statment but not return ) it will give you value
# print(add(3,4))       # if you print a functoin with return in it , it will give you a value.
# print(mutliply(3,4))  # when you print a function without having return in it , it give you none
"""
# Escape charcter in python
"""
# 1. \
# sentance = 'Rishi's best friend is ' # if you ran this code you will recive a error . to fix this
# sentance = 'Rishi\'s best friend is ' # here a singel quote is ignored due to (backslash) \ .
# print(sentance)

# 2 \\
# sentance = "Blackslash is \\ this " # double backslash give me a singel backslash
# print(sentance)

# 3 \n

#print("Hell is \n here")    # \n creats new line for me
                            # here in this example here will print in second line while Hell is print in first line.

# 4  \r                     # \r overwrit the word or char before it .
# print('shubham\nmishra')
# print('Rsh\rvyas')
# print("Rishi\risagoodboy")

# 5 \t                   # it is use for giveing tabs
# print("Rishi\tis good boy")

# 6 \000                # octal value

# print("\122\111\123\110\111")

# 7  \xhh  # hexal value
# print("\x41 \x42 \x43 \x44")
"""
# 8                         # form feed
"""
# print("hello\f\f\fworld")

# how to add to dictonarys
#
# a = {1:"one",2:"two"}
# b = {3:"three",4:"four"}
# c =  {**a,**b}
# print(c)
"""
# namedtuple
"""
# from collections import namedtuple       # can be used as class to form objects
#
# bike = namedtuple("fourwhiller","colour milage engine")  # dike is class here
# my_car = bike("red", 38.20 ,"v8")             # colour == red and milage == 38.20
# print(type(my_car))                      # type is fourwhiller
# print(my_car)
# print(my_car.__len__())
# print(my_car.__doc__)
# print(my_car.__class__)
# print(my_car.engine)
# my_car.colour = "blue"             # like tupels namedtuples are also immutable
                                    # to convert list into set tuple and string using json
"""
# import json
# list_data = ["hp","asus","aser","apple","hcl"]
# print(type(list_data))
# print(type(json.dumps(list_data)))
# list_data_2 = ["pav","tuf","nitro","mac","me"]
# print(set(list_data))
# print(type(set(list_data)))
# print(type(tuple(list_data)))
"""
                # Arrays in python
"""
from array import *

marks = array("i",[50,60,65,70])  # "i" for interger values (signed),eg.."u" for string value(unicode)
# print(marks)
# new_marks  = array(marks.typecode, [a*a for a in marks]) # for copying a array
# print(new_marks)
# name = array("u",["R","i","s","h","i","_","a","m"])      # strings are not allow in arrays instade of char.
# print(name)
"""
                           #     Numpy in python
                           # numpy for multi dimnsional array
from numpy import *

# marks = array([1,2,3,],int ) # here int is totaly optional
# print(marks)
                          # Types of arrays that can be created using numpy
"""
# 1 Array()
# marks = array([1,2,3,],int ) # here int is totaly optional
# # print(marks)

# 2 linespace()
# marks = linspace(0,16,17) # start ,stop(included([0]= 1,[16] = 16)) ,parts of range(0,16)
# print(marks)               # by default value for parts is 50 and linespace cannot be converted to int

# 3 logspace()
# marks = logspace(1,40,5) # start from 10**1 ,stop at 10**40 ,step is range(5)
# print(marks)             # step is by default is stop-1

# 4 arange()
# marks = arange(1,15,1) # start,stop ,step just like range()
# print(marks)           # stop is excluded

# 5 zeros()
# marks = zeros(10) # 10 is the number of zeros
# print(marks)

# 6 ones()
# marks = ones(10) # 10 is the number of ones
# print(marks)

# copy in arrays
# marks = array([1,23,4,56])
# marks = marks_1                #  Alising (both points towards to same add in memory)
# marks_1 = marks.view()        # shallow copying (change in one array affect on other one)
# marks_2 = marks.copy()         # deep copying (change in one array will not affect on other one)
# print(marks)
# marks[0] = 7
# print(marks_1)
# print(marks_2)
# print(id(marks))
# print(id(marks_1))
# print(id(marks_2))
"""
# multidimensinal array
"""
marks = array([
    [1,2,3,4],
    [2,34,6,5]
                ])
print(marks)
"""
                     # comparison in lists (oneliner loop)
"""                     
# [ expression-involving-loop-variable for loop-variable in sequence ]

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# printf = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# print(printf)

# [ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
"""