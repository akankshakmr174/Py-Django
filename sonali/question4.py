stack=[]
while True:
    print"1.push"
    print "2.pop"
    print "3.insert"
    print "4.exit"
    c=raw_input("enter ur choices: ")
    if int(c)==1:
        k=raw_input("enter a number to be pushed: ")
        stack.append(int(k))
        print "stack is containing... ",stack
    elif int(c)==2:
        stack.pop(len(stack)-1)
        print "stack is containing... ",stack
    elif int(c)==3:
        l=raw_input("enter index to be inserted: ")
        h=raw_input("enter the number to be inserted: ")
        stack.insert(int(l)-1,int(h))
        print "stack is containing... ",stack
    else:
        break
