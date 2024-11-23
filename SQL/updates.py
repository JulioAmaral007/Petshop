updates = {
    "tipofuncionario": ("""
        UPDATE TipoFuncionario
        SET salario = salario * 1.1
        WHERE id_tipo_funcionario IN (1, 2, 3);
    """),
    "funcionario": ("""
        UPDATE Funcionario
        SET nome = 'João da Silva'
        WHERE id_funcionario = 7;
    """),
    "fornecedor": ("""
        UPDATE Fornecedor
        SET email = 'novoemail@pethigiene.com.br'
        WHERE id_fornecedor = 8;
    """),
    "tiposervico": ("""
        UPDATE TipoServico
        SET descricao = 'Serviços Veterinários'
        WHERE id_tipo_servico = 2;
    """),
    "tipoproduto": ("""
        UPDATE TipoProduto
        SET descricao = 'Itens Higiênicos para Pets'
        WHERE id_tipo_produto = 10;
    """),
    "especie": ("""
        UPDATE Especie
        SET nome = 'Cachorro'
        WHERE id_especie = 1;
    """),
    "cliente": ("""
        UPDATE Cliente
        SET endereco = 'Arroio do Silva, Avenida Principal, Centro, 111'
        WHERE id_cliente = 3;
    """),
    "raca": ("""
        UPDATE Raca
        SET nome = 'Bulldog Inglês'
        WHERE id_raca = 4;
    """),
    "animal": ("""
        UPDATE Animal
        SET peso = 9.00
        WHERE id_animal = 1;
    """),
    "produto": ("""
        UPDATE Produto
        SET qtde_estoque = qtde_estoque - 10
        WHERE id_produto IN (6, 7, 8);
    """),
    "notacompra": ("""
        UPDATE NotaCompra
        SET valor = valor + 50
        WHERE id_nota_compra = 1;
    """),
    "servico": ("""
        UPDATE Servico
        SET descricao = 'Banho e Tosa Premium'
        WHERE id_servico = 2;
    """),
    "notacompraproduto": ("""
        UPDATE NotaCompraProduto
        SET qtde = 15
        WHERE id_nota_compra = 1;
    """),
    "notavenda": ("""
        UPDATE NotaVenda
        SET valor = 350.00, data = '2024-11-20'
        WHERE id_nota_venda = 5;
    """),
    "atendimento": ("""
        UPDATE Atendimento
        SET data = '2024-08-01'
        WHERE id_atendimento = 6;

    """),
    "atendimentoproduto": ("""
        UPDATE AtendimentoProduto
        SET qtde = 2
        WHERE id_atendimento = 5;
    """),
}
