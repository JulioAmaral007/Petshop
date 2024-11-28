import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
from IPython.display import display, Markdown

df = pd.read_csv("df_usar_trab.csv")
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

# Gemini_Key=userdata.get('GEMINI_AI_KEY_GENAI')
genai.configure(api_key='GEMINI_AI_KEY_GENAI')

model = genai.GenerativeModel('gemini-1.5-flash')
dados_json = df.to_json()
dados_json

contexto = f"""Estava analisando dados de um dataset com o obejtivo de identificar padrões úteis nos atendimentos de um petshop. Com isto em vista, gerei clusters para analisa-los.
                as colunas deste dataset são:
                -id_atendimento: id do atendimento, apenas para níveis de organiuzação;
                -data_venda: Data da venda, no caso do atendimento envolver venda de um produto;
                -valor_venda: Valor da venda, no caso do atendimento envolver venda de um produto;
                -descricao_servico: Serviço oferecido;
                -valor_servico: Valor do serviço oferecido;
                -nome_animal: Nome do animal;
                -peso_animal: Peso do animal;
                -nome_cliente: Nome do cliente, dono do animal atendido;
                -nome_funcionario: Nome do funcionário que atendeu o cliente;
                -cpf_funcionario: CPF do funcionário que atendeu o cliente;
                -data_atendimento: Data do atendimento;
                -valor_total_atendimento: Valor total do atendimento;
                -cluster: Cluster da tupla na sua totalidade;

                Note que seu objetivo é identificar qual ou quais colunas são mais determinantes para o rótulo do cluster, quero entender qual critério o algoritmo aderiu
                ao gerar os clusters. Ao identificar as colunas principais, se for o caso, diga a que faixa cada cluster se enquadra.
                Aqui estão os dados na forma de JSON:
                {dados_json}
                """
contexto

intrucoes = """Use os dados fornecidos e obedeça o prompt do usuário, gere inferencias e use métricas como desvio padrão e correlação, trate os dados se necessário"""
user_prompt = """Com base no contexto fornecido e seguindo as instruções dadas, descubra o critério adotado pelo algoritmo k-means para gerar clusters dos meus dados."""

response = model.generate_content(f"{user_prompt} \n Intrucões:{intrucoes} \n Contexto:{contexto}")
display(Markdown(response.text))