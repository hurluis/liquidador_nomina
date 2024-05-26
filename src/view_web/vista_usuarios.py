from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

blueprint = Blueprint("vista_usuarios", __name__, "templates")

import sys
sys.path.append("src")
from Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from Model.MonthlyPaymentLogic import SettlementParameters, calculate_settlement

app = Flask(__name__)
app.secret_key = "supersecretkey"

@blueprint.route("/")
def home():
    return render_template('inicio.html')

@blueprint.route("/crear-usuario")
def crear_usuario():
    # Aquí podrías manejar la lógica para crear un usuario
    return render_template('crear_usuario.html')

@blueprint.route("/buscar-usuario")
def buscar_usuario():
    # Aquí podrías manejar la lógica para buscar un usuario
    return render_template('buscar_usuario.html')

@blueprint.route("/modificar-usuario")
def modificar_usuario():
    # Aquí podrías manejar la lógica para modificar un usuario
    return render_template('modificar_usuario.html')

@blueprint.route("/eliminar-usuario")
def eliminar_usuario():
    # Aquí podrías manejar la lógica para eliminar un usuario
    return render_template('eliminar_usuario.html')

if __name__ == "__main__":
    app.register_blueprint(blueprint)
    app.run(debug=True)