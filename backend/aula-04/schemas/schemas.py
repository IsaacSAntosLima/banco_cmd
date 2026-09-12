from flask import jsonify

def response_success(entity_data):
    return jsonify("consulta realizada com sucesso", entity_data), 200

def response_created():
    return jsonify({"Mensagem: ":"Livro adicionado com sucesso"}), 201

def response_updated():
    return jsonify({"Mensagem: ":"Livro atualizado com sucesso"}),200

def response_deleted():
    return jsonify({"Mensagem: ":"Livro excluido com sucesso"}),200