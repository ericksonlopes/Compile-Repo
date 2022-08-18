from typing import List

from flask import jsonify, request, redirect, Blueprint

from src.compile_repo import CompileRepo, BranchsRepo, ReleasesRepo
from src.models import *

api = Blueprint('/', __name__)


@api.route('/', methods=['GET'])
def redireciona() -> jsonify:
    return redirect('https://github.com/Erickson-lopes-dev/Compile-Repo', code=302)


@api.route('/repofd', methods=['POST'])
def get_files_diretories() -> jsonify:
    try:
        # Armazena a data no json
        json_data = request.get_json()

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        # Instância da classe
        gdf = CompileRepo(repository=json_data['repository']).get_diretories_and_files()

        if 'branch' in json_data.keys():
            gdf.branch = json_data['branch']

        # recebe o objeto com todos os dados
        data_full: FullDataModel = gdf

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400

    else:
        return jsonify(data_full), 200


@api.route('/branchs', methods=['POST'])
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


@api.route('/releases', methods=['POST'])
def get_releases() -> jsonify:
    try:
        # Armazena a data no json
        json_data = request.get_json()

        # Verifica se o field existe no json
        if 'repository' not in json_data.keys():
            return jsonify({'erro': f"Field 'repository' not found"}), 400

        releases: List[ReleaseModel] = ReleasesRepo(json_data['repository']).get_releases()

    except Exception as error:
        return jsonify({'erro': f"{str(error)} {str(type(error))}"}), 400
    else:
        return jsonify(releases), 200


@api.route('/tags', methods=['POST'])
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
