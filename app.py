import json

from flask import Flask, jsonify, request

from compile_repo import CompileRepo

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

        # recebe o objeto com todos os dados
        data_full = cr.return_full_data_repo()

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400

    else:
        return jsonify(data_full), 200


if __name__ == '__main__':
    app.run()
