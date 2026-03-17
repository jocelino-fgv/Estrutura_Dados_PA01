class Node:
    def __init__(self, valor ):
        self.valor = valor
        self.next = None


class Encadeamento:
    def  __init__(self):
        self.head = None

    def insert_begin(self, valor):
        new_node = Node(valor)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, valor):
        new_node = Node(valor)
        if self.head is None:
            self.head = new_node
            return

        atual = self.head

        while atual.next:
           atual = atual.next
        atual.next = new_node

    def trocar_ultimo_primeiro(self):

        if self.head is None or self.head.next is None:
            return

        prev = None
        atual = self.head

        while atual.next:
            prev = atual
            atual = atual.next

        # atual = último
        # prev = penúltimo

        prev.next = self.head
        atual.next = self.head.next
        self.head.next = None
        self.head = atual

    def imprimir(self):
            atual = self.head
            while atual:
                print(atual.valor, end=" ->")
                atual = atual.next
            print("None")



lista = Encadeamento()
lista.insert_begin(10)
lista.insert_begin(7)
lista.insert_begin(23)
lista.insert_end(45)
lista.trocar_ultimo_primeiro()
lista.imprimir()
lista.trocar_ultimo_primeiro()
lista.imprimir()
lista.trocar_ultimo_primeiro()
lista.imprimir()