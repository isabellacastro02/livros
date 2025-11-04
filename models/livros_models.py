from flask import make_response, request
import json

# Importa o objeto `db` que representa a conexão com o banco de dados
from db import db

# Define a classe Livro como um modelo de dados do SQLAlchemy
class Livro(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'livros'

    # Estrutura da tabela com suas colunas
    id = db.Column(db.Integer, primary_key=True)  # Coluna ID, chave primária
    titulo = db.Column(db.String(150), nullable=False)  # Coluna para o título do livro
    autor = db.Column(db.String(100), nullable=False)  # Coluna para o autor do livro
    ano = db.Column(db.Integer, nullable=False)  # Coluna para o ano de publicação

    # Método para converter o objeto em formato JSON
    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano
        }


# Função para atualizar um livro
def update_livro(livro_id):
    livro = Livro.query.get(livro_id)  # Busca o livro pelo ID
    if not livro:  # Se o livro não for encontrado, retorna erro
        response = make_response(
            json.dumps({'mensagem': 'Livro não encontrado.'}, ensure_ascii=False),
            404  # Código HTTP 404 = "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    livro_data = request.json  # Dados enviados na requisição

    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in livro_data for key in ['titulo', 'autor', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Título, autor e ano são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 = "Requisição inválida"
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Atualiza os dados do livro
    livro.titulo = livro_data['titulo']
    livro.autor = livro_data['autor']
    livro.ano = livro_data['ano']

    db.session.commit()  # Confirma a atualização no banco

    # Retorna resposta com o livro atualizado
    response = make_response(
        json.dumps({
            'mensagem': 'Livro atualizado com sucesso.',
            'livro': livro.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response