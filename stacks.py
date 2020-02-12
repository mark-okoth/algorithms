class stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)


    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def sizeStack(self):
        return len(self.stack)
    
    
stack = stack()   

stack.push(1)
stack.push(14)
stack.push(147)
stack.push(1888)

print(stack.sizeStack())

print("removed items", stack.pop())
print('peek item', stack.peek())
print(stack.sizeStack())



 
 
          