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
        elif(self.next==None):
            self.next=Node(v)
        else:
            self.next.push(v)
    
    def pop(self):
        if(self.is_empty()):
            print("stack is empty")
        elif(self.next.next==None):
            temp=self.next.value
            self.next=None
            return(temp)
        else:
            self.next.pop()
            
            