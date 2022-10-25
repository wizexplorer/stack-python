L=[]
def insert():
    addMore="y"
    while(addMore.lower()!="n"):
        name=input("\t     Enter the name of the book to add : ")
        print("\t     The book",name,"has been added")
        L.append(name)
        addMore=input("\t     Add more(y/n) ? ")
        if addMore.lower() !="y" and addMore.lower() !="n":
            print("\t\t     Wrong input")
            addMore=input("\t     Add more(y/n) ? ")
    print("\t     Current book list : ",L)

def remove():
    delMore="y"
    while(delMore.lower()!="n"):
        if L==[]:
            print("\t     The stack is empty, enter a name to remove first")
            add_or_not=input("\t     Insert book(y/n) ? ")
            if add_or_not.lower()=="y":
                insert()
            elif add_or_not.lower()=="n":
                choice=4
            else:
                print("\t\t     Wrong input")
                add_or_not=input("\t     Insert book(y/n) ? ")
        else:
            x=L.pop()
            print("\t     The book",x,"has been removed")
            delMore=input("\t     Remove more(y/n) ? ")
            if delMore.lower() !="y" and delMore.lower() !="n":
                print("\t\t     Wrong input")
                delMore=input("\t     Remove more(y/n) ? ")
    print("\t     Current book list : ",L)
    
def traversal():
    n=len(L)
    if L==[]:
        print("\t     List is empty nothing to print")
        add_or_not="y"
        while(add_or_not!="n"):
            add_or_not=input("\t     Insert some books(y/n) ? ")
            if add_or_not.lower()=="y":
                insert()
            elif add_or_not.lower()=="n":
                traversal()
            else:
                print("\t\t     Wrong input")
                add_or_not=input("\t     Insert book(y/n) ? ")
    else:
        print("*"*65)
        print("\t\t  Current list : ")
        for i in range(n-1,-1,-1):
            print("\t\t                ",L[i])
        print("*"*65)
choice=0
print("|----------------------EXPERIMENT NO.01-------------------------|")
print("|                       STACK OF BOOKS                          |")

while(choice!=4):
    print("-"*65)
    print("\t\t 1: Insert a book")
    print("\t\t 2: Remove a book")
    print("\t\t 3: Print current list")
    print("\t\t 4: EXIT")
    try:
        choice=int(input("\t\t Enter your choice : "))
        if choice==1:
            insert()
        elif choice==2:
            remove()
        elif choice==3:
            traversal()
        elif choice!=1 and choice!=2 and choice!=3 and choice!=4:
            print("Wrong input; input numbers from 1 to 4")
    except Exception as err2:
        print(err2)
else :
    print("\t\t-->Exiting loop")
