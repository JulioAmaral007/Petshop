total_genero = ("""
    SELECT genero.nome, SUM(res.quantidade) AS total_genero 
    FROM genero JOIN(
	    SELECT jogo.id_jogo, jogo_genero.id_genero, COUNT(jogo_genero.id_genero) AS quantidade 
        FROM jogo JOIN jogo_genero
	    ON jogo.id_jogo = jogo_genero.id_jogo
	    GROUP BY jogo.id_jogo, jogo_genero.id_genero
	    ) AS res
    ON res.id_genero = genero.id_genero
    GROUP BY genero.nome
    ORDER BY total_genero DESC
""")

total_gasto_usuario = ("""
    SELECT usr.nickname, SUM(res.total) AS total_gasto FROM usuario AS usr JOIN
	    (SELECT DISTINCT comp.valor AS total, comp.id_usuario FROM compra AS comp 
	    JOIN compra_jogo AS comp_jg
	    ON comp.id_compra = comp_jg.id_compra
	    )AS res
    ON usr.id_usuario = res.id_usuario
    GROUP BY usr.nickname
    ORDER BY total_gasto DESC
""")

total_expansoes_vendidas = ("""
    SELECT expansao.nome, SUM(expansao.valor) AS total FROM expansao JOIN
	    (SELECT comp.id_compra, comp_exp.id_expansao FROM compra AS comp 
	    JOIN compra_expansao AS comp_exp
	    ON comp.id_compra = comp_exp.id_compra AND comp_exp.data_compra between '2023-01-01 00:00:01' and '2023-12-31 00:00:59'
        )AS res
    ON expansao.id_expansao = res.id_expansao
    GROUP BY expansao.nome
    ORDER BY total DESC
""")

total_raridade = ("""
        SELECT usuario.nickname, SUM(rar.qtd) AS total_raridades FROM usuario JOIN 
        (SELECT item.id_usuario, item_raridade.id_raridade, COUNT(item_raridade.id_raridade) AS qtd FROM item
        JOIN item_raridade ON item.id_item = item_raridade.id_item AND item_raridade.id_raridade >= 3
        GROUP BY item.id_usuario, item_raridade.id_raridade ORDER BY item.id_usuario
        ) AS rar
    ON usuario.id_usuario = rar.id_usuario
    GROUP BY usuario.nickname
    ORDER BY total_raridades DESC 
""")

