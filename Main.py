# esta parte é a interface gráfica do CLI.

import Tradutor as Tr
import Request as RQ


class Menu():
    def menu_simplificado():
        # Definindo o menu (segunda validação mais simples para ser mais direto ao ponto)
        print(" ")

        print("Pressione a tecla ENTER para receber uma ideia nova ou digite sair para sair")

        answer = input("Pressione Enter ou sair....")

        if not answer:
            # Chama o método (buscar_atividade) para puxar uma resposta da API
            atividade = RQ.buscar_atividade()
            # Chama o método (traduzir_texto) para fazer a tradução com a biblioteca translate
            traducao = Tr.Traduzir_texto(atividade)

            print(" ")

            print(traducao) # Dá a tradução em português brazil

            print(" ")

            print("Deseja continuar?")
            print("s/n")
            answer = input("Digite s para sim ou n para não....")
            
            if answer.upper() == 'S':
                Menu.menu_simplificado()
            elif answer.lower() == 'N':
                print("Saindo do Programa...")

       
        

    def Menu_Principal():
        # Definindo o menu (parte da primeira validação)
        print("Iniciando Programa....")
        print("Olá! Bem-vindo ao FewNew!")

        print(" ")

        print("Pressione a tecla ENTER para receber uma ideia nova ou digite sair para sair")

        answer = input("Pressione Enter ou sair....")

        atividade = RQ.buscar_atividade()
        traducao = Tr.Traduzir_texto(atividade)

        print(" ")

        print(traducao)

        print(" ")

        print("Deseja continuar?")
        print("s/n")
        answer = input("Digite s para sim ou n para não....")
            
        if answer.upper() == 'S':
            Menu.menu_simplificado()
        elif answer.lower() == 'N   ':
            print("Saindo do Programa...")


Menu.Menu_Principal()

# Este código pega a resposta da api contida no código request.py, traduz usando o código Tradutor.py e por fim 
# Imprime na tela. O usuário pode escolher se quer continuar ou sair do programa. Caso nãop queira usa-lo mais.