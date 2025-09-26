from node import Node

class LinkedList:
    def __init__(self, initial_data = None):
        self.head = None
        self.size = 0

        if initial_data:
            for item in initial_data:
                self.append(item)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data 
            current = current.next

    def append(self,node):
        newNode = Node(node)
        if self.head is None:
            self.head = newNode
            self.size += 1

        else:
            current = self.head

            while current.next:
                current = current.next
            current.next = newNode
            self.size += 1

    def remove(self, data):

        if self.size == 0:
            print('Lista vazia')
            return
        
        else:
            current = self.head

            if self.head.data == data:
                self.head = self.head.next
                self.size -= 1
                
            else:
                while current.next:

                    if current.next.data == data:
                        current.next = current.next.next
                        self.size -= 1
                        return
                    
                    current = current.next

                print('Item não encontrado')




    def pop(self):

        if self.size < 0:
            print('Lista vazia')
            return
        
        current = self.head
        
        if self.size == 1:
            self.head = None
            self.size -= 1

        else:
            
            while current.next:

                if current.next.next is None:

                    current.next = None
                    return
                current = current.next
        
    def peek(self):

        current = self.head

        while current.next:
            current = current.next
        return current.data
    
    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True
    

    
        

        