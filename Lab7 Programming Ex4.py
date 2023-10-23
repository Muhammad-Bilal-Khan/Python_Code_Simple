def myGrep(name,target):
    infile=open(name,'r')
    line=name.split()
    for line in name:
        if target in line:
            print(line, ends=" ")
#driver's Code
name=input("Enter file name ")
target=input("Enter target ")
print(myGrep(name,target))