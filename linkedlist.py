class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, initial_data=None):
        """
        Inicializa uma lista encadeada.
        
        Args:
            initial_data: Lista opcional de elementos para inicializar a lista encadeada.
        """
        self.head = None
        self.size = 0
        if initial_data:
            for item in initial_data:
                self.append(item)

    def __iter__(self):
        """
        Permite iterar sobre os elementos da lista encadeada.
        
        Yields:
            Os dados de cada nó da lista.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def append(self, data):
        """
        Adiciona um novo elemento ao final da lista.
        
        Args:
            data: Dado a ser adicionado na lista.
        """
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.size += 1

    def remove(self, data):
        """
        Remove a primeira ocorrência de um elemento da lista.
        
        Args:
            data: Dado a ser removido da lista.
        """
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
        """
        Remove e retorna o último elemento da lista.
        
        Returns:
            O dado do último nó removido ou None se a lista estiver vazia.
        """
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
        """
        Retorna o último elemento da lista sem removê-lo.
        
        Returns:
            O dado do último nó ou None se a lista estiver vazia.
        """
        if self.is_empty():
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data

    def is_empty(self):
        """
        Verifica se a lista está vazia.
        
        Returns:
            True se a lista estiver vazia, False caso contrário.
        """
        return self.size == 0

    def view(self):
        """
        Retorna uma representação em string da lista encadeada.
        
        Returns:
            String representando todos os elementos da lista.
        """
        r = ''
        current = self.head
        while current:
            r = r + str(current.data) + ' -> '
            current = current.next
        return r + 'None'

    def ordenar(self):
        """
        Ordena os elementos da lista em ordem crescente usando bubble sort.
        """
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

    def merge_sort(self):
        """
        Ordena a lista encadeada usando o algoritmo Merge Sort.
        Complexidade: O(n log n)
        """
        if self.size < 2:
            return
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
        """
        Função auxiliar recursiva para o Merge Sort.
        
        Args:
            head: Nó inicial da sublista a ser ordenada.
            
        Returns:
            Cabeça da lista ordenada.
        """
        if head is None or head.next is None:
            return head
        
        # Dividir a lista ao meio
        meio = self._get_middle(head)
        meio_next = meio.next
        meio.next = None
        
        # Ordenar recursivamente as duas metades
        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(meio_next)
        
        # Mesclar as duas metades ordenadas
        return self._merge(left, right)

    def _get_middle(self, head):
        """
        Encontra o nó do meio da lista usando técnica slow/fast pointer.
        
        Args:
            head: Nó inicial da lista.
            
        Returns:
            Nó do meio da lista.
        """
        if head is None:
            return head
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def _merge(self, left, right):
        """
        Mescla duas listas ordenadas em uma única lista ordenada.
        
        Args:
            left: Cabeça da primeira lista ordenada.
            right: Cabeça da segunda lista ordenada.
            
        Returns:
            Cabeça da lista mesclada e ordenada.
        """
        if left is None:
            return right
        if right is None:
            return left
        
        # Escolher o menor elemento como cabeça
        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)
        
        return result