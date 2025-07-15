class Node:
    def __init__(self,v=None):
        self.value=v
        self.next=None
    
class Stack:
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        if(self.head==None):
            return True
        else:
            return False
    
    def push(self,v=None):
        newNode=Node(v)
        newNode.next=self.head
        newNode.value=v
        self.head=newNode
    
    def pop(self):
        if(self.is_empty()):
            print("stack is empty")
            return None
        value=self.head.value
        self.head=self.head.next
        return(value)

    def peek(self):
        if(self.is_empty()):
            print("stack is empty")
            return None
        value=self.head.value
        return(value)
            

# Example usage:
# s = Stack()
# s.push(10)
# s.push(20)
# print(s.pop())  # 20
# print(s.pop())  # 10
# print(s.pop())  # Stack is empty, returns None