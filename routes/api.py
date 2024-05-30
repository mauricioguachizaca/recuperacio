from flask import Blueprint, jsonify, make_response, request
from controls.expresionDaoControl import ExpresionDaoControl
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

@api.route('/')
def home():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )

# LISTA EXPRESIONES GET
@api.route('/api/expresiones')
def lista_expresiones():
    ed = ExpresionDaoControl()
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": ed._lista}),
        200
    )

# GUARDAR EXPRESION POST
@api.route('/api/expresiones/guardar', methods=['POST'])
def guardar_expresion():
    ed = ExpresionDaoControl()
    data = request.json
    if "expresion" not in data:
        return make_response(
            jsonify({"msg": "Falta expresion", "code": 400, "data": []}),
            400
        )
    # Assuming the expression is sent as 'expresion' in the JSON data
    ed._expresion._expresion = data['expresion']
    result = ed.transform()
    return make_response(
        jsonify({"msg": "OK, la expresion se ha guardado correctamente", "code": 200, "data": result}),
        200
    )
