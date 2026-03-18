# def mostrar_menu():
#     print("\n--- MENU ---")
#     print("1. Cadastrar")
#     print("2. Visualizar")
#     print("3. Sair")

# while True:
#     mostrar_menu()
#     opcao = input("Escolha uma opção (1-3): ")

#     if opcao == '1':
#         print("Opção 1: Cadastrando...")
#         # Lógica de cadastro aqui
#     elif opcao == '2':
#         print("Opção 2: Visualizando...")
#         # Lógica de visualização aqui
#     elif opcao == '3':
#         print("Saindo... Até logo!")
#         break # Encerra o loop, fechando o programa
#     else:
#         print("Opção inválida! Tente novamente.")


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
        nome = "Pedro"
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
lista.insert_end("João")
lista.insert_end("Pedro")
lista.insert_end("Maria")
lista.insert_end("Carlos")
lista.buscar_viz()
#lista.imprimir()
        
                
