import json

from flask import Flask, jsonify, request

from compile_repo import CompileRepo
from utils import ReturnModel

app = Flask('__name__')


@app.route('/', methods=['GET'])
def route_test() -> jsonify:
    try:
        # Armazena a data no json
        json_data = json.loads(request.data)

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        # Instância da classe
        cr = CompileRepo(json_data['repository'])

        # Executa o código de busca
        cr.get_diretories_and_files()

        # Armazena o link do repositório
        repository = cr.repository
        # Armazena os arquivos
        list_files = cr.files_list
        # Armazena os diretórios
        list_directories = cr.directory_list

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400

    else:
        return jsonify(ReturnModel(repository=repository, files=list_files, directories=list_directories)), 200


if __name__ == '__main__':
    app.run()
