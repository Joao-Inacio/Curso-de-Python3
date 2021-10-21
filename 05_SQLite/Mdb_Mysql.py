"""
    CRUD com Pymysql no MySQL e Mariadb Server
"""
import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('conexao fechada')
        conexao.close()

# Insere um registro na base de dados
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 19, 75))
        conexao.commit()"""
# Insere varios registros na base de dados
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        dados = [
            ('João', 'Inácio', 22, 100),
            ('Inatiele', 'Aparecida', 22, 70),
            ('Inatiana', 'Silva', 21, 75),
        ]
        cursor.executemany(sql, dados)
        conexao.commit()"""
# Deleta um registro da base de dados
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id = %s'
        cursor.execute(sql, (6,))
        conexao.commit()"""
# Deleta Varios registros da base de dados
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
        cursor.execute(sql, (7, 8, 9))
        conexao.commit()"""
# deleta registra entre um range
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        cursor.execute(sql, (7,9))
        conexao.commit()"""
# Atualizar um registro na base de dados
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Joana', 5))
        conexao.commit()"""

# Seleciona na base de dados
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha['id'], linha['nome'], linha['sobrenome'], linha['idade'], linha['peso'])
