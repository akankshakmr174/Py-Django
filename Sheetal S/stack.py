class Stack():
  
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    return self.items == []
    
  def push(self, item):
    return self.items.append(item)
	
  def insert(self, pos, item):
    return self.items.insert(pos,item)
  
  def pop(self, item):
    return self.items.pop(item)
  
  def getElements(self):
    return self.items

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(6)
stack.pop(3)
stack.insert(2,7)
print stack.getElements()