class Queue:
    def __init__(self):
        self.content = [] 
    def add(self,value):
        self.content.append(value)
    def pop(self):
        self.content.pop(0)
    
    
queue = Queue()
queue.add('a')
queue.add('b')
queue.add('c')
queue.pop()
print(queue.content)
