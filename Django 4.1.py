f=open('AB.txt','w')
id=0
name=''
salary=0
for id in range (1,11,1):

    id=int(input("Enter ID"))
    name = input("Enter Name")
    salary = int(input("Enter Salary"))

    f.write(str(id)+'\n')
    f.write(name) + '\n'
    f.write(str(salary)+'\n')

print('fle saved')
f.close()




