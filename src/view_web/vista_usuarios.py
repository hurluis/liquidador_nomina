from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import sys
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from src.Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from src.Model.TablesEmployer import Employerinput, Employeroutput as Temployer,Employeroutput
import src.Model.TablesEmployer as Temployer
import src.Model.MonthlyPaymentLogic as mp
from src.Model.MonthlyPaymentLogic import calculate_settlement, InvalidRetirementFundPercentageError
import pandas as pd

app = Flask(__name__)
blueprint = Blueprint("vista_usuarios", __name__, template_folder="templates")

WorkersIncomeData.Droptable()
WorkersIncomeData.CreateTable()
WorkersoutputsData.Droptable()
WorkersoutputsData.CreateTable()

@blueprint.route("/")
def home():
    return render_template("inicio.html")

@blueprint.route("/new-user")
def nuevo():
    return render_template("crear_usuario.html")

@blueprint.route("/crear_usuario")
def crear_usuario():
    nuevo_empleado = Employerinput(
        name=request.args["nombre"], 
        id=request.args["cedula"], 
        basic_salary=float(request.args["salario"]), 
        monthly_worked_days=int(request.args["Días_Trabajados"]), 
        days_leave=int(request.args["Días_Libres"]), 
        transportation_allowance=float(request.args["Auxilio_Trasporte"]),
        daytime_overtime_hours=float(request.args["Horas_diurnas_extra"]), 
        nighttime_overtime_hours=float(request.args["Horas_nocturnas_extra"]), 
        daytime_holiday_overtime_hours=float(request.args["Horas_diurnas_extra_festivo"]),
        nighttime_holiday_overtime_hours=float(request.args["Horas_nocturnas_extra_festivo"]), 
        sick_leave_days=int(request.args["Días_enfermedad"]), 
        health_contribution_percentage=float(request.args["Porcentaje_seguro_salud"]),
        pension_contribution_percentage=float(request.args["Porcentaje_retiro"]), 
        solidarity_pension_fund_contribution_percentage=float(request.args["percentage_retirement_fund"])
    )

    WorkersIncomeData.Insert(nuevo_empleado)
    return render_template("resultado.html", user=nuevo_empleado, mensaje="Usuario insertado exitosamente!")

@blueprint.route("/buscar-usuario")
def buscar_usuario():
    return render_template("buscar_usuario.html")

@blueprint.route("/buscar_usuario_result", methods=["GET"])
def buscar_usuario_result():
    nombre = request.args["nombre"]
    cedula = request.args["cedula"]
    trabajador = WorkersIncomeData.QueryWorker(nombre, cedula)
    if trabajador:
        return render_template("resultado.html", user=trabajador, mensaje="Trabajador encontrado:")
    else:
        return render_template("resultado.html", mensaje="No se encontró ningún trabajador con el nombre y la cédula proporcionados.")

@blueprint.route("/actualizar-usuario")
def modificar_usuario():
    return render_template("actualizar_usuario.html")

@blueprint.route("/actualizar_usuario_result", methods=["POST"])
def actualizar_usuario_result():
    nombre = request.form["nombre"]
    cedula = request.form["cedula"]
    columna = request.form["columna"]
    valor = request.form["valor"]

    try:
        if columna in ["basic_salary", "transportation_allowance", "daytime_overtime_hours", "nighttime_overtime_hours",
                       "daytime_holiday_overtime_hours", "nighttime_holiday_overtime_hours", "health_contribution_percentage",
                       "pension_contribution_percentage", "solidarity_pension_fund_contribution_percentage"]:
            valor = float(valor)
        else:
            valor = int(valor)
        
        WorkersIncomeData.Update(nombre, cedula, KEYUPDATE=columna, VALUEUPDATE=valor)
        mensaje = "Información del trabajador actualizada exitosamente!"
        return render_template("resultado.html", mensaje=mensaje)
    except Temployer.not_exist as e:
        mensaje = f"Error al actualizar: {str(e)}"
        return render_template("resultado.html", mensaje=mensaje)
    except Exception as e:
        mensaje = f"Error inesperado: {str(e)}"
        return render_template("resultado.html", mensaje=mensaje)

@blueprint.route("/eliminar-usuario")
def eliminar_usuario():
    return render_template("eliminar_usuario.html")

@blueprint.route("/eliminar_usuario_result", methods=["POST"])
def eliminar_usuario_result():
    nombre = request.form["nombre"]
    cedula = request.form["cedula"]

    trabajador = WorkersIncomeData.QueryWorker(nombre, cedula)
    if trabajador:
        WorkersIncomeData.DeleteWorker(nombre, cedula)
        return render_template("resultado.html", mensaje="Trabajador eliminado exitosamente!")
    else:
        return render_template("resultado.html", mensaje="No se encontró ningún trabajador con el nombre y la cédula proporcionados.")
    
@blueprint.route("/calcular-liquidacion", methods=["GET"])
def calcular_liquidacion():
    return render_template("calcular_liquidacion.html")

@blueprint.route("/mostrar_resultado_liquidacion", methods=["POST"])
def mostrar_resultado_liquidacion():
    nombre = request.form["nombre"]
    cedula = request.form["cedula"]
    
    try:
        findemployer = WorkersoutputsData.QueryWorker(nombre, cedula)
        if findemployer:
            return render_template("resultado_liquidacion.html",
                                  nombre=findemployer.name,
                                  cedula=findemployer.id,
                                  salario_basico=findemployer.basic_salary,
                                  dias_trabajados=findemployer.workdays,
                                  dias_licencia_enfermedad=findemployer.sick_leave,
                                  subsidio_transporte=findemployer.transportation_aid,
                                  horas_extra_diurnas=findemployer.dayshift_extra_hours,
                                  horas_extra_nocturnas=findemployer.nightshift_extra_hours,
                                  horas_extra_diurnas_festivos=findemployer.dayshift_extra_hours_holidays,
                                  horas_extra_nocturnas_festivos=findemployer.nightshift_extra_hours_holidays,
                                  dias_licencia=findemployer.leave_days,
                                  porcentaje_seguro_salud=findemployer.percentage_health_insurance,
                                  porcentaje_aporte_pensiones=findemployer.percentage_retirement_insurance,
                                  porcentaje_aporte_fondo_retiro=findemployer.percentage_retirement_fund,
                                  total_a_pagar=findemployer.amounttopay)
        else:
            return render_template("resultado.html", mensaje="No se encontró ningún trabajador con el nombre y la cédula proporcionados.")
    except Temployer.not_found as e:
        return render_template("resultado.html", mensaje=str(e))
    except Exception as e:
        return render_template("resultado.html", mensaje=str(e))





app.register_blueprint(blueprint, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
