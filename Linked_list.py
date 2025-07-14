class Node:
    def __init__ (self,v=None):
         self.value=v
         self.next=None
         
    def isempty(self):
        if(self.value==None):
            return(True)
        else:
            return(False)
    
    def append(self,v):
        if(self.value==None):
            self.value=v
        elif(self.next==None):
            self.next=Node(v)
        else:
            self.next.append(v)
        return
    
    def insert(self,v):
        if(self.isempty()):
            self.value=v
            return
        newNode=Node(v)
        (self.value,newNode.value)=(newNode.value,self.value)
        (self.next,newNode.next)=(newNode,self.next)
        
    def delete(self,v):
        if(self.value==v):
            self.value=None
            if(self.next!=None):
                self.value=self.next.value
                self.next=self.next.next
            return
        else:
            if(self.next!=None):
                self.next.delete(v)
                if self.next.value==None:
                    self.next=None
        return
            
        