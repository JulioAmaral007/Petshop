from Funcao import funcoes as fc

try:
    fc.connect()
    fc.dropTables()
    opcao = 1

    while True:  # Loop principal do menu
        print("""\n       ---MENU---
        1.  Operações
        2.  Consultas
        0.  Desconectar do Banco de Dados\n """)
        
        try:
            choice = int(input("Opção: "))
            if choice == 0:
                print("Desconectando...")
                fc.exitDB()
                break
            elif choice == 1:
                fc.operacoesMenu()
            elif choice == 2:
                fc.consultasMenu()
            else:
                print("Opção inválida. Escolha entre 0 e 2.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

except fc.psycopg2.Error as err:
    print("Não foi possível se conectar ao Banco de Dados devido ao seguinte erro: \n", err.args)

