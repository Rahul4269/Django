
#By using temporary variable
a=int(input("Enter the first number:  "))
b=int(input("Enter the second number:  "))
dummy=a
a=b
b=dummy
print("First Number is",a)
print("Second Number is",b)

#without temporary variable
c=int(input("Enter the first number:  "))
d=int(input("Enter the second number:  "))

c,d=d,c
print("First Number is",c)
print("Second Number is",d)

#by using +,- operator
e=int(input("Enter the first number:  "))
f=int(input("Enter the second number:  "))

e=e+f
f=e-f
e=e-f
print("First Number is",e)
print("Second Number is",f)

#by using *,/ operator
g=int(input("Enter the first number:  "))
h=int(input("Enter the second number:  "))

g=g*h
h=g//h
g=g//h
print("First Number is",g)
print("Second Number is",h)