from flask import jsonify, Blueprint, request

from services.alunos import find_all, find_by_id, create_aluno, update_aluno, delete_aluno
from schemas.schemas_alunos import *

alunos_bp = Blueprint("alunos", __name__)

DESCRICAO = "serviço de api para biblioteca"
VERSAO = "1.2"

@alunos_bp.get("/alunos/info")
def get_info():
    return jsonify(descricao= DESCRICAO, versao = VERSAO)

@alunos_bp.get("/alunos")
def get_alunos():
    alunos = find_all() or []

    return response_success_a(alunos)

@alunos_bp.get("/alunos/<int:aluno_id>")
def get_aluno(aluno_id):
    aluno = find_by_id(aluno_id) or []

    return response_success_a(aluno)

@alunos_bp.post("/alunos")
def post_aluno():
    dados = request.get_json()

    nome = dados["nome"]
    curso = dados["curso"]
    idade = dados["idade"]

    create_aluno(nome,curso,idade)
    return response_created_a()

@alunos_bp.put("/alunos/<int:aluno_id>")
def put_aluno(aluno_id):
    dados = request.get_json()
    
    nome = dados["nome"]
    curso = dados["curso"]
    idade = dados["idade"]

    update_aluno(nome,curso,idade, aluno_id)
    
    return response_updated_a()

@alunos_bp.delete("/alunos/<int:aluno_id>")
def del_aluno(aluno_id):

    delete_aluno(aluno_id)

    return response_deleted_a()