import unittest
import sys
sys.path.append("Liquidador_para_nomina/src")
sys.path.append("./src")
from MonthlyPayment.MonthlyPaymentLogic import *
import MonthlyPayment.MonthlyPaymentLogic as mp
from Controller.Controladortablas import WorkersIncomeData
from Controller.Controladortablas import WorkersoutputsData
import Model.TablesEmployer as Temployer


print(f"""Bienvenido a este calculador de nómina, el cual va a tener la posibilidad de conectarse a una base de datos.
           Dentro de las siguientes características que va a tener el programa están las siguientes: primero, puedes construir 
           una tabla inicial en la cual puedes insertar tus trabajadores y asignarles las características de sus sueldos
           correspondientes como "salario básico", "días mensuales laborados", "días de licencia", "ayuda de transporte", "horas extra diurnas",
           "horas extra nocturnas", "horas extra diurnas festivos", "horas extra nocturnas festivos", "días de licencia por enfermedad",
           "porcentaje de aporte a salud", "porcentaje de aporte a pensión", "porcentaje de aporte a fondo de solidaridad pensional".""")

print(f"""Además de esto, a esta tabla podrás actualizar los datos, eliminarlos, insertar y hacer consultas sobre los trabajadores.""")

print()

print(f"""Ahora bien, también puedes acceder a la segunda tabla, la cual va a contener información de los pagos a los trabajadores. 
            A esta tabla podrás hacer consultas y ver todo lo referente a los trabajadores.""")

print("""Que vas a hacer 
          insertar_insertar_trabajador
          buscar_usuario
          eliminar_trabajador
          llenar_tabla_de_pagos
          hacer_busquedas_en_tabla_de_pagos
          """)

Valor=input("selecciona una de las anteriores")


