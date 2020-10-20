print("Hello")
print("Hi python")
print('''a
b
c
d
e
''')
a=54 #integer
b=2.5#float
c="rahul" #string
d=True
print("a is ",a)
print("b is ",b)
print("c is ",c)
print("d is ",d)

aa,bb,cc=32,2.5,"air"
print(aa,bb,cc)
print("type of a is",type(a))
print("type of b is",type(b))
print("type of c is",type(c))

#"string types in python"
st='this is python string'
print(st)
print(st[0])
print(st[5])
print(st[1:6])
print('lenght of string is',len(st))
print(st[-3])
print(st*3)


#reverse string

print(st[::-1])

#concat string
r="java prog"
print(st+r)


#list
rt=[32,5.2,478,"rahul",True]
print(rt)
print (rt[2])
print(type(rt))
rt[1]=21000
print(rt)

del rt[0]
print(rt)
print(len(rt))
print(rt[2:])
print(rt*2)

#tuple
tp=(21,2.3,"rahul")
print(tp)
#tp[0]=52


#dictionary
#key value pair cocept
dt = {'roll no':444 ,'name':'rahul','mark':456}
print(dt)
print(dt.keys())
print(dt.values())

print(dt["name"])

dt1 = {'roll no':[1,2,3] ,'name':'rahul','mark':456}
print(dt1)

#sets
fruits={"rahul","aaaa","mango"}
print(fruits)
fruits.add("banana")
print(fruits)
fruits.remove("banana")
print(fruits)

#operator
s=12
d=56
print(s/d)
print(s//d)
c=s>d
print(c)


#user input function
a=input("enter name")
print(a)
print(type(a))

b=int(input("Enter the value:"))
print(b)
print(type(b))

c=int(input("Enter the value:"))
print(c)
print(type(c))

print(b*c)