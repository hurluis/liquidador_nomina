

from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

blueprint = Blueprint( "vista_usuarios", __name__, "templates" )


import sys
sys.path.append("src")
from Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from Model.MonthlyPaymentLogic import SettlementParameters, calculate_settlement

app = Flask(__name__)
app.secret_key = "supersecretkey"

@blueprint.route("/")
def home():
    return render_template('inicio.html')

@blueprint.route('/crear-usuario')
def index():
    return render_template('crear-usuario.html')

@blueprint.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = {
            'basic_salary': float(request.form['basic_salary']),
            'workdays': int(request.form['workdays']),
            'sick_leave': int(request.form['sick_leave']),
            'transportation_aid': float(request.form['transportation_aid']),
            'dayshift_extra_hours': int(request.form['dayshift_extra_hours']),
            'nightshift_extra_hours': int(request.form['nightshift_extra_hours']),
            'dayshift_extra_hours_holidays': int(request.form['dayshift_extra_hours_holidays']),
            'nightshift_extra_hours_holidays': int(request.form['nightshift_extra_hours_holidays']),
            'leave_days': int(request.form['leave_days']),
            'percentage_health_insurance': float(request.form['percentage_health_insurance']) / 100,
            'percentage_retirement_insurance': float(request.form['percentage_retirement_insurance']) / 100,
            'percentage_retirement_fund': float(request.form['percentage_retirement_fund']) / 100
        }

        settlement_params = SettlementParameters(**data)
        amount_to_pay = calculate_settlement(settlement_params)

        return render_template('result.html', amount_to_pay=amount_to_pay)
    except Exception as e:
        flash(f'Error en el cálculo: {e}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
