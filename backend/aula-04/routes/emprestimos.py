from flask import Blueprint, request
from services.emprestimos import *
from schemas.schemas_emprestimos import *

emprestimos_bp = Blueprint("emprestimos", __name__)

@emprestimos_bp.get("/emprestimos")
def get_emprestimos():
    emprestimos = find_all() or []

    return response_success(emprestimos)

@emprestimos_bp.get("/emprestimos/abertos")
def get_emprestimo_abertos():
    emprestimos = find_abertos() or []

    return response_success(emprestimos)

@emprestimos_bp.get("/emprestimos/<int:emprestimo_id>")
def get_emprestimo(emprestimo_id):

    emprestimo = find_by_id(emprestimo_id) 
    if not emprestimo:
        return response_not_found("emprestimo não encontrado")

    return response_success(emprestimo)

@emprestimos_bp.post("/emprestimos")
def post_emprestimo():

    dados = request.get_json()

    if not dados:
        return response_bad_request("dados da requisição não encontrados")

    aluno_id = dados.get("fk_aluno_id")
    livro_id = dados.get("fk_livro_id")

    if not aluno_existe(aluno_id):
        return response_not_found("aluno não encontrado")

    if not livro_existe(livro_id):
        return response_not_found("livro não encontrado")

    # if not livro_disponivel(livro_id):
    #     return response_conflict("livro ja está emprestado")

    emprestimo = create_emprestimo(aluno_id, livro_id)



    return response_created_emprestimo(emprestimo)

@emprestimos_bp.put("/emprestimos/<int:emprestimo_id>/devolucao")
def put_devolucao(emprestimo_id):
    emprestimo = find_by_id(emprestimo_id)

    if not emprestimo:
        return response_not_found("emprestimo não encontrado")

    if emprestimo["data_devolucao"] is not None:
        return response_conflict("Este emprestimo ja foi devolvido")

    emprestimo = devolver_livro(emprestimo_id)


    return response_devolucao(emprestimo)

@emprestimos_bp.delete("/emprestimos/<int:emprestimo_id>")
def delete_emprestimos(emprestimo_id):
    emprestimo = find_by_id(emprestimo_id)

    if not emprestimo:
        return response_not_found("emprestimo não encontrado")

    delete_emprestimo(emprestimo_id)

    return response_deleted()
