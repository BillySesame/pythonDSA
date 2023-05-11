class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class SLinkedList:
    def __init__(self):
        self.head = None

    def listPrint(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next
        

linkedList = SLinkedList()
monday = Node("Monday")
tuesday = Node("Tuesday")
wednesday = Node("Wednesday")
linkedList.head = monday
linkedList.head.next = tuesday
linkedList.head.next.next = wednesday

linkedList.listPrint()