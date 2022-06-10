import json

from flask import Flask, jsonify, request, redirect

from compile_repo import CompileRepo

app = Flask('__name__')


@app.route('/', methods=['GET'])
def redireciona() -> jsonify:
    return redirect('https://github.com/Erickson-lopes-dev/Compile-Repo', code=302)


@app.route('/repo', methods=['GET'])
def repo() -> jsonify:
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
