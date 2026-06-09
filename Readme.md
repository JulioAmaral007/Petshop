# PetShop Manager

Sistema de gerenciamento de dados para petshop com banco de dados relacional e módulo de inteligência artificial para análise de padrões de atendimento.

---

## 🚀 Visão Geral

O **PetShop Manager** é um sistema de linha de comando desenvolvido para gerenciar as operações de um petshop. Ele centraliza o controle de clientes, animais, funcionários, fornecedores, produtos, serviços e atendimentos em um banco de dados relacional PostgreSQL.

Além do gerenciamento tradicional, o sistema conta com um módulo de IA que processa os dados de atendimento usando embeddings semânticos e clustering K-Means, e integra a API do Google Gemini para interpretar em linguagem natural os padrões encontrados nos dados.

**Público-alvo:** administradores e operadores de petshops que precisam de controle centralizado de dados e insights sobre os atendimentos.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Banco de Dados:** PostgreSQL (psycopg2)
- **Análise de Dados:** pandas, numpy
- **Visualização:** matplotlib, plotly, seaborn
- **Machine Learning:** scikit-learn (KMeans, PCA, cosine similarity), yellowbrick, pyod (ECOD), prince, lightgbm
- **Embeddings Semânticos:** sentence-transformers (`all-MiniLM-L6-v2`)
- **Grafos de Similaridade:** networkx
- **IA Generativa:** Google Gemini 1.5 Flash (`google-generativeai`)
- **Notebook Interativo:** Jupyter Notebook

---

## 🎯 Principais Funcionalidades

- **CRUD completo** para todas as 16 entidades do banco de dados
- **Criação e recriação automática** de tabelas e dados de teste
- **Atualização interativa** de registros via terminal (selecione a tabela, atributo e valor)
- **Visualização tabular** de qualquer tabela no terminal com pandas
- **3 consultas analíticas** com geração automática de gráficos de barras:
  - Receita total por cliente e funcionário responsável
  - Quantidade de produtos vendidos por tipo e fornecedor
  - Receita total por espécie de animal atendida
- **Módulo de IA** com pipeline completo de análise:
  - Geração de embeddings semânticos a partir dos dados de atendimento
  - Cálculo de matriz de similaridade coseno entre registros
  - Determinação do número ótimo de clusters via método do cotovelo (K-Elbow) e Silhouette
  - Clusterização K-Means com visualização PCA em 2D e 3D (interativo com Plotly)
  - Envio dos clusters ao Google Gemini para interpretação dos padrões em linguagem natural

---

## 🏗️ Arquitetura

O sistema é organizado em três camadas:

1. **Entrada (`main.py`)** — ponto de entrada da aplicação. Gerencia o loop de menu principal e trata erros de conexão ao banco.

2. **Lógica de negócio (`functions.py`)** — contém todas as funções: conexão, CRUD, consultas analíticas com gráficos e o pipeline completo de IA.

3. **Módulo SQL (`SQL/`)** — dicionários Python com todas as instruções DDL e DML organizadas por operação, carregadas dinamicamente pelas funções do sistema.

O fluxo principal: o usuário conecta ao PostgreSQL → navega pelo menu → executa operações ou consultas → opcionalmente aciona o módulo de IA, que lê o arquivo `db_ia.csv`, gera embeddings, clusteriza e consulta o Gemini.

---

## 📂 Estrutura do Projeto

```
petshop/
├── main.py              # Ponto de entrada; menu principal e loop de interação
├── functions.py         # Toda a lógica: conexão, CRUD, consultas e módulo de IA
├── ia.ipynb             # Notebook Jupyter com exploração interativa do módulo de IA
├── db_ia.csv            # Dataset exportado do banco para uso no pipeline de ML
├── SQL/
│   ├── tables.py        # Instruções CREATE TABLE para as 16 entidades
│   ├── inserts.py       # Dados de teste para popular o banco
│   ├── updates.py       # Instruções UPDATE de exemplo para todas as tabelas
│   ├── delete.py        # Instruções DELETE de exemplo para todas as tabelas
│   └── drop.py          # Instruções DROP TABLE CASCADE para limpeza do banco
└── Readme.md
```

---

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.12+
- PostgreSQL rodando localmente na porta `5432`
- Banco de dados `petshop` criado no PostgreSQL
- Usuário `postgres` com senha configurada

### Instalação

Clone o repositório e instale as dependências:

```bash
git clone <url-do-repositorio>
cd petshop
pip install psycopg2-binary pandas numpy matplotlib plotly seaborn scikit-learn sentence-transformers networkx pyod yellowbrick lightgbm prince google-generativeai markdown shap
```

Para o notebook Jupyter, instale adicionalmente:

```bash
pip install jupyter nbformat
```

### Configuração

Edite as credenciais de conexão em `functions.py` na função `connect()`:

```python
cnx = psycopg2.connect(
    host='localhost',
    port='5432',
    database='petshop',
    user='postgres',
    password='SUA_SENHA'
)
```

Para usar o módulo de IA, configure sua chave da API do Google Gemini na função `IA()` em `functions.py`:

```python
genai.configure(api_key='SUA_CHAVE_GEMINI')
```

### Execução

```bash
python main.py
```

O sistema conecta ao banco, recria as tabelas automaticamente e exibe o menu principal.

Para a exploração interativa com o notebook:

```bash
jupyter notebook ia.ipynb
```

---

## 🗄️ Banco de Dados

**PostgreSQL** com 16 tabelas relacionais:

| Tabela | Descrição |
|---|---|
| `TipoFuncionario` | Categorias de funcionários com salário base |
| `Funcionario` | Funcionários do petshop |
| `Fornecedor` | Fornecedores de produtos |
| `TipoServico` | Categorias de serviços (higiênico, veterinário, hospedagem, transporte, comercial) |
| `TipoProduto` | Categorias de produtos (higiene, alimento, medicamento, brinquedo, etc.) |
| `Especie` | Espécies de animais (canino, felino, ave, peixe, roedor) |
| `Cliente` | Dados dos clientes |
| `Raca` | Raças vinculadas às espécies |
| `Animal` | Animais dos clientes com peso e raça |
| `Produto` | Catálogo de produtos com estoque e valor |
| `Servico` | Catálogo de serviços com valor |
| `NotaCompra` | Notas fiscais de compra de estoque |
| `NotaCompraProduto` | Itens de cada nota de compra |
| `NotaVenda` | Notas fiscais de venda por cliente |
| `Atendimento` | Registro de cada atendimento (serviço + animal + funcionário + nota de venda) |
| `AtendimentoProduto` | Produtos utilizados em cada atendimento |

---

## 🤖 Módulo de Inteligência Artificial

O módulo de IA, disponível tanto via menu no terminal quanto no notebook `ia.ipynb`, executa o seguinte pipeline:

1. **Carregamento dos dados** — lê `db_ia.csv`, que contém registros de atendimentos com informações de serviço, animal, cliente e funcionário.

2. **Geração de embeddings** — cada atendimento é convertido em texto estruturado e codificado pelo modelo `all-MiniLM-L6-v2` da biblioteca sentence-transformers, gerando vetores de 384 dimensões.

3. **Matriz de similaridade coseno** — calcula a similaridade entre todos os pares de atendimentos, criando uma matriz 500×500.

4. **Determinação do número de clusters** — método do cotovelo (K-Elbow) e análise de Silhouette testam de 2 a 10 clusters.

5. **Clusterização K-Means** — agrupa os atendimentos em 4 clusters com visualização PCA em 2D e 3D via Plotly.

6. **Interpretação com IA generativa** — o dataset clusterizado é enviado ao Google Gemini 1.5 Flash, que identifica quais colunas são determinantes para cada cluster e descreve o critério adotado pelo algoritmo.

---

## 📈 Melhorias Futuras

- Interface web para substituir o menu de terminal
- Autenticação de usuários com controle de permissões por perfil
- Dashboard com relatórios automáticos e filtros por período
- Exportação de relatórios em PDF ou Excel
- Agendamento de atendimentos com calendário
- Controle automático de estoque com alertas de reposição
- Configuração de credenciais via variáveis de ambiente (`.env`)

---

## 👨‍💻 Desenvolvedor

**Desenvolvido por:**

- Júlio Cézar Rodrigues Pereira

---

## 📚 Contexto

Projeto acadêmico desenvolvido para a disciplina de **Banco de Dados** do curso de graduação. O sistema demonstra na prática a modelagem de banco de dados relacional com PostgreSQL, operações CRUD, consultas com junções e agregações, geração de visualizações a partir de dados relacionais e integração com técnicas de machine learning e IA generativa para análise de dados.
