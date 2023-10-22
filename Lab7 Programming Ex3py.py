def abc(name):
    infile=open(name,'r')
    outfile=open(name,'w')
    for line in infile:
        words=line.strip().split()
        for r in range(len(word)):
            if len(words[r])==4:
                words[r]=="XXXX"
        outfile.wite(''.join(words)+'\n')
#driver's code
name=input("Enter file name: ")
print(abc(name))
    