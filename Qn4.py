def push(st):
    item=raw_input("Enter item: ")
    st.append(item)
    return st
    
def pop(st):
    if len(st)==0:
        print "You can stop popping now. The stack is empty."
    else:
        st.pop()
    return st
    
def display(st):
    if len(st)==0:
        print "Stack is empty"
    else:
        print " ".join(st)
    
st=[]
ch=1
print "Start pushing items into the stack: "
while ch!=0:
    st=push(st)
    ch=int(raw_input("Enter 0 to stop pushing: "))

ch=1
print "Pop items now "
while ch!=0:
    st=pop(st)
    ch=int(raw_input("Enter 0 to stop popping: "))

display(st)
