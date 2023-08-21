from flask_restful import Resource
import json
from flask import request

habilidades = ['Python', 'Java', 'Flask', 'PHP']


# lista todas as habilidade e permite registrar uma nova habilidade
class ListaHabilidades(Resource):
    def get(self):
        return habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(habilidades)
        dados['id'] = posicao
        habilidades.append(dados)
        return habilidades[posicao]


# devolve umq habilidade pelo ID, tambem altera e deleta uma habilidade
class Habilidades(Resource):
    def get(self, id):
        try:
            response = habilidades[id]
        except IndexError:
            mensagem = f'Habilidade de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        habilidades[id] = dados
        return dados

    def delete(self, id):
        habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro Excluido'}
