inserts = {
    "tipofuncionario": ("""
        insert into TipoFuncionario (id_tipo_funcionario, salario, descricao) values
        (1, 1500.00, 'Banhista/Tosador'),
        (2, 3500.00, 'Veterinário'),
        (3, 2500.00, 'Gerente'),
        (4, 1200.00, 'Recepcionista'),
        (5, 2200.00, 'Assistente Administrativo');
    """),
    "funcionario": ("""
        insert into Funcionario (id_funcionario, cpf, nome, id_tipo_funcionario) values
        (1, '12345678901', 'João Silva', 3),        -- Gerente (id_tipo_funcionario 4)
        (2, '23456789012', 'Maria Oliveira', 5),    -- Auxiliar (id_tipo_funcionario 6)
        (3, '34567890123', 'Carlos Pereira', 4),    -- Recepcionista (id_tipo_funcionario 5)
        (4, '45678901234', 'Ana Santos', 2),        -- Veterinário (id_tipo_funcionario 3)
        (5, '56789012345', 'Fernanda Costa', 1),    -- Banhista/Tosador 1 (id_tipo_funcionario 1)
        (6, '67890123456', 'Paulo Souza', 1),       -- Banhista/Tosador 2 (id_tipo_funcionario 1)
        (7, '78901234567', 'Juliana Martins', 1),   -- Banhista/Tosador 3 (id_tipo_funcionario 1)
        (8, '89012345678', 'Ricardo Lima', 1);      -- Banhista/Tosador 4 (id_tipo_funcionario 1)
    """),
    "fornecedor": ("""
        insert into Fornecedor (id_fornecedor, nome, email) values
        (1, 'PetHigiene Ltda', 'contato@pethigiene.com.br'),
        (2, 'Rações Top Pet', 'vendas@racoestoppet.com.br'),
        (3, 'Farmavet Saúde Animal', 'suporte@farmavet.com.br'),
        (4, 'Brinquedos Pet Fun', 'comercial@petfun.com.br'),
        (5, 'Acessórios Animais Plus', 'info@animaisplus.com.br'),
        (6, 'PetModa Fashion', 'atendimento@petmoda.com.br'),
        (7, 'Abrigos e Cia', 'contato@abrigosecia.com.br'),
        (8, 'PetTransporte Seguros', 'vendas@pettransporte.com.br');
    """),
    "tiposervico": ("""
        insert into TipoServico (id_tipo_servico, descricao) values 
        (1, 'Higiênico'), -- Serviços de higiene
        (2, 'Veterinário'), -- Serviços relacionados à saúde
        (3, 'Hospedagem'), -- Serviços de acomodação
        (4, 'Transporte'), -- Serviços de transporte de animais
        (5, 'Comercial'); --Serviços de vendas da loja
    """),
    "tipoproduto": ("""
        insert into TipoProduto (id_tipo_produto, descricao) values
        (1, 'Higiênico'),
        (2, 'Alimento'),
        (3, 'Medicamento'),
        (4, 'Brinquedo'),
        (5, 'Acessório'),
        (6, 'Roupa'),
        (7, 'Cama ou Abrigo'),
        (8, 'Item de Transporte');
    """),
    "especie": ("""
        insert into Especie (id_especie, nome) values
        (1, 'Canino'),
        (2, 'Felino'),
        (3, 'Ave'),
        (4, 'Peixe'),
        (5, 'Roedor');
    """),
    "cliente": ("""
        insert into Cliente (id_cliente, nome, endereco, telefone) values 
        (1, 'João Silva', 'Araranguá, Rua das Flores, Centro, 123', '48999451234'),
        (2, 'Maria Oliveira', 'Araranguá, Rua São João, Cidade Alta, 456', '48999455678'),
        (3, 'Carlos Pereira', 'Arroio do Silva, Avenida Beira Mar, Centro, 789', '48999457890'),
        (4, 'Ana Santos', 'Araranguá, Rua das Palmeiras, Mato Alto, 321', '54999451234'),
        (5, 'Fernanda Costa', 'Criciúma, Avenida Universitária, Centro, 654', '54999456789'),
        (6, 'Paulo Souza', 'Arroio do Silva, Rua do Pescador, Centro, 987', '48999456789'),
        (7, 'Juliana Martins', 'Criciúma, Rua das Orquídeas, São Luiz, 112', '54999457890'),
        (8, 'Ricardo Lima', 'Sombrio, Rua Principal, Centro, 556', '54999455678'),
        (9, 'Mariana Rocha', 'Sombrio, Rua das Hortências, Centro, 778', '48999456780'),
        (10, 'Bruno Almeida', 'Arroio do Silva, Rua da Praia, Centro, 223', '48999453421'),
        (11, 'Laura Nascimento', 'Araranguá, Rua dos Pinheiros, Centro, 990', '54999454321'),
        (12, 'Tiago Fernandes', 'Criciúma, Avenida das Nações, Centro, 345', '48999457689'),
        (13, 'Carolina Ribeiro', 'Sombrio, Rua Nova Esperança, Centro, 567', '48999453456'),
        (14, 'Eduardo Gonçalves', 'Arroio do Silva, Rua do Sol, Centro, 878', '54999456754'),
        (15, 'Gabriela Mendes', 'Araranguá, Rua do Comércio, Centro, 767', '54999454320'),
        (16, 'André Duarte', 'Sombrio, Rua Santa Clara, Centro, 333', '48999456743'),
        (17, 'Patrícia Barros', 'Criciúma, Rua XV de Novembro, Centro, 899', '48999451239'),
        (18, 'Felipe Vasconcelos', 'Araranguá, Rua Independência, Jardim das Avenidas, 525', '54999459876'),
        (19, 'Renata Farias', 'Sombrio, Avenida Brasil, Centro, 141', '54999451222'),
        (20, 'Luciano Castro', 'Arroio do Silva, Rua das Gaivotas, Centro, 999', '48999454333');
    """),
    "raca": ("""
        insert into Raca (id_raca, nome, id_especie) values
        (1, 'Labrador', 1),
        (2, 'Poodle', 1),
        (3, 'Beagle', 1),
        (4, 'Bulldog Francês', 1),
        (5, 'Shih Tzu', 1),
        (6, 'SRD Cão', 1), 
        (7, 'Yorkshire', 1),
        (8, 'Dachshund', 1),
        (9, 'Cocker Spaniel', 1),
        (10, 'Chihuahua', 1),
        (11, 'Pug', 1),
        (12, 'Boxer', 1),
        (13, 'Maltês', 1),
        (14, 'Schnauzer', 1),
        (15, 'Rottweiler', 1),
        (16, 'Persa', 2),
        (17, 'Siamês', 2),
        (18, 'Maine Coon', 2),
        (19, 'Bengal', 2),
        (20, 'Sphynx', 2),
        (21, 'SRD Gato', 2), 
        (22, 'Calopsita', 3),
        (23, 'Periquito', 3),
        (24, 'Canário', 3),
        (25, 'Papagaio', 3),
        (26, 'Agapornis', 3),
        (27, 'Betta', 4),
        (28, 'Guppy', 4),
        (29, 'Neon', 4),
        (30, 'Molly', 4),
        (31, 'Carpa', 4),
        (32, 'Hamster', 5),
        (33, 'Porquinho-da-Índia', 5),
        (34, 'Chinchila', 5),
        (35, 'Gerbil', 5);
    """),
    "animal": ("""
        insert into Animal (id_animal, peso, nome, id_raca, id_cliente) values
        (1, 8.50, 'Rex', 6, 1),   -- SRD (Cachorro vira-lata)
        (2, 5.20, 'Luna', 2, 2),  -- Poodle
        (3, 6.30, 'Max', 3, 2),   -- Beagle
        (4, 3.00, 'Bella', 6, 3), -- SRD (Cachorro vira-lata)
        (5, 4.80, 'Milo', 5, 4),  -- Shih Tzu
        (6, 7.00, 'Toby', 6, 4),  -- SRD (Cachorro vira-lata)
        (7, 2.00, 'Rex', 7, 5),   -- Yorkshire
        (8, 9.40, 'Tina', 8, 6),  -- Dachshund
        (9, 1.80, 'Piui', 22, 7), -- Calopsita
        (10, 0.50, 'Rico', 23, 7), -- Periquito
        (11, 0.25, 'Gigi', 24, 8), -- Canário
        (12, 1.20, 'Pipoca', 25, 9), -- Papagaio
        (13, 5.50, 'Simba', 21, 10), -- Gato SRD (Gato vira-lata)
        (14, 6.00, 'Luna', 21, 10),  -- Gato SRD (Gato vira-lata)
        (15, 4.00, 'Toby', 4, 11),  -- Bulldog Francês
        (16, 2.20, 'Dolly', 7, 12), -- Yorkshire
        (17, 8.50, 'Sasha', 8, 13), -- Dachshund
        (18, 7.50, 'Rocky', 9, 14), -- Cocker Spaniel
        (19, 0.30, 'Fufu', 32, 15), -- Hamster (Roedor)
        (20, 0.80, 'Nina', 20, 15), -- Agapornis
        (21, 0.60, 'Blue', 27, 16);  -- Betta (Peixe)
    """),
    "produto": ("""
        insert into Produto (id_produto, nome, valor, qtde_estoque, id_tipo_produto, id_fornecedor) values
        (1, 'Shampoo', 25.90, 50, 1, 1),
        (2, 'Tapete Higiênico', 45.00, 100, 1, 1),
        (3, 'Removedor de Odores', 30.50, 30, 1, 1),
        (4, 'Areia Higiênica para Gatos', 20.00, 80, 1, 1),
        (5, 'Filtro para Aquários', 70.00, 25, 1, 1),
        (6, 'Ração para Cães Adultos', 120.00, 200, 2, 2),
        (7, 'Ração para Gatos Filhotes', 95.00, 150, 2, 2),
        (8, 'Snacks para Animais', 15.00, 250, 2, 2),
        (9, 'Ração Úmida para Gatos', 7.50, 300, 2, 2),
        (10, 'Petisco Dentário para Cães', 20.00, 200, 2, 2),
        (11, 'Ração para Aves Pequenas', 25.00, 100, 2, 2),
        (12, 'Ração para Roedores', 30.00, 120, 2, 2),
        (13, 'Alimento Flocado para Peixes', 10.00, 300, 2, 2),
        (14, 'Shampoo Antipulgas para Cães', 45.00, 120, 3, 3),
        (15, 'Vermífugo para Gatos', 50.00, 100, 3, 3),
        (16, 'Pomada para Ferimentos', 35.00, 40, 3, 3),
        (17, 'Suplemento Vitamínico', 60.00, 80, 3, 3),
        (18, 'Antitóxico para Animais', 25.00, 60, 3, 3),
        (19, 'Vacina Antirrábica para Cães', 50.00, 150, 3, 3),
        (20, 'Vacina Polivalente para Gatos', 70.00, 100, 3, 3),
        (21, 'Vacina para Aves (Newcastle)', 30.00, 50, 3, 3),
        (22, 'Antibiótico para Peixes (uso em aquário)', 45.00, 40, 3, 3),
        (23, 'Vitamina C para Roedores', 15.00, 70, 3, 3),
        (24, 'Bola de Borracha', 20.00, 80, 4, 4),
        (25, 'Arranhador para Gatos', 150.00, 40, 4, 4),
        (26, 'Corda para Mastigar', 30.00, 60, 4, 4),
        (27, 'Escadinha para Aves', 35.00, 50, 4, 4),
        (28, 'Roda para Roedores', 60.00, 30, 4, 4),
        (29, 'Coleira Ajustável', 35.00, 100, 5, 5),
        (30, 'Guia Retrátil', 80.00, 50, 5, 5),
        (31, 'Peitoral para Cães', 120.00, 40, 5, 5),
        (32, 'Bebedouro para Aves', 25.00, 100, 5, 5),
        (33, 'Comedouro para Roedores', 20.00, 60, 5, 5),
        (34, 'Casaco para Inverno', 90.00, 30, 6, 6),
        (35, 'Camisa Estampada', 40.00, 50, 6, 6),
        (36, 'Botinha para Cães', 25.00, 20, 6, 6),
        (37, 'Cama Pequena para Cães', 150.00, 25, 7, 7),
        (38, 'Abrigo para Gatos', 180.00, 20, 7, 7),
        (39, 'Ninho para Aves', 60.00, 40, 7, 7),
        (40, 'Caixa de Transporte Pequena', 200.00, 15, 8, 8),
        (41, 'Bolsa para Animais', 150.00, 20, 8, 8),
        (42, 'Assento de Carro para Pets', 300.00, 10, 8, 8),
        (43, 'Caixa de Transporte para Aves', 120.00, 10, 8, 8),
        (44, 'Ração para Cães Filhotes', 130.00, 180, 2, 2), 
        (45, 'Ração para Gatos Adultos', 120.00, 150, 2, 2), 
        (46, 'Vermífugo para Cães Filhotes', 55.00, 90, 3, 3), 
        (47, 'Suplemento de Cálcio para Gatos', 50.00, 60, 3, 3), 
        (48, 'Vermífugo para Roedores', 40.00, 80, 3, 3), 
        (49, 'Antipulgas para Gatos', 45.00, 100, 3, 3), 
        (50, 'Vermífugo para Aves', 35.00, 50, 3, 3),
        (51, 'Vermífugo para Peixes', 60.00, 30, 3, 3),  
        (52, 'Filtro Biológico para Aquário', 90.00, 40, 5, 5),
        (53, 'Brinquedo para Cães Filhotes', 25.00, 150, 4, 4),
        (54, 'Brinquedo Interativo para Gatos', 45.00, 80, 4, 4), 
        (55, 'Piscina para Roedores', 70.00, 30, 4, 4), 
        (56, 'Comedouro Automático para Peixes', 80.00, 60, 5, 5),
        (57, 'Vacina V10 para Cães', 100.00, 50, 3, 3),
        (58, 'Vacina V8 para Cães', 85.00, 60, 3, 3),
        (59, 'Vacina Contra Tosse dos Canis (Bordetella)', 70.00, 80, 3, 3),
        (60, 'Vacina Contra Giardíase para Cães', 75.00, 40, 3, 3),
        (61, 'Vacina Quádrupla para Gatos', 90.00, 50, 3, 3),
        (62, 'Vacina Contra Leucemia Felina (FeLV)', 120.00, 40, 3, 3),
        (63, 'Vacina Contra Influenza Aviária para Aves', 40.00, 30, 3, 3),
        (64, 'Vacina para Doenças Respiratórias Aviárias', 50.00, 20, 3, 3),
        (65, 'Vacina Experimental Contra Doenças Intestinais para Roedores', 25.00, 10, 3, 3),
        (66, 'Vacina para Peixes - Prevenção de Doenças Comuns', 30.00, 15, 3, 3),
        (67, 'Vacina contra Parvovirose para Cães', 60.00, 120, 3, 3),
        (68, 'Vacina contra Hepatite Infecciosa para Cães', 70.00, 100, 3, 3),
        (69, 'Vacina contra Leptospirose para Cães', 55.00, 140, 3, 3),
        (70, 'Vacina contra Cinomose para Cães', 80.00, 90, 3, 3),
        (71, 'Vacina contra Leucemia Felina para Gatos', 75.00, 100, 3, 3),
        (72, 'Vacina contra Panleucopenia Felina para Gatos', 65.00, 120, 3, 3),
        (73, 'Vacina contra Rinotraqueíte Felina para Gatos', 50.00, 150, 3, 3),
        (74, 'Vacina contra Calicivírus Felino para Gatos', 60.00, 110, 3, 3),
        (75, 'Microchip para Cães', 80.00, 100, 3, 3), 
        (76, 'Microchip para Gatos', 70.00, 100, 3, 3);
    """),
    "notacompra": ("""
        insert into NotaCompra (id_nota_compra, valor, data, id_funcionario) values
        (1, 386.55, '2024-07-15', 1), -- Produtos Higiênicos (Fornecedor 2) 
        (2, 459.00, '2024-07-25', 2), -- Alimentos (Fornecedor 3) 
        (3, 531.00, '2024-08-10', 1), -- Medicamentos (Fornecedor 4)
        (4, 382.50, '2024-09-02', 1), -- Brinquedos (Fornecedor 5) 
        (5, 283.50, '2024-10-25', 2), -- Acessórios (Fornecedor 6) 
        (6, 328.50, '2024-11-15', 1); -- Medicamentos (Fornecedor 4 novamente) 
    """),
    "servico": ("""
        insert into Servico (id_servico, descricao, valor, id_tipo_servico) values
        (1, 'Banho', 50.00, 1),
        (2, 'Tosa Completa', 70.00, 1),
        (3, 'Corte de Unhas', 20.00, 1),
        (4, 'Limpeza de Ouvidos', 30.00, 1),
        (5, 'Consulta Geral', 100.00, 2),
        (6, 'Aplicação de Vacinas', 80.00, 2),
        (7, 'Exame de Sangue', 150.00, 2),
        (8, 'Microchipagem', 200.00, 2),
        (9, 'Diária Básica', 80.00, 3),
        (10, 'Diária com Recreação', 120.00, 3),
        (11, 'Hospedagem VIP', 200.00, 3),
        (12, 'Transporte para Consultas', 50.00, 4),
        (13, 'Transporte para Banho e Tosa', 40.00, 4),
        (14, 'Transporte para Hospedagem', 60.00, 4),
        (15, 'Venda de Produtos da Loja', 0.00, 5),
        (16, 'Banho Com Shampoo Antipulgas', 80.00, 1),
        (17, 'Tosa Higiênica', 40.00, 1),
        (18, 'Aparação de Asas', 40.00, 1),
        (19, 'Aparação de Bico', 30.00, 1), 
        (20, 'Exame Parasitológico de Aves', 70.00, 2), 
        (21, 'Banho a Seco', 50.00, 1),
        (22, 'Corte de Dentes', 20.00, 1), 
        (23, 'Manutenção de Aquário', 100.00, 1), 
        (24, 'Consulta Veterinária de Emergência', 150.00, 2),
        (25, 'Desparasitação', 70.00, 2);
    """),
    "notacompraproduto": ("""
        insert into NotaCompraProduto (id_nota_compra, id_produto, qtde) values
        (1, 1, 5), -- Shampoo
        (1, 14, 4), -- Shampoo Antipulgas
        (1, 4, 6), -- Areia Higiênica para Gatos
        (2, 45, 3), -- Ração para Gatos Adultos
        (2, 9, 10), -- Ração Úmida para Gatos
        (2, 8, 5), -- Snacks para Animais
        (3, 16, 5), -- Pomada para Ferimentos
        (3, 19, 5), -- Vacina Antirrábica para Cães
        (3, 69, 3), -- Vacina contra Leptospirose para Cães
        (4, 54, 3), -- Brinquedo Interativo para Gatos
        (4, 26, 5), -- Brinquedo para Mastigar
        (4, 55, 2), -- Piscina para Roedores
        (5, 29, 3), -- Coleira Ajustável
        (5, 30, 2), -- Guia Retrátil
        (5, 32, 2), -- Bebedouro para Aves
        (6, 18, 3), -- Antitóxico para Animais
        (6, 19, 3), -- Vacina Antirrábica para Cães
        (6, 68, 2); -- Vacina contra Hepatite Infecciosa para Cães
    """),
    "notavenda": ("""
        insert into NotaVenda (id_nota_venda, data, valor, id_cliente) values
        (1, '2024-07-15', 75.90, 3),
        (2, '2024-07-20', 70.00, 8),
        (3, '2024-07-20', 100.00, 3),
        (4, '2024-08-01', 150.00, 12),
        (5, '2024-08-05', 40.00, 7),
        (6, '2024-08-10', 100.00, 4),
        (7, '2024-08-12', 50.00, 15),
        (8, '2024-08-14', 185.90, 1),
        (9, '2024-08-18', 25.00, 18),
        (10, '2024-08-20', 105.00, 9),
        (11, '2024-08-25', 200.00, 11),
        (12, '2024-09-01', 125.00, 5),
        (13, '2024-09-05', 360.00, 16),
        (14, '2024-09-08', 100.00, 13),
        (15, '2024-09-08', 70.00, 6),
        (16, '2024-09-12', 40.00, 19),
        (17, '2024-09-15', 150.00, 4),
        (18, '2024-09-17', 270.00, 2),
        (19, '2024-09-20', 120.00, 20),
        (20, '2024-09-22', 275.00, 10),
        (21, '2024-10-02', 235.00, 3),
        (22, '2024-10-05', 30.00, 7),
        (23, '2024-10-05', 280.00, 14),
        (24, '2024-10-10', 70.00, 8),
        (25, '2024-10-12', 45.00, 17),
        (26, '2024-10-15', 175.00, 13),
        (27, '2024-10-18', 40.00, 9),
        (28, '2024-10-20', 235.00, 5),
        (29, '2024-10-22', 115.90, 12),
        (30, '2024-10-25', 400.00, 1);
    """),
    "atendimento": ("""
        insert into Atendimento (id_atendimento, id_nota_venda, id_servico, id_animal, id_funcionario, data, valor_total) values
        (1, 1, 1, 4, 5, '2024-07-15', 75.90), -- Cliente 3, Animal 4, Banho, Banhista/Tosador 1
        (2, 2, 20, 11, 4, '2024-07-20', 70.00), -- Cliente 8, Animal 11, Exame Parasitológico de Ave, Veterinario
        (3, 3, 5, 4, 4, '2024-07-20', 100.00), -- Cliente 3, Animal 4, Consulta Geral, Veterinario
        (4, 4, 7, 16, 4, '2024-08-01', 150.00), -- Cliente 12, Animal 16, Exame de Sangue, Veterinario
        (5, 5, 18, 9, 8, '2024-08-05', 40.00), -- Cliente 7, Animal 9, Aparação de Asas, Banhista/Tosador 4
        (6, 6, 9, 5, 5, '2024-08-10', 100.00), -- Cliente 4, Animal 5, Diária Básica, Banhista/Tosador 1
        (7, 7, 22, 19, 8, '2024-08-12', 20.00), -- Cliente 15, Animal 19, Corte de Dentes, Banhista/Tosador 4
        (8, 7, 19, 20, 8, '2024-08-12', 30.00), -- Cliente 15, Animal 20, Aparação de Bico, Banhista/Tosador 4
        (9, 8, 13, 1, 6, '2024-08-14', 40.00), -- Cliente 1, Animal 1, Transporte para Banho e Tosa, Banhista/Tosador 2
        (10, 8, 1, 1, 6, '2024-08-14', 75.90), -- Cliente 1, Animal 1, Banho, Banhista/Tosador 2
        (11, 8, 2, 1, 6, '2024-08-14', 70.00), -- Cliente 1, Animal 1, Tosa Completa, Banhista/Tosador 2
        (12, 9, 15, NULL, 3, '2024-08-18', 25.00), -- Cliente 18, Nenhum Animal, Venda de Produtos da Loja, Recepcionista
        (13, 10, 25, 12, 4, '2024-08-20', 105.00), -- Cliente 9, Animal 12, Desparasitação, Veterinario
        (14, 11, 6, 15, 4, '2024-08-25', 200.00), -- Cliente 11, Animal 15, Aplicação de Vacinas, Veterinario
        (15, 12, 16, 7, 5, '2024-09-01', 125.00), -- Cliente 5, Animal 7, Banho com Shampoo Antipulgas, Banhista/Tosador 1
        (16, 13, 15, NULL, 3, '2024-09-05', 230.00), -- Cliente 16, Nenhum Animal, Venda de Produtos da Loja, Recepcionista
        (17, 13, 25, 21, 4, '2024-09-05', 130.00), -- Cliente 16, Animal 21, Desparasitação, Veterinario
        (18, 14, 5, 17, 4, '2024-09-08', 100.00), -- Cliente 13, Animal 17, Consulta Geral, Veterinario
        (19, 15, 2, 8, 7, '2024-09-08', 70.00), -- Cliente 6, Animal 8, Tosa Completa, Banhista/Tosador 3
        (20, 16, 15, NULL, 3, '2024-09-12', 40.00), -- Cliente 19, Nenhum Animal, Venda de Produtos da Loja, Recepcionista
        (21, 17, 12, 6, 6, '2024-09-15', 50.00), -- Cliente 4, Animal 6, Transporte para Consultas, Banhista/Tosador 2
        (22, 17, 5, 6, 4, '2024-09-15', 100.00), -- Cliente 4, Animal 6, Consulta Geral, Veterinario
        (23, 18, 6, 2, 4, '2024-09-17', 135.00), -- Cliente 2, Animal 2, Aplicação de Vacinas, Veterinario
        (24, 18, 6, 2, 4, '2024-09-17', 135.00), -- Cliente 2, Animal 3, Aplicação de Vacinas, Veterinario
        (25, 19, 15, NULL, 3, '2024-09-20', 120.00), -- Cliente 20, Nenhum Animal, Venda de Produtos da Loja, Recepcionista
        (26, 20, 10, 13, 6, '2024-09-22', 127.50), -- Cliente 10, Animal 13, Diária com Recreação, Banhista/Tosador 2
        (27, 20, 10, 14, 6, '2024-09-22', 127.50), -- Cliente 10, Animal 14, Diária com Recreação, Banhista/Tosador 2
        (28, 20, 3, 14, 6, '2024-09-22', 20.00), -- Cliente 10, Animal 14, Corte de Unhas, Banhista/Tosador 2
        (29, 21, 19, 4, 8, '2024-10-01', 60.00), -- Cliente 3, Animal 4, Transporte para Hospedagem, Banhista/Tosador 4
        (30, 21, 9, 4, 8, '2024-10-01', 95.00), -- Cliente 3, Animal 4, Diária Básica, Banhista/Tosador 4
        (31, 21, 9, 4, 8, '2024-10-02', 80.00), -- Cliente 3, Animal 4, Diária Básica, Banhista/Tosador 4
        (32, 22, 19, 10, 6, '2024-10-05', 30.00), -- Cliente 7, Animal 10, Aparação de Bico, Banhista/Tosador 2
        (33, 23, 8, 18, 4, '2024-10-05', 280.00), -- Cliente 14, Animal 18, Microchipagem, Veterinario
        (34, 24, 20, 11, 4, '2024-10-10', 70.00), -- Cliente 8, Animal 11, Exame Parasitologico de Aves, Veterinario
        (35, 25, 15, NULL, 3, '2024-10-12', 45.00), -- Cliente 17, Nenhum Animal, Venda de Produtos da Loja, Recepcionista
        (36, 26, 24, 17, 4, '2024-10-15', 175.00), -- Cliente 13, Animal 17, Consulta de Emergência, Veterinario
        (37, 27, 18, 12, 5, '2024-10-18', 40.00), -- Cliente 9, Animal 12, Aparação de Asas, Banhista/Tosador 1
        (38, 28, 12, 7, 6, '2024-10-20', 50.00), -- Cliente 5, Animal 7, Transporte para Consulta, Banhista/Tosador 2
        (39, 28, 24, 7, 4, '2024-10-20', 185.00), -- Cliente 5, Animal 7, Consulta de Emergência, Veterinario
        (40, 29, 1, 16, 8, '2024-10-22', 75.90), -- Cliente 12, Animal 16, Banho, Banhista/Tosador 4
        (41, 29, 17, 16, 8, '2024-10-22', 40.00), -- Cliente 12, Animal 16, Tosa Higiência, Banhista/Tosador 4
        (42, 30, 5, 1, 4, '2024-10-25', 100.00), -- Cliente 1, Animal 1, Consulta Geral, Veterinario
        (43, 30, 3, 1, 6, '2024-10-25', 20.00), -- Cliente 1, Animal 1, Aparação de Unhas, Banhista/Tosador 2
        (44, 30, 8, 1, 4, '2024-10-25', 280.00); -- Cliente 1, Animal 1, Microchipagem, Veterinario
    """),
    "atendimentoproduto": ("""
        insert into AtendimentoProduto (id_atendimento, id_produto, qtde) values
        (1, 1, 1), -- Banho, Shampoo
        (6, 10, 1), -- Diária Básica, Petisco Dentário para Cães
        (10, 1, 1), -- Banho, Shampoo
        (12, 11, 1), -- Venda de Produtos da Loja, Ração para Aves Pequenas
        (13, 50, 1), -- Desparasitação, Vermífugo para Aves
        (14, 19, 1), -- Aplicação de Vacinas, Vacina Antirábica para Cães
        (14, 68, 1), -- Aplicação de Vacinas, Vacina contra Heptatite Infecciosa para Cães
        (15, 14, 1), -- Banho com Shampoo Antipulgas, Shampoo Antipulgas
        (16, 29, 2), -- Venda de Produtos da Loja, Coleira Ajustável
        (16, 30, 2), -- Venda de Produtos da Loja, Guia Retrátil
        (17, 51, 1), -- Desparasitação, Vermífugo para Peixes
        (20, 4, 2), -- Venda de Produtos da Loja, Areia Higiência para Gatos
        (23, 69, 1), -- Aplicação de Vacinas, Vacina contra Leptospirose para Cães
        (24, 69, 1), -- Aplicação de Vacinas, Vacina contra Leptospirose para Cães
        (25, 45, 1), -- Venda de Produtos da Loja, Ração para Gatos Adultos
        (26, 9, 1), -- Diária com Recreação, Ração Umida para Gatos
        (27, 9, 1), -- Diária com Recreação, Ração Umida para Gatos
        (27, 20, 1), -- Diária com Recreação, Areia Higiência para Gatos
        (30, 8, 1), -- Diária Básica, Snacks para Animais
        (33, 75, 1), -- Microchipagem, Microchip para Cães
        (35, 54, 1), -- Venda de Produtos da Loja, Brinquedo Interativo para Gatos	 
        (36, 18, 1), -- Consulta de Emergência, Antitóxico para Animais	
        (39, 16, 1), -- Consulta de Emergência, Pomada para Ferimentos
        (40, 1, 1), -- Banho, Shampoo
        (44, 75, 1); -- Microchipagem, Microchip para Cães
    """),
}
