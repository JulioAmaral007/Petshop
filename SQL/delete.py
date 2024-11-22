delete = {
   'tipofuncionario': ("""
        DELETE FROM TipoFuncionario WHERE id_tipo_funcionario = 3;
    """),
    'cliente': ("""
        DELETE FROM Cliente WHERE telefone = '(11) 98765-4321';
    """),
    'fornecedor': ("""
        DELETE FROM Fornecedor WHERE nome = 'Fornecedor C';
    """),
    'produto': ("""
        DELETE FROM Produto WHERE id_produto = 5;
    """),
    'animal': ("""
        DELETE FROM Animal WHERE nome = 'Rex' AND id_cliente = 2;
    """),
    'servico': ("""
        DELETE FROM Servico WHERE descricao = 'Vacinação';
    """),
}