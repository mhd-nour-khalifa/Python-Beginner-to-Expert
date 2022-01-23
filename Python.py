# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:53:10 2022

@author: murat.orhun
"""
# comment

# data types. int float  string, boolean, list, dictionary.

print("data types")

one =100

print(type(one))

one=3.4
print(type(one))

one=True
one ="Ali"

#operators: +, - , * , / ,%,  < >= <= ==, !=, and ,or not

two= 45

sum = two +1000
print(sum)

x=10
y=20

print(x+y)

x="10"
y="20"

print(x+y)

print("20"+str(4))

print(int("20")+4)

print(type(x))
print(x*10)

#loops
print("test loops")

for i in range(10):
	print(i)

print("test again")
for i in range(6,10):
	print(i)


print("test again")
for i in range(2,10,2):
	print(i)



print("test again")
for i in range(10,0,-2):
	print(i)

print("test while")
p=0
while(p<10):
	print(p)
	p=p+2
	

# conditions
print("test conditions")

grade=70
if(grade>=90):
	print("A")
elif(grade > 80):
	print("B")
else:
	print("F")

# list

print("test list")
d=[]#empty
d.append(100)
d.append(300)
d.append(400)

print(d)
print(d[0])
print(d[-1])
print(d[-2])

t=[1,2,3,4,5,6,7,-4,-9]

print(t)
print("size of the list is: ", len(t))

#print list elements

for i in t:
	print(i)

print("array with index")

for i in range(len (t)):
	print(t[i])

# table:

table= [[1,2,3,4], [5,6,7,8], [9, 0, -1,-2]]
print(table)

print("print table")

for i in table:
	print(i)


print("print table with index")
for i in range(len(table)):
	for j in range(len(table[i])):
		print(table[i][j], " ", end="")
	print()

# functions...

print("test functions")
def sum(a,b):
	return a+b

print(sum(2,3))
print(sum("2","3"))
print(sum(2.4,3.7))
# print(sum("2",3))  # wrong

def hi():
	print("Hello")

hi()
print(hi())

# function give sum of array elementss

def sumArray(data):
	k=0
	for i in data:
		k=k+i
	
	return k

print(t)
print("sum of array t is:",sumArray(t))


def min(a=34, b=-100,c=10):
	if(a<b and a< c):
		return a
	elif (b<a and b<c):
		return b
	else:
		return c

print("test minimum number", min())
print("test minimum number", min(-200))
print("test minimum number", min(-200,-300))
print("test minimum number", min(-200,-300,-900))

#classes
print("test classes")
class Person:
	def __init__(self,name,a):
		self.name = name
		self.age=a
		self.__gender="Male"
	
	def info(self):
		print("Name is: ",self.name,", age is: ",self.age, "gender is:",self.__gender)
	
	def sum(self,a,b):
		return a+b
	
	def total(self,a,b,c):
		return self.sum(a,b)+c+self.age
	
	def getGender(self):
		return self.__gender
	
	def setGender(self, g):
		self.__gender=g

p=Person("Ali",45)
p.info()
print(p.name)
print(p.getGender())
p.setGender("Female")
p.name="Fatma"
p.info()

print(p.sum(2,3))
print("total",p.total(2,3, 4))

class Calculate:
	def __init__(self,p):
		self.p=p
		
	def sub(self,a,b):
		return a-b-self.p


class Student(Person,Calculate):
	def __init__(self,name,age,dept,p):
		#super().__init__(name,age)
		Person.__init__(self,name,age)
		Calculate.__init__(self,p)
		self.dept=dept
	
	def info(self):
		Person.info(self)
		print("Dept is: ", self.dept)


s= Student("Ali", 20,"CMPE",40)
s.info()
print(s.sub(3,5))
print(s.sum(2,3))


