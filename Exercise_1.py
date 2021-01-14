class myStack:
     def __init__(self):
          self.s = list()
         
     def isEmpty(self):
         return len(self.s)!= null

     def push(self, item):
         self.s.append(item)

     # -1 represent last variable (LIFO)
     def pop(self):
        return self.s.pop(-1)
        
     def peek(self):
          return self.s[-1]
        
     def size(self):
          return len(self.s)
         
     def show(self):
          print(self.s)
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
s.show()
s.push('3')
s.show()
