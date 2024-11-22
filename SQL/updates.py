updates = {
    'funcionario': ("""
        UPDATE TipoFuncionario
        SET salario = 8500.00
        WHERE descricao = 'Veterinário';
    """),
    'cliente': ("""
        UPDATE Cliente
        SET endereco = 'Rua Nova, 789'
        WHERE nome = 'Carlos Mendes';
    """),
    'animal': ("""
        UPDATE Animal
        SET id_raca = 2
        WHERE id_cliente = 2 AND nome = 'Mimi';
    """),
    'produto': ("""
        UPDATE Produto
        SET valor = valor * 1.10
        WHERE id_fornecedor = 1;
    """),
    'notacompra': ("""
        UPDATE NotaCompra
        SET valor = valor * 0.95
        WHERE valor > 1000;
    """),
}