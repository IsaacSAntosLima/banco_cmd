import mysql.connector                  
import os
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)

conexao = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"),
)

DESCRICAO = "serviço de api para biblioteca"
VERSAO = "1.0"

@app.get("/info")
def get_info():
    return jsonify(descricao=DESCRICAO, versao=VERSAO)

@app.get("/livros")
def get_livros():
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livro")

    resultados = cursor.fetchall()

    livros = []

    for resultado in resultados:
        livros.append({
            "id": resultado[0],
            "titulo": resultado[1],
            "autor": resultado[2],
        })

    cursor.close()
    conexao.close()

    return livros 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)