import psycopg2
from SQL.tables import tables
from SQL.drop import drop
from SQL.inserts import inserts
from SQL.updates import updates
from SQL.delete import delete
import matplotlib.pyplot as plt
import pandas as pd
from settings import *

def connect():
    global cnx
    global cursor
    try:
        # Conectar ao banco padrão 'postgres' para garantir que possamos criar o banco de dados
        initial_cnx = psycopg2.connect(
            host=DB_HOST, 
            port=DB_PORT, 
            database='postgres',  # Conexão inicial ao banco padrão
            user=DB_USER, 
            password=DB_PASSWORD
        )
        initial_cnx.autocommit = True  # Necessário para executar CREATE DATABASE
        initial_cursor = initial_cnx.cursor()
        
        # Verificar se o banco de dados especificado existe
        initial_cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = initial_cursor.fetchone()

        if not exists:
            # Criar o banco de dados se não existir
            initial_cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Banco de dados '{DB_NAME}' criado com sucesso.")
        else:
            print(f"Banco de dados '{DB_NAME}' já existe.")
        
        # Fechar a conexão inicial
        initial_cursor.close()
        initial_cnx.close()

        # Estabelecer a conexão ao banco de dados desejado
        cnx = psycopg2.connect(
            host=DB_HOST, 
            port=DB_PORT, 
            database=DB_NAME, 
            user=DB_USER, 
            password=DB_PASSWORD
        )
        cnx.autocommit = False  # Controle manual do commit

        if cnx:
            print("Conectado ao servidor PostgreSQL")
            cursor = cnx.cursor()  # Criar o cursor para a conexão principal
            cursor.execute("SELECT current_database();")
            db_name = cursor.fetchone()
            print("Conectado ao banco de dados:", db_name[0])
        
        return cnx  # Retorna a conexão para ser usada em outras funções

    except psycopg2.Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

def exitDB():
    print("\n---EXIT DB---")
    cnx.close()
    print("Conexão ao PostgreSQL foi encerrada")

def operacoesMenu():
    while True:
        print("""\n       ---OPERAÇÕES---
        1.  CRUD
        2.  Criar todas as tabelas
        3.  Deletar todas as tabelas
        4.  Inserir teste
        5.  Atualizar teste
        6.  Deletar teste
        7.  Update valor
        8.  Mostrar tabela
        0.  Voltar\n """)

        try:
            option = int(input("Opção: "))
            if option == 0:
                break
            elif option == 1:
                crud()
            elif option == 2:
                createTables()
            elif option == 3:
                dropTables()
            elif option == 4:
                insertSQL()
            elif option == 5:
                updateSQL()
            elif option == 6:
                deleteSQL()
            elif option == 7:
                updateValue()
            elif option == 8:
                showTable()
            else:
                print("Escolha um valor entre 0 e 8.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def consultasMenu():
    while True:
        print("""\n       ---CONSULTAS---
        1. Receita total por cliente com dados de funcionários
        2. Quantidade de produtos vendidos por tipo de produto e fornecedor
        3. Despesa média por funcionário e tipo de serviço
        0. Voltar\n """)

        try:
            choice = int(input("Opção: "))
            
            if choice == 0:
                print("Voltando ao menu principal...")
                break
            
            elif choice == 1:
                print("Executando receita total por cliente com dados de funcionários...")
                consulta1()
            
            elif choice == 2:
                print("Executando quantidade de produtos vendidos por tipo de produto e fornecedor...")
                consulta2()
            
            elif choice == 3:
                print("Executando despesa média por funcionário e tipo de serviço...")
                consulta3()
            
            else:
                print("Escolha um valor entre 0 e 3.")
        
        except ValueError:
            print("Entrada inválida. Digite um número.")
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

def createTables():
    print("Iniciando criação das tabelas...")
    cursor = cnx.cursor()
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print("Criando tabela {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except psycopg2.Error as err:
            print(err)
        else:
            print("OK")
    cnx.commit()
    cursor.close()

def dropTables():
    print("Dropando tabelas...")
    cursor = cnx.cursor()
    for drop_name in drop:
        print(drop_name)
        drop_description = drop[drop_name]
        try:
            print("Deletando {}: ".format(drop_name), end='')
            cursor.execute(drop_description)
        except psycopg2.Error as err:
            print(err)
        else:
            print("OK")
    cnx.commit()
    cursor.close()

def insertSQL():
    print("Inserindo dados...")
    cursor = cnx.cursor()
    for insert_name in inserts:
        insert_description = inserts[insert_name]
        try:
            print("Inserindo valores para {}: ".format(insert_name), end='')
            cursor.execute(insert_description)
        except psycopg2.Error as err:
            print(err)
        else:
            print("OK")
    cnx.commit()
    cursor.close()

def updateSQL():
    print("Atualizando dados...")
    cursor = cnx.cursor()
    for update_name in updates:
        update_description = updates[update_name]
        try:
            print("Atualizando dados para {}: ".format(update_name), end='')
            cursor.execute(update_description)
        except psycopg2.Error as err:
            print(err)
        else:
            print("OK")
    cnx.commit()
    cursor.close()
        
def deleteSQL():
    print("Deletando dados")
    cursor = cnx.cursor()
    for delete_name in delete:
        delete_description = delete[delete_name]
        try:
            print("Deletando dados para {}: ".format(delete_name), end='')
            cursor.execute(delete_description)
        except psycopg2.Error as err:
            print(err)
        else:
            print("OK")
    cnx.commit()
    cursor.close()

def updateValue():
    print("Digite o nome da tabela que deseja atualizar: ")
    # Criação das tabelas
    cursor = cnx.cursor()
    for table_name in tables:
        print("Nome: {}".format(table_name))
    try:
        name = input(str("\nDigite o nome da tabela que deseja consultar. ")).upper()
        for table_name in tables:
            table_description = tables[table_name]
            if table_name == name:
                print("Para criar a tabela: {}, foi utilizado o seguinte código {}".format(table_name, table_description))
                
        atributo = input("Digite o atributo a ser alterado: ")
        valor = input("Digite o valor a ser atribuído: ")
        codigo_f = input("Digite a coluna da chave primária: ")
        codigo = input("Digite o valor numérico do campo da chave primária: ")

        query = f"update {name} set {atributo} = %s where {codigo_f} = %s;"
        cursor.execute(query, (valor, codigo))
        print("Atributo atualizado com sucesso!")
    except psycopg2.Error as err:
        print(err.msg)
    else:
        print("Atributo atualizado")
    cnx.commit()
    cursor.close()

def showTable():
    print("\nTabelas")
    # Criação das tabelas
    cursor = cnx.cursor()
    for table_name in tables:
        print("Nome: {}".format(table_name))
    try:
        name = input(str("\nDigite o nome da tabela que deseja consultar: ")).lower()
        query_colunas = "SELECT COLUMN_NAME FROM information_schema.columns WHERE TABLE_NAME = '{}' ORDER BY ORDINAL_POSITION;".format(name)
        cursor.execute(query_colunas)
        nomes_colunas = cursor.fetchall()
        colunas = list(sum(nomes_colunas, ()))
        query = "select * from " + name
        cursor.execute(query)
    except psycopg2.Error as err:
        print(err)
    else:
        print("TABELA {}".format(name))
        myresult = cursor.fetchall()
        data = pd.DataFrame(myresult, columns=colunas)
        print(data)
    cursor.close()

def consulta1():
    select_query = """
    SELECT 
        c.nome AS nome_cliente,
        f.nome AS nome_funcionario,
        SUM(nv.valor) AS receita_total
    FROM 
        Cliente c
    JOIN 
        NotaVenda nv ON c.id_cliente = nv.id_cliente
    JOIN 
        Atendimento a ON nv.id_nota_venda = a.id_nota_venda
    JOIN 
        Funcionario f ON a.id_funcionario = f.id_funcionario
    GROUP BY 
        c.nome, f.nome
    ORDER BY 
        receita_total DESC
    """
    print("\n Consulta 1: Receita Total por Cliente e Funcionário.")

    cursor = cnx.cursor()
    try:
        cursor.execute(select_query)
        myresult = cursor.fetchall()

        # Extraindo os dados para exibição no terminal
        clientes = [f"{row[0]} ({row[1]})" for row in myresult]  # Combina o nome do cliente com o nome do funcionário
        receita_total = [row[2] for row in myresult]

        # Criando um DataFrame para exibir os resultados tabulares
        data = pd.DataFrame({
            'Cliente (Funcionário)': clientes,
            'Receita Total (R$)': receita_total
        })

        # Exibindo a tabela de forma tabular no terminal
        print("\nResultado da Consulta:")
        print(data)

        # Gerando o gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(clientes, receita_total, color='skyblue')
        plt.xlabel('Cliente (Funcionário)')
        plt.ylabel('Receita Total (R$)')
        plt.title('Receita Total por Cliente e Funcionário')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Exibindo o gráfico
        plt.show()

    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

    cursor.close()

def consulta2():
    select_query = """
    SELECT 
        tp.descricao AS tipo_produto,
        f.nome AS nome_fornecedor,
        SUM(ap.qtde) AS total_vendido
    FROM 
        TipoProduto tp
    JOIN 
        Produto p ON tp.id_tipo_produto = p.id_tipo_produto
    JOIN 
        AtendimentoProduto ap ON p.id_produto = ap.id_produto
    JOIN 
        Fornecedor f ON p.id_fornecedor = f.id_fornecedor
    GROUP BY 
        tp.descricao, f.nome
    ORDER BY 
        total_vendido DESC
    """
    print("Consulta 2: Quantidade de Produtos Vendidos por Tipo e Fornecedor.")

    cursor = cnx.cursor()
    try:
        cursor.execute(select_query)
        myresult = cursor.fetchall()

        # Extraindo os dados para exibição no terminal
        produtos_fornecedores = [f"{row[0]} - {row[1]}" for row in myresult]  # Combina o tipo de produto com o fornecedor
        total_vendido = [row[2] for row in myresult]

        # Criando um DataFrame para exibir os resultados tabulares
        data = pd.DataFrame({
            'Tipo de Produto e Fornecedor': produtos_fornecedores,
            'Quantidade Vendida': total_vendido
        })

        # Exibindo a tabela de forma tabular no terminal
        print("\nResultado da Consulta:")
        print(data)

        # Gerando o gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(produtos_fornecedores, total_vendido, color='lightgreen')
        plt.xlabel('Tipo de Produto e Fornecedor')
        plt.ylabel('Quantidade Vendida')
        plt.title('Quantidade de Produtos Vendidos por Tipo e Fornecedor')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Exibindo o gráfico
        plt.show()

    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

    cursor.close()

def consulta3():
    select_query = """
    SELECT 
        f.nome AS nome_funcionario,
        ts.descricao AS tipo_servico,
        AVG(a.valor_total) AS despesa_media
    FROM 
        Funcionario f
    JOIN 
        Atendimento a ON f.id_funcionario = a.id_funcionario
    JOIN 
        Servico s ON a.id_servico = s.id_servico
    JOIN 
        TipoServico ts ON s.id_tipo_servico = ts.id_tipo_servico
    GROUP BY 
        f.nome, ts.descricao
    ORDER BY 
        despesa_media DESC
    """
    print("\nConsulta 3: Despesa Média por Funcionário e Tipo de Serviço.")

    cursor = cnx.cursor()
    try:
        cursor.execute(select_query)
        myresult = cursor.fetchall()

        # Extraindo os dados para exibição no terminal
        funcionarios_servicos = [f"{row[0]} - {row[1]}" for row in myresult]  # Combina o nome do funcionário com o tipo de serviço
        despesa_media = [row[2] for row in myresult]

        # Criando um DataFrame para exibir os resultados tabulares
        data = pd.DataFrame({
            'Funcionário e Tipo de Serviço': funcionarios_servicos,
            'Despesa Média (R$)': despesa_media
        })

        # Exibindo a tabela de forma tabular no terminal
        print("\nResultado da Consulta:")
        print(data)

        # Gerando o gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(funcionarios_servicos, despesa_media, color='lightcoral')
        plt.xlabel('Funcionário e Tipo de Serviço')
        plt.ylabel('Despesa Média (R$)')
        plt.title('Despesa Média por Funcionário e Tipo de Serviço')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Exibindo o gráfico
        plt.show()

    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

    cursor.close()

def crud():
    dropTables()
    createTables()
    insertSQL()

    print("\n---CONSULTAS BEFORE---")
    consulta1()
    consulta2()
    consulta3()

    updateValue()

    print("\n---CONSULTAS AFTER---")
    consulta1()
    consulta2()
    consulta3()