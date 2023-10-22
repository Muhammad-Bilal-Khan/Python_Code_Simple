question=input("Enter yes if you want progression or no if you don't want ")
if question == "yes":
    a=int(input("Enter the 1st value of your arthematic progression: "))
    d=int(input("Enter the common difference: "))
    n=int(input("Enter the nth term you want to calculate "))
    answer=(a+(n-1)*d)
    print("The nth term will be: ",answer)
elif question=="no":
    print("Program finishing")
while question == "yes":
    print("Write your answer in yes or no only")
    question=input("Do you want to continue? ")
    if question=="yes":
       a=int(input("Enter the 1st value of your arthematic progression: "))
       d=int(input("Enter the common difference: "))
       n=int(input("Enter the nth term you want to calculate "))
       answer=(a+(n-1)*d)
       print("The nth term will be: ",answer)
    elif question== "no":
        print("Program finishing")