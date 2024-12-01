import psycopg2
from SQL.tables import tables
from SQL.drop import drop
from SQL.inserts import inserts
from SQL.updates import updates
from SQL.delete import delete
import matplotlib.pyplot as plt
from settings import *
from IPython.display import display, Markdown
import pandas as pd
import numpy as np
import matplotlib.cm as cm
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import shap
from sklearn.cluster import KMeans
from sklearn.preprocessing import PowerTransformer, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score, silhouette_samples, accuracy_score, classification_report
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import networkx as nx
from pyod.models.ecod import ECOD
from yellowbrick.cluster import KElbowVisualizer
import lightgbm as lgb
import prince
# from google.colab import userdata
import google.generativeai as genai

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

import re

def remove_html_tags(text):
    # Remover tudo que está entre '<' e '>'
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

def IA():
    df = pd.read_csv("db_ia.csv")
    df.head()

    def compile_text(x):
        text =  f"""ID: {x['id_atendimento']},
                    Data da venda: {x['data_venda']},
                    Valor: {x['valor_venda']},
                    Exame: {x['descricao_servico']},
                    Valor: {x['valor_servico']},
                    Nome Animal: {x['nome_animal']},
                    Peso Animal: {x['peso_animal']},
                    Nome Cliente: {x['nome_cliente']}
                    Nome Funcionario: {x['nome_funcionario']}
                    CPF Funcionario: {x['cpf_funcionario']}
                    Data Atendimento: {x['data_atendimento']}
                    Valor Total: {x['valor_total_atendimento']}
                """

        return text

    def get_pca_2d(df, predict):
        pca_2d_object = prince.PCA(
        n_components=2,
        n_iter=3,
        rescale_with_mean=True,
        rescale_with_std=True,
        copy=True,
        check_input=True,
        engine='sklearn',
        random_state=42
        )

        pca_2d_object.fit(df)

        df_pca_2d = pca_2d_object.transform(df)
        df_pca_2d.columns = ["comp1", "comp2"]
        df_pca_2d["cluster"] = predict

        return pca_2d_object, df_pca_2d

    def get_pca_3d(df, predict):
        pca_3d_object = prince.PCA(
        n_components=3,
        n_iter=3,
        rescale_with_mean=True,
        rescale_with_std=True,
        copy=True,
        check_input=True,
        engine='sklearn',
        random_state=42
        )

        pca_3d_object.fit(df)

        df_pca_3d = pca_3d_object.transform(df)
        df_pca_3d.columns = ["comp1", "comp2", "comp3"]
        df_pca_3d["cluster"] = predict

        return pca_3d_object, df_pca_3d

    def plot_pca_3d(df, title = "PCA Space", opacity=0.8, width_line = 0.1):
        df = df.astype({"cluster": "object"})
        df = df.sort_values("cluster")

        fig = px.scatter_3d(df,
                            x='comp1',
                            y='comp2',
                            z='comp3',
                            color='cluster',
                            template="plotly",

                            # symbol = "cluster",

                            color_discrete_sequence=px.colors.qualitative.Vivid,
                            title=title).update_traces(
                                # mode = 'markers',
                                marker={
                                    "size": 4,
                                    "opacity": opacity,
                                    # "symbol" : "diamond",
                                    "line": {
                                        "width": width_line,
                                        "color": "black",
                                    }
                                }
                            ).update_layout(
                                    width = 1000,
                                    height = 800,
                                    autosize = False,
                                    showlegend = True,
                                    legend=dict(title_font_family="Times New Roman",
                                                font=dict(size= 20)),
                                    scene = dict(xaxis=dict(title = 'comp1', titlefont_color = 'black'),
                                                yaxis=dict(title = 'comp2', titlefont_color = 'black'),
                                                zaxis=dict(title = 'comp3', titlefont_color = 'black')),
                                    font = dict(family = "Gilroy", color  = 'black', size = 15))


        fig.show()

    def plot_pca_2d(df, title = "PCA Space", opacity=0.8, width_line = 0.1):
        df = df.astype({"cluster": "object"})
        df = df.sort_values("cluster")

        fig = px.scatter(df,
                            x='comp1',
                            y='comp2',
                            color='cluster',
                            template="plotly",
                            # symbol = "cluster",

                            color_discrete_sequence=px.colors.qualitative.Vivid,
                            title=title).update_traces(
                                # mode = 'markers',
                                marker={
                                    "size": 8,
                                    "opacity": opacity,
                                    # "symbol" : "diamond",
                                    "line": {
                                        "width": width_line,
                                        "color": "black",
                                    }
                                }
                            ).update_layout(
                                    width = 800,
                                    height = 700,
                                    autosize = False,
                                    showlegend = True,
                                    legend=dict(title_font_family="Times New Roman",
                                                font=dict(size= 20)),
                                    scene = dict(xaxis=dict(title = 'comp1', titlefont_color = 'black'),
                                                yaxis=dict(title = 'comp2', titlefont_color = 'black'),
                                                ),
                                    font = dict(family = "Gilroy", color  = 'black', size = 15))


        fig.show()

    def random_sample(df: pd.DataFrame, num_rows: int) -> pd.DataFrame:
        """
        Returns a DataFrame with a specific number of rows randomly selected.

        Parameters:
        df (pd.DataFrame): Original DataFrame.
        num_rows (int): Number of rows to be randomly sampled.

        Returns:
        pd.DataFrame: New DataFrame with the random rows.
        """
        if num_rows > len(df):
            raise ValueError(f"The number of requested rows ({num_rows}) exceeds the number of rows in the DataFrame ({len(df)}).")

        return df.sample(n=num_rows, random_state=42)

    def calculate_cosine_similarity(embeddings: list) -> np.ndarray:
        """
        Calculates the cosine similarity between each pair of embeddings.

        Parameters:
        embeddings (list): A list of n-dimensional embeddings (each embedding is a list or a numpy array).

        Returns:
        np.ndarray: A matrix where each element [i, j] represents the cosine similarity between embedding i and j.
        """
        # Convert the list of embeddings to a NumPy array (if not already)
        embeddings_array = np.array(embeddings)

        # Compute the cosine similarity matrix
        similarity_matrix = cosine_similarity(embeddings_array)

        return similarity_matrix

    def create_similarity_graph(similarity_matrix: np.ndarray, threshold: float) -> nx.Graph:
        """
        Creates an undirected graph from a similarity matrix where edges are formed
        between nodes with similarity greater than or equal to a given threshold.

        Parameters:
        similarity_matrix (np.ndarray): The matrix of cosine similarities.
        threshold (float): The minimum similarity value to create an edge.

        Returns:
        nx.Graph: An undirected graph where nodes are connected if their similarity is above the threshold.
        """
        # Create an empty undirected graph
        graph = nx.Graph()

        # Number of embeddings (nodes)
        num_nodes = similarity_matrix.shape[0]

        # Add nodes to the graph
        graph.add_nodes_from(range(num_nodes))

        # Add edges based on the similarity threshold
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if similarity_matrix[i, j] >= threshold:
                    graph.add_edge(i, j, weight=similarity_matrix[i, j])

        return graph

    sentences = df.apply(lambda x: compile_text(x), axis=1).tolist()
    sentences

    model = SentenceTransformer("all-MiniLM-L6-v2")
    output = model.encode(sentences=sentences,
            show_progress_bar=True,
            normalize_embeddings=True)

    embeddings = pd.DataFrame(output)
    print(embeddings)

    sim_matrix = calculate_cosine_similarity(embeddings)
    print(sim_matrix)
    print(sim_matrix.shape)

    km = KMeans(init="k-means++", random_state=0, n_init="auto")
    visualizer = KElbowVisualizer(km, k=(1,10), locate_elbow=False)

    visualizer.fit(embeddings)
    visualizer.show()

    from yellowbrick.cluster import SilhouetteVisualizer

    range_clusters = range(2, 11)
    visualizers = []

    for n_clusters in range_clusters:
        model = KMeans(n_clusters=n_clusters, random_state=42)
        visualizer = SilhouetteVisualizer(model)
        visualizer.fit(embeddings)
        visualizers.append(visualizer)
        visualizer.show()

    n_clusters = 4

    clusters = KMeans(n_clusters=n_clusters, init = "k-means++").fit(embeddings)
    clusters_predict = clusters.predict(embeddings)

    pca_3d_object, df_pca_3d = get_pca_3d(embeddings, clusters_predict)
    plot_pca_3d(df_pca_3d, title = "PCA Space", opacity=1, width_line = 0.1)

    pca_2d_object, df_pca_2d = get_pca_2d(embeddings, clusters_predict)
    plot_pca_2d(df_pca_2d, title = "PCA Space", opacity=1, width_line = 0.1)

    df['cluster'] = clusters.labels_
    df.head()

    genai.configure(api_key='GEMINI_AI_KEY_GENAI')

    model = genai.GenerativeModel('gemini-1.5-flash')

    # Supondo que 'df' seja o seu DataFrame
    dados_json = df.to_json()

    # Preparando o contexto com informações do dataset
    contexto = f"""
    Estava analisando dados de um dataset com o objetivo de identificar padrões úteis nos atendimentos de um petshop. Com isto em vista, gerei clusters para analisá-los.
    As colunas deste dataset são:
    - id_atendimento: ID do atendimento, apenas para níveis de organização;
    - data_venda: Data da venda, no caso do atendimento envolver venda de um produto;
    - valor_venda: Valor da venda, no caso do atendimento envolver venda de um produto;
    - descricao_servico: Serviço oferecido;
    - valor_servico: Valor do serviço oferecido;
    - nome_animal: Nome do animal;
    - peso_animal: Peso do animal;
    - nome_cliente: Nome do cliente, dono do animal atendido;
    - nome_funcionario: Nome do funcionário que atendeu o cliente;
    - cpf_funcionario: CPF do funcionário que atendeu o cliente;
    - data_atendimento: Data do atendimento;
    - valor_total_atendimento: Valor total do atendimento;
    - cluster: Cluster da tupla na sua totalidade.

    Note que seu objetivo é identificar qual ou quais colunas são mais determinantes para o rótulo do cluster, quero entender qual critério o algoritmo aderiu ao gerar os clusters. Ao identificar as colunas principais, se for o caso, diga a que faixa cada cluster se enquadra.
    Aqui estão os dados na forma de JSON:
    {dados_json}
    """

    # Definindo as instruções para o modelo
    instrucoes = """
    Use os dados fornecidos e obedeça o prompt do usuário, gere inferências e use métricas como desvio padrão e correlação, trate os dados se necessário.
    """

    # Definindo o prompt do usuário
    user_prompt = """
    Com base no contexto fornecido e seguindo as instruções dadas, descubra o critério adotado pelo algoritmo k-means para gerar clusters dos meus dados.
    """

    # Geração da resposta utilizando o modelo
    response = model.generate_content(f"{user_prompt}\nInstruções:{instrucoes}\nContexto:{contexto}")

    # Exibindo a resposta no formato Markdown
    import markdown

    # Converte o texto Markdown para HTML
    html_content = markdown.markdown(response.text)
    clean_text = remove_html_tags(html_content)
    print(clean_text)

