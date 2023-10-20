def even(num):
    for n in range(2,num):
        if (n%2==0)or(n%3==0):
            print(n,end=" ")    
num=int(input("Enter the number:  "))
print(even(num))
            