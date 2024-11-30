delete = {
    "atendimentoproduto": ("""
        DELETE FROM AtendimentoProduto 
        WHERE id_atendimento IN (
            SELECT id_atendimento 
            FROM Atendimento 
            WHERE id_nota_venda IN (
                SELECT id_nota_venda 
                FROM NotaVenda 
                WHERE valor < 150
            )
        );
    """),
    "atendimento": ("""
        DELETE FROM Atendimento 
        WHERE id_nota_venda IN (
            SELECT id_nota_venda 
            FROM NotaVenda 
            WHERE valor < 150
        );
    """),
    "notavenda": ("""
        DELETE FROM NotaVenda 
        WHERE valor < 150;
    """),
    "notacompraproduto": ("""
        DELETE FROM NotaCompraProduto 
        WHERE id_nota_compra IN (1, 2, 3, 4, 5, 6);
    """),
    "notacompra": ("""
        DELETE FROM NotaCompra 
        WHERE data < '2024-08-01';
    """),
    "produto": ("""
        DELETE FROM Produto 
        WHERE id_tipo_produto IN (SELECT id_tipo_produto FROM TipoProduto WHERE descricao = 'Cama ou Abrigo');
        DELETE FROM Produto WHERE qtde_estoque = 0;
    """),
    "raca": ("""
        DELETE FROM Raca 
        WHERE id_raca NOT IN (SELECT DISTINCT id_raca FROM Animal);
    """),
    "cliente": ("""
        DELETE FROM Cliente 
        WHERE id_cliente IN (
            SELECT id_cliente 
            FROM NotaVenda 
            WHERE valor < 100
        );
    """),
    "especie": ("""
        DELETE FROM Especie 
        WHERE id_especie NOT IN (SELECT DISTINCT id_especie FROM Raca);
    """),
    "tipoproduto": ("""
        DELETE FROM TipoProduto 
        WHERE id_tipo_produto NOT IN (SELECT DISTINCT id_tipo_produto FROM Produto);
    """),
    "tiposervico": ("""
        DELETE FROM TipoServico 
        WHERE id_tipo_servico NOT IN (SELECT DISTINCT id_tipo_servico FROM Servico);
    """),
    "fornecedor": ("""
        DELETE FROM Fornecedor 
        WHERE id_fornecedor NOT IN (
            SELECT DISTINCT id_fornecedor
            FROM Produto
        );
    """),
}
