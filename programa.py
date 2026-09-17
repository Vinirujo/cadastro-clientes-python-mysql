import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexao.cursor()

nome = input("Digite o nome: ")
data_nacimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
email = input("Digite o email: ")

sql = """
INSERT INTO clientes (nome, data_nacimento, email)
VALUES (%s, %s, %s)
"""

dados = (nome, data_nacimento, email)
cursor.execute(sql, dados)
conexao.commit()

cursor.execute("SELECT * FROM clientes")

resultados = cursor.fetchall()

for cliente in resultados:
    print(cliente)