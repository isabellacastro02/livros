from models.livros_models import Livros
from db import db
import json
from flask import make_response, request

def update_livro(livro_id):
    livro = Livro.query.get(livro_id)  # Busca o livro pelo ID
    if not livro:  # Caso o livro não seja encontrado
        response = make_response(
            json.dumps({'mensagem': 'Livro não encontrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    dados = request.json  # Pega os dados enviados pelo corpo da requisição

    # Atualiza apenas os campos enviados
    livro.titulo = dados.get('titulo', livro.titulo)
    livro.autor = dados.get('autor', livro.autor)
    livro.ano = dados.get('ano', livro.ano)

    db.session.commit()  # Confirma a atualização no banco de dados

    # Retorna resposta com os dados do livro atualizado
    response = make_response(
        json.dumps({
            'mensagem': 'Livro atualizado com sucesso.',
            'livro': livro.json()  # supondo que seu model Livro tenha um método .json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


# Função para excluir um livro por ID com confirmação via parâmetro
def delete_livro(livro_id):
    confirmacao = request.args.get('confirmacao')  # Obtém o parâmetro da URL

    if confirmacao != 'true':  # Se não houver confirmação, impede a exclusão
        response = make_response(
            json.dumps({'mensagem': 'Confirmação necessária para excluir o livro.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    livro = Livro.query.get(livro_id)  # Busca o livro pelo ID
    if not livro:  # Se o livro não for encontrado
        response = make_response(
            json.dumps({'mensagem': 'Livro não encontrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(livro)  # Remove o livro do banco
    db.session.commit()  # Confirma a exclusão

    # Retorna resposta com mensagem de sucesso
    response = make_response(
        json.dumps({'mensagem': 'Livro excluído com sucesso.'}, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response