#function is block of code which is reusable entity
'''
def Hello():
    print("Hello")
    print("In function")
print("I am calling")
Hello()

#value pass in fun
def sum(a,b):
    c=a+b
    print("sum is :",c)

sum(10,4)

def sum(a,b):
    c=a+b
    print("sum is :",c)

x=int(input("Enter a number "))
y=int(input("Enter a number "))
sum(x,y)

#function with return value
def calc(a,b):#actual
    z=a*b
    return  z

x=int(input("Enter a number "))
y=int(input("Enter a number "))
c=calc(x,y)#formal
print("sum .. returned",c)

#function with default parameter

def show (name="Test",city="mumbai"):
    print(name)
    print(city)
show()

def show (empo,name,salary):
    print('emp..',empo)
    print('name',name)
    print("salary",salary)
show("E001",'john',21000)
show(name='mark',salary=22000,empo='E002')
show(salary=31000,name="rahul",empo=25000)

def Hello():
    print("Hello")
    print("Hello Python")

d=Hello()
d

'''
#decorator for the function
def decr(func):
    print('start of calling')
    func()
    print("End of calling")

def Hello():
    print("I am Hello")

d=decr(Hello)


print("*******************************")

def decr(func):
    def sayHello():
        print('start of calling')
        func()
        print("End of calling")
    return sayHello()
def Hello():
    print("I am Hello")

d=decr(Hello)



#modules
def sum(a,b):
    print("sum is ..",(a+b))

def Hi():
    print("Hi function ")

def Hello():
    print("Hello calls")



