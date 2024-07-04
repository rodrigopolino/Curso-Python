import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    #password='',
    database='bdyoutube',
)

cursor = conexao.cursor()

print("VENDAS")
print('----------------------------------')
nome_produto = input("Digite o nome do produto: ")
valor = int(input("Digite o valor: "))

#CRUD

#CREATE
"""
cursor.execute(f'''
INSERT INTO vendas (nome_produto, valor)
VALUES
("{nome_produto}", {valor})
''')
"""
conexao.commit() #edita o banco de dados

#READ
cursor.execute('SELECT * FROM vendas')
resultado = cursor.fetchall()  #ler o banco de dados
print(resultado) #lista de tuplas

#UPDATE
"""
cursor.execute(f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"')

conexao.commit() #edita o banco de dados
"""

#DELETE
cursor.execute(f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"')
conexao.commit() #edita o banco de dados

cursor.close()
conexao.close()