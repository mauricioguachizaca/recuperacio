from flask import Blueprint, render_template, request, redirect, abort
from controls.expresionDaoControl import ExpresionDaoControl

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('template.html')

# RENDERS A LOS TEMPLATES
@router.route('/expresiones')
def ver_expresiones():
    ed = ExpresionDaoControl()
    lista = list(ed._lista)  # Convertir Linked_List a una lista
    return render_template('expresiones/lista.html', lista=lista)


@router.route('/expresiones/formulario')
def ver_guardar():
    return render_template('expresiones/guardar.html')

@router.route('/expresiones/editar/<pos>')
def ver_editar(pos):
    ed = ExpresionDaoControl()
    try:
        expresion = ed._lista[int(pos)-1]  # Uso de la propiedad _lista
    except IndexError:
        abort(404)
    return render_template('expresiones/editar.html', data=expresion)

# LOGICAS
# GUARDAR EXPRESION POST
@router.route('/expresiones/guardar', methods=['POST'])
def guardar_expresion():
    ed = ExpresionDaoControl()
    data = request.form
    if 'expresion' not in data:
        abort(400)
    ed._expresion._expresion = data['expresion']  # Uso de la propiedad _expresion
    result = ed.transform()
    return redirect('/expresiones', code=302)

@router.route('/expresiones/modificar', methods=['POST'])
def modificar_expresion():
    ed = ExpresionDaoControl()
    data = request.form
    pos = int(data['id']) - 1
    try:
        expresion = ed._lista[pos]  # Uso de la propiedad _lista
    except IndexError:
        abort(404)
    if 'expresion' not in data:
        abort(400)
    expresion._expresion = data['expresion']
    result = ed.transform()
    return redirect('/expresiones', code=302)
