class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, initial_data=None):
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

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
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
        if self.size <= 0:
            print('Lista vazia')
            return
        
        if self.size == 1:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            data = current.next.data
            current.next = None
            self.size -= 1
            return data
    
    def peek(self):
        if self.is_empty():
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data
    
    def is_empty(self):
        return self.size == 0
        
    def view(self):
        r = ''
        current = self.head
        while current:
            r = r + str(current.data) + ' -> '
            current = current.next
        return r + 'None'

    def ordenar(self):
        if self.size < 2:
            return

        trocou_algo = True
        while trocou_algo:
            trocou_algo = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    trocou_algo = True
                current = current.next


