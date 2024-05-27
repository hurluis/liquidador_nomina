from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

blueprint = Blueprint("vista_usuarios", __name__, "templates")

import sys
sys.path.append("src")
from Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from Model.TablesEmployer import Employerinput
import Model.TablesEmployer as Temployer
WorkersIncomeData.Droptable()
WorkersIncomeData.CreateTable()
WorkersoutputsData.Droptable()
WorkersoutputsData.CreateTable()

# Definir la clase NuevoEmpleado


# Definir las rutas y las funciones asociadas
@blueprint.route("/")
def home():
    return render_template("inicio.html")

@blueprint.route("/new-user")
def nuevo():
    return render_template("crear_usuario.html")

@blueprint.route("/crear_usuario")
def crear_usuario():

    # Crear una instancia de NuevoEmpleado con los datos del formulario
    nuevo_empleado = Employerinput(name=request.args["nombre"], id=request.args["cedula"], basic_salary=request.args["salario"], monthly_worked_days=request.args["Días_Trabajados"], days_leave=request.args["Días_Libres"], transportation_allowance=request.args["Auxilio_Trasporte"],
                daytime_overtime_hours=request.args["Horas_diurnas_extra"], nighttime_overtime_hours=request.args["Horas_nocturnas_extra"], daytime_holiday_overtime_hours=request.args["Horas_diurnas_extra_festivo"],
                nighttime_holiday_overtime_hours=request.args["Horas_nocturnas_extra_festivo"], sick_leave_days=request.args["Días_enfermedad"], health_contribution_percentage=request.args["Porcentaje_seguro_salud"],
                pension_contribution_percentage=request.args["Porcentaje_retiro"], solidarity_pension_fund_contribution_percentage=request.args["percentage_retirement_fund"])

    # Insertar el nuevo empleado en la base de datos
    WorkersIncomeData.Insert(nuevo_empleado)

        # Redirigir al usuario a la página de resultado después de insertar los datos
    return render_template("resultado.html", user=nuevo_empleado, mensaje= "Usuario insertado exitosamente!")



@blueprint.route("/buscar_usuario")
def buscar_usuario():
    # Aquí podrías manejar la lógica para buscar un usuario
    return render_template("buscar_usuario.html")

@blueprint.route("/actualizar_usuario")
def modificar_usuario():
    # Aquí podrías manejar la lógica para modificar un usuario
    return render_template("actualizar_usuario.html")

@blueprint.route("/eliminar_usuario")
def eliminar_usuario():
    # Aquí podrías manejar la lógica para eliminar un usuario
    return render_template("eliminar_usuario.html")

