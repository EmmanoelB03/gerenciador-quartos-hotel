class Node:
    def __init__(self,room,guest):
        self.room = room
        self.guest = guest
        self.next = None


class StackInfoGuest():
    def __init__(self):
        """
        Inicializa uma pilha para armazenar informações de hóspedes.
        """
        self.top = None
        self.size = 0

    def push(self,room,guest):
        """
        Adiciona um novo hóspede no topo da pilha.
        
        Args:
            room: Número do quarto.
            guest: Nome do hóspede.
        """
        newNode = Node(room, guest)
        if self.top is None:
            self.top = newNode
            self.size += 1
        else:
            newNode.next = self.top
            self.top = newNode
            self.size += 1

    def pop(self):
        """
        Remove o elemento do topo da pilha.
        """
        if self.size > 0:
            self.top = self.top.next
            self.size -= 1
        else:
            print('Pilha vazia')

    def peek(self):
        """
        Exibe as informações do hóspede no topo da pilha.
        """
        if self.size > 0:
            print(f'Quarto: {self.top.room} | Hosp: {self.top.guest}')
        else:
            print('Pilha vazia')

    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        
        Returns:
            True se a pilha estiver vazia, False caso contrário.
        """
        if self.size > 0:
            return False
        else:
            return True

    def return_room(self):
        """
        Retorna o número do quarto no topo da pilha.
        
        Returns:
            Número do quarto do hóspede no topo da pilha.
        """
        return self.top.room

    def return_guest(self):
        """
        Retorna o nome do hóspede no topo da pilha.
        
        Returns:
            Nome do hóspede no topo da pilha.
        """
        return self.top.guest