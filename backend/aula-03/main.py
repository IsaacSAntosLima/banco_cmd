import mysql.connector                  
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request

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

@app.post("/livros")
def post_livro():

    dados = request.get_json()

    if not dados:
        return{"mensagem":"lista vazia"}

    if not dados["titulo"]:
        return{"mensagem":"titulo é obrigatorio!"}

    if not dados["autor"]:
        return{"mensagem":"autor é obrigatorio!"}

    if not dados["ano_publicacao"]:
        return{"mensagem":"ano da publicação é obrigatorio!"}

    if not dados["fk_categoria_id"]:
        return{"mensagem":"a categoria é obrigatoria!"}

    if len(dados)!= 4:
        return{"mensagem":"atributos inexistentes"}

    titulo = dados["titulo"]
    autor = dados["autor"]
    ano_publicacao = dados["ano_publicacao"]
    fk_categoria_id = dados["fk_categoria_id"]

    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO livro (
            titulo,
            autor,
            ano_publicacao,
            fk_categoria_id
        )
            VALUES(%s,%s,%s,%s)
            """, (
            titulo,
            autor,
            ano_publicacao,
            fk_categoria_id
            )
    )
    conexao.commit()
    return{"mensagem":"Livro cadastrada com sucesso"},201

@app.put("/livros/<id>")
def put_livro(id):
    dados = request.get_json()

    titulo = dados["titulo"]
    autor = dados["autor"]
    ano_publicacao = dados["ano_publicacao"]
    fk_categoria_id = dados["fk_categoria_id"]
    
   
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE livro 
        SET titulo = %s,
        autor = %s,
        ano_publicacao = %s,
        fk_categoria_id = %s
        WHERE id = %s
    """, (
        titulo,
        autor,
        ano_publicacao,
        fk_categoria_id,
        id
    )
    )
    conexao.commit()
    if cursor.rowcount == 0:
            return{"Erro":"livro não encontrado"},404
    return{"mensagem": "livro atualizado"}, 200

@app.delete("/livros/<id>")
def delete_livro(id):
    conexao = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE"),
    )
    cursor = conexao.cursor()
    cursor.execute(
      "DELETE FROM livro WHERE id = %s",
      (id,)
    )
    conexao.commit()
    if cursor.rowcount == 0:
        return{"Erro":"livro não encontrado"},404
    return{"mensagem":"livro excluido com sucesso"},201









if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)