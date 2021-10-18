"""
    SQLite: usando o módulo sqlite3
"""
import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

'''
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')'''

''' 
cursor.execute("INSERT INTO clientes (nome,peso) VALUES ('João Inácio', 90.8)")
cursor.execute("INSERT INTO clientes (nome,peso) VALUES (?, ?)", ('Maria', 50))
cursor.execute("INSERT INTO clientes (nome,peso) VALUES (:nome, :peso)", {'nome': 'José', 'peso': 75})
cursor.execute("INSERT INTO clientes VALUES (:id, :nome, :peso)", {'id': None, 'nome': 'Paulo', 'Peso': 65})
conexao.commit()'''

# Atualizando registro
'''
cursor.execute("UPDATE clientes SET nome=:nome WHERE id=:id", {'nome': 'Ana', 'id': 2})
conexao.commit()'''

# Deletando registro
'''
cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 2})
conexao.commit()
'''
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 80})

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)


cursor.close()
conexao.close()
