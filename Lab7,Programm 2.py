def duplicate(name):
    file=open(name,'r')
    result=[]
    for line in file:
        for x in line.strip().split():
            if x in result:
                return True
            result.append(x)
        result.append(x)
    return False
#driver's Code
name=input("Enter File name: ")
print(duplicate(name))