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
    if not conexao.is_connected():
        conexao.reconnect(attempts= 3, delay=2)

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livro")

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    livros = []

    for resultado in resultados:
        livros.append({
            "id": resultado[0],
            "titulo": resultado[1],
            "autor": resultado[2],
        })

    return jsonify(livros)

@app.get("/livros/<id>")
def get_livro(id):
    if not conexao.is_connected():
        conexao.reconnect(attemps= 3, delay =2)

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livro WHERE id = %s", (id,))

    resultado = cursor.fetchone()
    
    if not resultado:
        return {"error": "Livro não encontrado."}, 404
    
    livro = [{
            "id": resultado[0],
            "titulo": resultado[1],
            "autor": resultado[2],
            "ano": resultado[3],
            "categoria": resultado[4]
     }]


    cursor.close
    conexao.close

  
    return jsonify(livro)


        










if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)