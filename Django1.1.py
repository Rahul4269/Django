Name=input("Enter your Name :")
sub1=int(input("Enter marks of sub 1:"))
sub2=int(input("Enter marks of sub 2:"))
sub3=int(input("Enter marks of sub 3:"))
sub4=int(input("Enter marks of sub 4:"))
sub5=int(input("Enter marks of sub 5:"))
percentage=(((sub1+sub2+sub3+sub4+sub5)*100)/500)
student1={"Name":Name,
          "sub1":sub1,
          "sub2":sub2,
          "sub3":sub3,
          "sub4":sub4,
          "sub5":sub5,
          "percentage":percentage
          }
print(student1)