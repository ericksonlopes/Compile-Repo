from flask import Flask, jsonify, request, Response
from compile_repo import CompileRepo
import json

app = Flask('__name__')


@app.route('/', methods=['GET'])
def route_test() -> jsonify:
    try:
        # armazena a data no json
        json_data = json.loads(request.data)

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        cr = CompileRepo(json_data['repository'])
        # Executa o código de busca
        cr.get_infos()
        # armazena os arquivos
        list_files = cr.files_list
        # armazena os diretórios
        list_directories = cr.directory_list

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400

    else:
        return jsonify({"files": list_files, "directories": list_directories}), 200


if __name__ == '__main__':
    app.run()
