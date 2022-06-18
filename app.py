from flask import Flask, jsonify, request, redirect

from compile_repo import CompileRepo, BranchsRepo
from utils import *

app = Flask('__name__')


@app.route('/', methods=['GET'])
def redireciona() -> jsonify:
    return redirect('https://github.com/Erickson-lopes-dev/Compile-Repo', code=302)


@app.route('/repo', methods=['POST'])
def get_files_diretories() -> jsonify:
    try:
        # Armazena a data no json
        json_data = request.get_json()

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        # Instância da classe
        cr = CompileRepo(json_data['repository'])

        if 'branch' in json_data.keys():
            cr.branch = json_data['branch']

        cr.get_diretories_and_files()

        # recebe o objeto com todos os dados
        data_full: FullDataModel = cr.return_full_data_repo()

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400

    else:
        return jsonify(data_full), 200


@app.route('/get-branches', methods=['POST'])
def get_branchs() -> jsonify:
    try:
        # Armazena a data no json
        json_data = request.get_json()

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        branchs: List[BranchModel] = BranchsRepo(json_data['repository']).get_all_branchs()

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400
    else:
        return jsonify(branchs), 200


@app.route('/releases')
def get_releases() -> jsonify:
    try:
        # Armazena a data no json
        json_data = request.get_json()

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        releases = []

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400
    else:
        return jsonify({}), 200


@app.route('/tags')
def get_tags() -> jsonify:
    try:
        # Armazena a data no json
        json_data = request.get_json()

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        tags = []

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400
    else:
        return jsonify({}), 200


if __name__ == '__main__':
    app.run()
