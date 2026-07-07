import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM livro")

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

cursor.close()
conexao.close()