def push(x):
    if len(list)>10:
        print("stack is full") 
    else:    
        list.append(x)
        print(list)
def pop():
    if len(list)==0:
        print("stack is empty")
    else:
        print(list.pop())
        return list
list=[1,2,3,4]
choice=int(input("enter choice : 0 for exit 1 for push and 2 for pop:"))
while choice!=0:
    
    if choice==1:
        print("enter the element")
        x=int(input())
        push(x)
    else:
        pop()
    choice=int(input("enter choice : 0 for exit 1 for push and 2 for pop:"))
