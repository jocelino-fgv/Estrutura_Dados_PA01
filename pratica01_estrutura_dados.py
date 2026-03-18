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
lista.insert_end(10)
lista.insert_end(20)
lista.imprimir()
        
                
