class Node:
    def __init__(self,v=None):
        self.value=v
        self.next=None
    
    def is_empty(self):
        if(self.value==None):
            return True
        else:
            return False
    
    def push(self,v=None):
        if(self.value==None):
            self.value=v
            return
        newNode=Node(v)
        (newNode.value,self.value)=(self.value,newNode.value)
        (newNode.next,self.next)=(self.next,newNode)
    
    def pop(self):
        if(self.is_empty()):
            print("stack is empty")
            return
        temp=self.value
        (self.value,self.next.value)=(self.next.value,self.value)
        (self.next,self.next.next)=(self.next.next,None)
        return(temp)

            
            