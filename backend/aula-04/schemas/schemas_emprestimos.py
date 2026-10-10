from flask import jsonify

def response_success(entity_data):
    return jsonify("consulta realizada com sucesso", entity_data), 200

def response_not_found(mensagem):
    return jsonify({"erro": mensagem}), 404

def response_deleted():
    return jsonify({"Mensagem: ":"Livro excluido com sucesso"}),200

def response_bad_request(mensagem):
    return jsonify({"erro": mensagem}), 400


def response_conflict(mensagem):
    return jsonify({"erro": mensagem}), 409


def response_internal_error():
    return jsonify({"erro": "Ocorreu um erro interno no servidor"}), 500


def response_created_emprestimo(emprestimo):
    return jsonify({
        "mensagem": "Empréstimo realizado com sucesso",
        "emprestimo": emprestimo
    }), 201


def response_devolucao(emprestimo):
    return jsonify({
        "mensagem": "Livro devolvido com sucesso",
        "emprestimo": emprestimo
    }), 200