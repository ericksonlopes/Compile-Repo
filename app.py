from flask import Flask, jsonify, request, Response
from compile_repo import CompileRepo
import json

app = Flask('__name__')


@app.route('/', methods=['GET'])
def route_test():
    try:
        json_data = json.loads(request.data)

        cr = CompileRepo(json_data['repository'])

        # Executa o código de busca
        cr.get_infos()

        list_files = cr.files_list
        list_directories = cr.directory_list
    except Exception as error:
        return Response({'erro': f"{str(error)} {str(type(error))}"}, status=400)

    else:
        return jsonify({"files": list_files, "directories": list_directories}, 200)


if __name__ == '__main__':
    app.run()
