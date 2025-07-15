# remember to do enqueue at tail and dequeue at head as this s the only way to get O(1) if done ulta we will get O(n) for dequeue

class Node:
    def __init__(self,v=None):
        self.value=v
        self.next=None
        
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def is_empty(self):
        if(self.head==None):
            return(True)
        else:
            return(False)
    
    def enqueue(self,v):
        if(self.is_empty()):
            newNode=Node(v)
            self.head=newNode
            self.tail=newNode
            return
        else:
            newNode=Node(v)
            self.tail.next=newNode
            self.tail=self.tail.next
            return
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
            return None
        else:
            value=self.head.value
            self.head=self.head.next
            if(self.is_empty()):
                self.tail=None
            return(value)
            
            
            