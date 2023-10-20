name=input("Enter you name: ")
father_name=input("Enter you Father's name: ")
roll_no=input("Enter your Roll Number: ")

sub1=str(input("Enter the name of first subject: "))
sub1_marks=int(input("Enter marks of the first subject: "))
sub2=str(input("Enter the name of second subject: "))
sub2_marks=int(input("Enter marks of the second subject: "))
sub3=str(input("Enter the name of third subject: "))
sub3_marks=int(input("Enter marks of the third subject: "))
sub4=str(input("Enter the name of fourth subject: "))
sub4_marks=int(input("Enter marks of the fourth subject: "))
sub5=str(input("Enter the name of fifth subject: "))
sub5_marks=int(input("Enter marks of the fifth subject: "))

per_centage=(sub1_marks+sub2_marks+sub3_marks+sub4_marks+sub5_marks)*100/500
avg=(sub1_marks+sub2_marks+sub3_marks+sub4_marks+sub5_marks)/5
total=sub1_marks+sub2_marks+sub3_marks+sub4_marks+sub5_marks

print("Student Name: ",name)
print("Father Name: ",father_name)
print("Roll Number: ",roll_no)
print("Percentage is: ",per_centage)
print("The total numbers are: ",total)

if(avg==90):
    print("Grade: A*")
elif(avg==80):
    print("Grade: A")
elif(avg==70):
    print("Grade: B")
elif(avg==60):
    print("Grade: C")
else:
    print("Grade: F")


