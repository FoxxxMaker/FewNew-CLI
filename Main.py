# esta parte é a interface gráfica do CLI.
'''
parte que receberá as importações futuras

'''

class Menu():
    def Menu_Principal():
        # Definindo o menu (primeira parte)
        print("Iniciando Programa....")
        print("Olá! Bem-vindo ao FewNew!")

        print(" ")

        print("Pressione a tecla N para receber uma ideia nova!")

        answer = input()

        if answer.lower() == 'N':
            # resposta dos arquivos que ainda serão editados
            print("Ideia para base:")
            print("Faça amigos!")
        elif answer.lower() != 'n':
            print("Por favor, digite apenas N.")
            # Aqui virá outro menu resumido