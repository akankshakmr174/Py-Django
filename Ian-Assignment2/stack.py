stack=[]
choice=1

def push_to_stack(stack):   #stack-push function
    data=raw_input("Enter the data")
    stack.append(data)
    return stack

def pop_from_stack(stack):  #stack-pop function
    l=len(stack)
    if l==0:
        print "Empty stack"
    else:
        stack.pop(l-1)
    return stack

def display(stack): #stack-display function
    for i in range(len(stack)):
        print stack[i]

while choice>=1 and choice<=3:
    print "1.Push"
    print "2.Pop"
    print "3.Display"
    choice=int(raw_input("Enter your choice"))
    if choice==1:
        stack=push_to_stack(stack)
    elif choice==2:
        stack=pop_from_stack(stack)
    elif choice==3:
        display(stack)
    else:
        print "Wrong choice!"
        break
