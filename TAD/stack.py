#vai servir para verificar o último hospede

class Node:
    def __init__(self,room,guest):
        self.room = room
        self.status = status
        self.guest = guest
        self.next = None

class StackInfoGuest():
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self,room,guest):
        newNode = Node(room, guest)

        if self.top is None:
            self.top = newNode
            self.size += 1
        else:

            newNode.next = self.top
            self.top = newNode
            self.size += 1

    def pop(self):

        if self.size > 0:
            self.top = self.top.next
            self.size -= 1
        else:
            print('Pilha vazia')

    def peek(self):

        if self.size > 0:
            print(f'Quarto: {self.top.room} | Status: {self.top.status} | Hosp: {self.top.guest}')

        else:
            print('Pilha vazia')

    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True
        
    def return_room(self):
        return self.top.room
    
    def return_guest(self):
        return self.top.guest


        

