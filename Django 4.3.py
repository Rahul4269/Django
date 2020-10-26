f=open('AB.txt','r')



data=f.read(100)

r=open("AAA.txt",'w')
for char in data:

    if char in "aeiouAEIOU":
        r.write(char)




f.close()