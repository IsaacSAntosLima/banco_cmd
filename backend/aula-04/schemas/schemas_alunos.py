from flask import jsonify

def response_success_a(entity_data):
    return jsonify("consulta realizada com sucesso", entity_data), 200

def response_created_a():
    return jsonify({"Mensagem: ":"Aluno adicionado com sucesso"}), 201

def response_updated_a():
    return jsonify({"Mensagem: ":"Aluno atualizado com sucesso"}),200

def response_deleted_a():
    return jsonify({"Mensagem: ":"Aluno excluido com sucesso"}),200