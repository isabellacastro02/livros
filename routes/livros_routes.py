from flask import Blueprint, request
from controllers.livro_controllers import (
    get_livros,
    get_livro_by_id,
    get_livro_by_titulo,
    create_livro,
    update_livro,
    delete_livro
)

# Define um Blueprint para as rotas de "Livro"
livro_routes = Blueprint('livro_routes', __name__)

# Rota para listar todos os livros (GET)
@livro_routes.route('/livros', methods=['GET'])
def livros_get():
    return get_livros()

# Rota para buscar um livro pelo ID (GET)
@livro_routes.route('/livros/<int:livro_id>', methods=['GET'])
def livro_get_by_id(livro_id):
    return get_livro_by_id(livro_id)

# Rota para buscar um livro pelo título (GET)
@livro_routes.route('/livros/titulo/<string:livro_titulo>', methods=['GET'])
def livro_get_by_titulo(livro_titulo):
    return get_livro_by_titulo(livro_titulo)

# Rota para criar um novo livro (POST)
@livro_routes.route('/livros', methods=['POST'])
def livros_post():
    return create_livro(request.json)

# Rota para atualizar um livro pelo ID (PUT)
@livro_routes.route('/livros/<int:livro_id>', methods=['PUT'])
def livros_put(livro_id):
    return update_livro(livro_id, request.json)

# Rota para excluir um livro pelo ID (DELETE)
@livro_routes.route('/livros/<int:livro_id>', methods=['DELETE'])
def livro_delete(livro_id):
    return delete_livro(livro_id)
