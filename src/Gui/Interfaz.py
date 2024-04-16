import sys
sys.path.append("Liquidador_para_nomina/src") 
from MonthlyPayment.MonthlyPaymentLogic import *
import MonthlyPayment.MonthlyPaymentLogic as mp

from kivy.app import App # Es necesario para iniciar y ejecutar una aplicación Kivy.
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
"""
Se utiliza para mostrar texto en la interfaz de usuario de una aplicación Kivy. 
Puedes usarla para mostrar texto estático o dinámico en diferentes partes de tu 
aplicación.
"""
from kivy.uix.button import Button
"""
se utiliza para crear botones en la interfaz de usuario de una aplicación Kivy. 
Los botones pueden ser utilizados para interactuar con la aplicación, 
como hacer clic para realizar una acción específica.
"""

from kivy.uix.boxlayout import BoxLayout
"""
La clase BoxLayout es un diseño que organiza a sus hijos en una sola fila o columna. 
Es útil para organizar widgets (como etiquetas y botones) 
en la interfaz de usuario de una manera ordenada y predecible.
"""
from kivy.uix.screenmanager import ScreenManager, Screen

"""
ScreenManager: Es un widget que administra varias pantallas. Puedes agregar pantallas
a este administrador y cambiar entre ellas según sea necesario.
El ScreenManager maneja la navegación entre pantallas y las animaciones asociadas.

Screen: Representa una pantalla en tu aplicación. 
Puedes personalizar el contenido de cada pantalla con otros widgets de Kivy. 
Las instancias de Screen se agregan al ScreenManager para crear la estructura de la aplicación 
con múltiples pantallas.
"""

class Mein_menu(Screen):
    def __init__(self, **kwargs):
        super(Mein_menu, self).__init__(**kwargs)
        
        
        main_layout = BoxLayout(orientation='vertical')
        
        header=BoxLayout(orientation='horizontal')
        text_header=Label(text="Bienvenido a la aplicacion Calculadora de nomina",font_size=27,color=(1, 0, 0, 1),
                          bold=True,italic=True,font_name='Arial')
        header.add_widget(text_header)
        img = Image(source=r'Liquidador_para_nomina\src\Gui\bienvenidos44.png') 
        header.add_widget(img)
        main_layout.add_widget(header)
        
        
        Buttons_=BoxLayout(orientation='vertical')
        Button_one=Button(text="ir a la Descripcion",font_size=25,color=(0, 0, 1, 1),
                          bold=True,italic=True,font_name='Arial', on_press=self.go_to_tutorial)
        
        Button_two=Button(text=("Ir a la aplicacion"),font_size=25,color=(0, 0, 1, 1),
                          bold=True,italic=True,font_name='Arial',on_press=self.go_to_aplicacion)
        Buttons_.add_widget( Button_one)
        Buttons_.add_widget( Button_two)
        main_layout.add_widget(Buttons_)

        self.add_widget(main_layout)
    
    def go_to_tutorial(self, instance):
        self.manager.current = 'Description'
    
    def go_to_aplicacion(self,instance):
        self.manager.current="Aplicacion"

class Description(Screen):
    def __init__(self, **kwargs):
        super(Description, self).__init__(**kwargs)
        
        header_Description = BoxLayout(orientation='vertical')

        scroll_view = ScrollView()

        # Crear un BoxLayout para contener el texto
        text_layout = BoxLayout(orientation='vertical')

        text_description = f"""
El propósito del programa es calcular el salario mensual de un empleado 
considerando diferentes variables como el salario básico, días laborados, 
días de licencia, y días de incapacidad, entre otros.

Para llevar a cabo este cálculo, se utilizan varias constantes:

1) El salario mínimo legal en Colombia es de ${mp.MINIMUM_WAGE}.
2) La Unidad de Valor Tributario (UVT) tiene un valor de ${mp.UVT}.
3) Coeficientes para calcular el pago de horas extras en diferentes situaciones:
    * Horas extras diurnas: {mp.EXTRA_HOUR_DAYSHIFT}
    * Horas extras nocturnas: {mp.EXTRA_HOUR_NIGHTSHIFT}
    * Horas extras diurnas en días festivos: {mp.EXTRA_HOUR_DAYSHIFT_HOLIDAYS}
    * Horas extras nocturnas en días festivos: {mp.EXTRA_HOUR_NIGHTSHIFT_HOLIDAYS}
4) El número de días y horas en un mes se establece en {mp.MONTH_DAYS} días y {mp.MONTH_HOURS} horas.
5) Porcentajes utilizados para calcular contribuciones de seguro de salud, aportes a pensiones, fondos de retiro y licencias por enfermedad:
    * Porcentaje de seguro de salud y aportes a pensiones: {mp.PERCENTAGE_HEALTH_INSURANCE * 100}%
    * Porcentaje de fondo de retiro: {mp.PERCENTAGE_RETIREMENT_FUND * 100}%
6) Una lista que define los porcentajes de retención salarial en función del salario en UVT.
7) Los porcentajes deben ser ingresados de forma decimal

"""
        description_label =Label(text=text_description,font_size=20 ,size_hint_y=None,halign="justify", valign="top", font_name='Arial')
        Text_proposito=Label(text="Proposito",font_size=30,bold=True, italic=True, font_name='Arial')
        description_label.bind(texture_size=description_label.setter('size'))
        text_layout.add_widget(Text_proposito)
        text_layout.add_widget(description_label)
        scroll_view.add_widget(text_layout)
        header_Description.add_widget(scroll_view)
        
        Contenedor_botones=BoxLayout(orientation="vertical", size_hint=(0.5, 0.8))
        Contenedor_botones.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        button_next = Button(text="ir a la aplicacion",on_press=self.go_to_aplicacion)
        button_back= Button(text="Regresar al texto principal",on_press=self.go_to_Mein_menu)
        Contenedor_botones.add_widget(button_next)
        Contenedor_botones.add_widget(button_back)
        header_Description.add_widget(Contenedor_botones)
        self.add_widget(header_Description)
    
    def go_to_Mein_menu(self, instance):
        self.manager.current = 'Menu Principal'
    
    def go_to_aplicacion(self,instance):
        self.manager.current="Aplicacion"


class aplicacion(Screen):
    def __init__(self, **kwargs):
        super(aplicacion, self).__init__(**kwargs)
        contenedor = GridLayout(cols=4,padding=20,spacing=20)
        lista_contenedor= ["salario basico",
                            "dias laborados",
                            "dias licencia",
                            "ayuda transporte",
                            "horas extra diurnas",
                            "horas extra nocturnas",
                            "horas extra diurnas festivos",
                            "horas extra nocturnas festivos",
                            "dias licencia enfermedad",
                            "porcentaje seguro salud",
                            "porcentaje seguro retiro",
                            "porcentaje fondo retiro"]
        self.text_inputs={}
        for index in lista_contenedor:
            contenedor.add_widget(Label(text=index))
            self.text_inputs[index] = TextInput(font_size=30)
            contenedor.add_widget(self.text_inputs[index])

        self.button_menu=Button(text="Menu principal",on_press=self.go_to_Mein_menu)
        contenedor.add_widget(self.button_menu)
        
        self.button_calculator=Button(text="Calcular")
        contenedor.add_widget(self.button_calculator)

        self.button_calculator.bind(on_press=self.Result_payment)

        self.resultado=Label(text=".................")
        contenedor.add_widget(self.resultado)

        self.button_description=Button(text="Ventana descripcion",on_press=self.go_to_description)
        contenedor.add_widget(self.button_description)
        self.add_widget(contenedor)
    
    def Result_payment(self,sender):
        try:
            self.validar()
            basic_salary= float(self.text_inputs["salario basico"].text)
            workdays= int(self.text_inputs["dias laborados"].text)
            sick_leave= int(self.text_inputs["dias licencia"].text)
            transportation_aid=float(self.text_inputs["ayuda transporte"].text)
            dayshift_extra_hours=float(self.text_inputs["horas extra diurnas"].text)
            nightshift_extra_hours=float(self.text_inputs["horas extra nocturnas"].text)
            dayshift_extra_hours_holidays=float(self.text_inputs["horas extra diurnas festivos"].text)
            nightshift_extra_hours_holidays=float(self.text_inputs["horas extra nocturnas festivos"].text)
            leave_days=int(self.text_inputs["dias licencia enfermedad"].text)
            percentage_health_insurance=float(self.text_inputs["porcentaje seguro salud"].text)
            
            percentage_retirement_insurance=float(self.text_inputs["porcentaje seguro retiro"].text)
            
            percentage_retirement_fund=float(self.text_inputs["porcentaje fondo retiro"].text)
            
            verificar_result_total = mp.SettlementParameters(basic_salary, workdays, sick_leave, transportation_aid,
                                        dayshift_extra_hours, nightshift_extra_hours,
                                        dayshift_extra_hours_holidays, nightshift_extra_hours_holidays,
                                        leave_days, percentage_health_insurance,
                                        percentage_retirement_insurance, percentage_retirement_fund)
            result_total=mp.calculate_settlement(verificar_result_total)
            self.resultado.text= str(result_total)
        
        except ValueError as err:
            self.resultado.text= "Los valores ingresado no son válidos"
        
        except Exception as err:
            self.mostrar_error( err )
    
    def mostrar_error( self, err ):
        contenido = GridLayout(cols=1)
        contenido.add_widget( Label(text= str(err) ) )
        cerrar = Button(text="Cerrar" )
        contenido.add_widget( cerrar )
        popup = Popup(title="Error",content=contenido)
        cerrar.bind( on_press=popup.dismiss)
        popup.open()

    def validar(self):
        for key, value in self.text_inputs.items():
            if not value.text:
                raise Exception(f"El Valor de {key} no puede estar vacío")
            try:
                float_value = float(value.text)
            except ValueError:
                raise Exception(f"El Valor de {key} debe ser un número válido")
       
    def go_to_Mein_menu(self, instance):
        self.manager.current = 'Menu Principal'
    
    def go_to_description(self,instance):
        self.manager.current="Description"


class nomina_calculator(App):
    def build(self):
        boss_screen= ScreenManager()
        boss_screen.add_widget(Mein_menu(name="Menu Principal"))
        boss_screen.add_widget(Description(name="Description"))
        boss_screen.add_widget(aplicacion(name="Aplicacion"))
        return boss_screen    
if __name__ == "__main__":
    nomina_calculator().run()