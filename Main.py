# esta parte é a interface gráfica do CLI.

import Tradutor as Tr

class Menu():
    def menu_simplificado():
        # Definindo o menu (segunda parte)
        print(" ")

        print("Pressione a tecla ENTER para receber uma ideia nova ou digite sair para sair")

        answer = input("Pressione Enter ou sair....")

        if not answer:
            print(Tr.tradu)
            print(" ")

            print("Deseja continuar?")
            print("s/n")
            answer = input("Digite s para sim ou n para não....")
            
            if answer.upper() == 'S':
                Menu.menu_simplificado()
            if answer.upper() == 'S':
                print("Saindo....")

        elif answer.lower() == "sair":
            print("Saindo do Programa...")

        print(Tr.tradu())
        

    def Menu_Principal():
        # Definindo o menu (parte da primeira validação)
        print("Iniciando Programa....")
        print("Olá! Bem-vindo ao FewNew!")

        print(" ")

        print("Pressione a tecla ENTER para receber uma ideia nova ou digite sair para sair")

        answer = input("Pressione Enter ou sair....")

        if not answer:
            print(Tr.tradu)
            print(" ")

            print("Deseja continuar?")
            print("s/n")
            answer = input("Digite s para sim ou n para não....")
            
            if answer.upper() == 'S':
                Menu.menu_simplificado()
            if answer.upper() == 'S':
                print("Saindo....")

        elif answer.lower() == "sair":
            print("Saindo do Programa...")

Menu.Menu_Principal()