class Dado:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None


class Elos:
    def __init__(self):
        self.head = None

    def insert_end(self, valor):
        new_node = Dado(valor)
        if self.head is None:
            self.head = new_node
            return
        atual = self.head
        while atual.next:
            atual = atual.next
        atual.next = new_node
        new_node.prev = atual

    def buscar_viz(self):
        sv = "sem vizinho"
        atual = self.head
        while atual:
            if atual.valor != nome:
                atual = atual.next
                #if atual.next is None:

            else:
                if atual.prev:
                    atual_prev = atual.prev.valor
                else:
                    atual_prev = sv
                if atual.next:
                    atual_next = atual.next.valor
                else:
                    atual_next = sv
                print(f"Os vizinhos de {atual.valor} são: {atual_prev} à esquerda e à direita {atual_next}")
                return
        print("Nome não localizado")

    # def insert_begin(self, valor):
    #     new_node = Node(valor)
    #     new_node.next = self.head
    #     self.head = new_node
    #
    # def insert_end(self, valor):
    #     new_node = Node(valor)
    #     if self.head is None:
    #         self.head = new_node
    #         return

    def imprimir(self):
            atual = self.head
            while atual:
                if atual.prev:
                    atual_prev = atual.prev.valor
                else:
                    atual_prev = None
                if atual.next:
                    atual_next = atual.next.valor
                else:
                    atual_next = None

                print(atual_prev, atual.valor, atual_next)
                atual = atual.next



lista = Elos()
# lista.insert_end("João")
# lista.insert_end("Pedro")
# lista.insert_end("Maria")
# lista.insert_end("Carlos")
lista.buscar_viz()
#lista.imprimir()

def mostrar_menu():
    print("\n--- MENU ---")
    print("(1) Inserir morador(a)")
    print("(2) Buscar vizinhos de um dado morador")
    print("(3) Ver moradores cujos vizinhos foram buscados")
    print("(4) Finalizar execução")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        nome_morador = input("Cadastrar morador, informe o nome: ")
        lista.insert_end(nome_morador)
    elif opcao == '2':
        nome = input("Informe o nome do morador ")
        lista.buscar_viz()
    elif opcao == '3':
        hist_busca_moradores = input("Informe o nome do morador")
    elif opcao == '4':
        print("Encerrando, até breve.")
        break
    else:
        print("Opção inválida! Tente novamente.")


