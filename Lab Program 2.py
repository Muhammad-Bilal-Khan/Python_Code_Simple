contacts={}
def phone_directory():
    #contacts={}
    #q=question
    q=input("Do you want to add value in directory  ")
    q.lower()
    while q== "yes":
        key=input("Enter the key you want  ")
        value=input("Enter the value you want for this key  ")
        contacts[key]=value
        q=input("Do you want to add value in directory  ")
        q.lower()
        while q== "yes":
            key=input("Enter the key you want  ")
            value=input("Enter the value you want for this key  ")
            contacts[key]=value
            q=input("Do you want to add value in directory  ")
    else:
        print("Ending Program")
def del_contact(key2):
    k2=key2
    del contacts[k2]
    return (contacts)

def length_directory():
    print("Length: ",len(contacts))
 #sourcecode   
directory= phone_directory() #to add and print contacts
print(directory)
print(contacts)
del_question=input("Do you want to delete a key from phone directory?  ")
del_question.lower()
if del_question=="yes":
    key_to_delete=input("Enter key ")
    del_contact(key_to_delete)  #to delete a contact

length_directory() #to print number of contacts
print(contacts)