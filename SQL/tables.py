tables = {
    "TipoFuncionario" : ("""
        CREATE TABLE IF NOT EXISTS TipoFuncionario (
            id_tipo_funcionario Integer PRIMARY KEY,
            descricao Varchar(100) NOT NULL,
            salario Numeric(7,2) NOT NULL,
            CONSTRAINT tipo_funcionario_unico UNIQUE (descricao)
        );
    """),
    "Funcionario" : ("""
        CREATE TABLE IF NOT EXISTS Funcionario (
            id_funcionario Integer PRIMARY KEY,
            cpf Varchar(100) NOT NULL,
            nome Varchar(100) NOT NULL,
            id_tipo_funcionario Integer,
            FOREIGN KEY(id_tipo_funcionario) REFERENCES TipoFuncionario (id_tipo_funcionario),
            CONSTRAINT funcionario_unico UNIQUE (cpf)
        );
    """),
    "Fornecedor" : ("""
        CREATE TABLE IF NOT EXISTS Fornecedor (
            id_fornecedor Integer PRIMARY KEY,
            nome Varchar(100) NOT NULL,
            email Varchar(100) NOT NULL
        );
    """),
    "TipoServico" : ("""
        CREATE TABLE IF NOT EXISTS TipoServico (
            id_tipo_servico Integer PRIMARY KEY,
            descricao Varchar(100) NOT NULL,
            CONSTRAINT tipo_servico_unico UNIQUE (descricao)
        );
    """),
    "TipoProduto" : ("""
        CREATE TABLE IF NOT EXISTS TipoProduto (
            id_tipo_produto Integer PRIMARY KEY,
            descricao Varchar(100) NOT NULL,
            CONSTRAINT tipo_produto_unico UNIQUE (descricao)
        );
    """),
    "Especie" : ("""
        CREATE TABLE IF NOT EXISTS Especie (
            nome Varchar(100) NOT NULL,
            id_especie Integer PRIMARY KEY,
            CONSTRAINT especie_unico UNIQUE (nome)
        );
    """),
    "Cliente" : ("""
        CREATE TABLE IF NOT EXISTS Cliente (
            nome Varchar(100) NOT NULL,
            id_cliente Integer PRIMARY KEY,
            endereco Varchar(100),
            telefone Varchar(100)
        );
    """),
    "Raca" : ("""
        CREATE TABLE IF NOT EXISTS Raca (
            id_raca Integer PRIMARY KEY,
            nome Varchar(100) NOT NULL,
            id_especie Integer,
            FOREIGN KEY(id_especie) REFERENCES Especie (id_especie),
            CONSTRAINT raca_unico UNIQUE (nome)
        );
    """),
    "Animal" : ("""
        CREATE TABLE IF NOT EXISTS Animal (
            id_animal Integer PRIMARY KEY,
            nome Varchar(100) NOT NULL,
            peso Numeric(4,2) NOT NULL,
            id_raca Integer,
            id_cliente Integer,
            FOREIGN KEY(id_raca) REFERENCES Raca (id_raca),
            FOREIGN KEY(id_cliente) REFERENCES Cliente (id_cliente)
        );
    """),
    "Produto" : ("""
        CREATE TABLE IF NOT EXISTS Produto (
            id_produto Integer PRIMARY KEY,
            qtde_estoque Integer NOT NULL,
            nome Varchar(100) NOT NULL,
            valor Numeric(6,2) NOT NULL,
            id_fornecedor Integer,
            id_tipo_produto Integer,
            FOREIGN KEY(id_fornecedor) REFERENCES Fornecedor (id_fornecedor),
            FOREIGN KEY(id_tipo_produto) REFERENCES TipoProduto (id_tipo_produto),
            CONSTRAINT produto_unico UNIQUE (nome)
        );
    """),
    "NotaCompra" : ("""
        CREATE TABLE IF NOT EXISTS NotaCompra (
            id_nota_compra Integer PRIMARY KEY,
            valor Numeric(6,2) NOT NULL,
            data Timestamp NOT NULL,
            id_funcionario Integer,
            FOREIGN KEY(id_funcionario) REFERENCES Funcionario (id_funcionario)
        );
    """),
    "Servico" : ("""
        CREATE TABLE IF NOT EXISTS Servico (
            id_servico Integer PRIMARY KEY,
            valor Numeric(6,2),
            descricao Varchar(100) NOT NULL,
            id_tipo_servico Integer,
            FOREIGN KEY(id_tipo_servico) REFERENCES TipoServico (id_tipo_servico),
            CONSTRAINT servico_unico UNIQUE (descricao)
        );
    """),
    "NotaCompraProduto" : ("""
        CREATE TABLE IF NOT EXISTS NotaCompraProduto (
            qtde Integer NOT NULL,
            id_nota_compra Integer,
            id_produto Integer,
            PRIMARY KEY(id_nota_compra,id_produto),
            FOREIGN KEY(id_nota_compra) REFERENCES NotaCompra (id_nota_compra),
            FOREIGN KEY(id_produto) REFERENCES Produto (id_produto)
        );
    """),
    "NotaVenda" : ("""
        CREATE TABLE IF NOT EXISTS NotaVenda (
            id_nota_venda Integer PRIMARY KEY,
            data Timestamp NOT NULL,
            valor Numeric(7,2) NOT NULL,
            id_cliente Integer,
            FOREIGN KEY(id_cliente) REFERENCES Cliente (id_cliente)
        );
    """),
    "Atendimento" : ("""
        CREATE TABLE IF NOT EXISTS Atendimento (
            id_atendimento Integer PRIMARY KEY,
            id_nota_venda Integer,
            id_servico Integer,
            id_animal Integer,
            data Timestamp NOT NULL,
            valor_total Numeric(6,2) NOT NULL,
            id_funcionario Integer,
            FOREIGN KEY(id_nota_venda) REFERENCES NotaVenda (id_nota_venda),
            FOREIGN KEY(id_servico) REFERENCES Servico (id_servico),
            FOREIGN KEY(id_animal) REFERENCES Animal (id_animal),
            FOREIGN KEY(id_funcionario) REFERENCES Funcionario (id_funcionario)
        );
    """),
    "AtendimentoProduto" : ("""
        CREATE TABLE IF NOT EXISTS AtendimentoProduto (
            qtde Integer NOT NULL,
            id_produto Integer,
            id_atendimento Integer,
            PRIMARY KEY(id_produto,id_atendimento),
            FOREIGN KEY(id_produto) REFERENCES Produto (id_produto),
            FOREIGN KEY(id_atendimento) REFERENCES Atendimento (id_atendimento)
        );
    """),
}
