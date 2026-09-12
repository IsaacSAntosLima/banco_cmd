from flask import jsonify, request, Blueprint

from services.livros import find_all, find_by_id, create_livro, update_livro, delete_livro
from schemas.schemas import *

livros_bp = Blueprint("livros", __name__)

DESCRICAO = "serviço de api para biblioteca"
VERSAO = "1.1"

@livros_bp.get("/livros/info")
def get_info():
    return jsonify(descricao=DESCRICAO, versao=VERSAO)

@livros_bp.get("/livros")
def get_livros():
    livros = find_all() or []

    return response_success(livros)

@livros_bp.get("/livros/<int:livro_id>")
def get_livro(livro_id):
    livro = find_by_id(livro_id) or []

    return response_success(livro)

@livros_bp.post("/livros")
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

    create_livro(titulo, autor, ano_publicacao, fk_categoria_id)
    return response_created()

@livros_bp.put("/livros/<int:livro_id>")
def put_livro(livro_id):

    dados = request.get_json()

    titulo = dados["titulo"]
    autor = dados["autor"]
    ano_publicacao = dados["ano_publicacao"]
    fk_categoria_id = dados["fk_categoria_id"]

    update_livro(titulo, autor, ano_publicacao, fk_categoria_id, livro_id)

    return response_updated()

@livros_bp.delete("/livros/<int:livro_id>")
def del_livro(livro_id):

    delete_livro(livro_id)

    return response_deleted()