import sys
sys.path.append("Liquidador_para_nomina/src")
sys.path.append("./src")
from MonthlyPayment.MonthlyPaymentLogic import *
import MonthlyPayment.MonthlyPaymentLogic as mp
#from Controller.Controladortablas import WorkersIncomeData

class faileprimarykey(Exception):
    pass

class not_exist(Exception):
    pass

class not_found(Exception):
    pass

class updatenotfount(Exception):
    pass

class Employerinput:
    def __init__(self,name, id, basic_salary, monthly_worked_days, days_leave, transportation_allowance,
                 daytime_overtime_hours, nighttime_overtime_hours, daytime_holiday_overtime_hours,
                 nighttime_holiday_overtime_hours, sick_leave_days, health_contribution_percentage,
                 pension_contribution_percentage, solidarity_pension_fund_contribution_percentage):
        
        self.name = name
        self.id = id
        self.basic_salary = basic_salary
        self.monthly_worked_days = monthly_worked_days
        self.days_leave = days_leave
        self.transportation_allowance = transportation_allowance
        self.daytime_overtime_hours = daytime_overtime_hours
        self.nighttime_overtime_hours = nighttime_overtime_hours
        self.daytime_holiday_overtime_hours = daytime_holiday_overtime_hours
        self.nighttime_holiday_overtime_hours = nighttime_holiday_overtime_hours
        self.sick_leave_days = sick_leave_days
        self.health_contribution_percentage = health_contribution_percentage
        self.pension_contribution_percentage = pension_contribution_percentage
        self.solidarity_pension_fund_contribution_percentage = solidarity_pension_fund_contribution_percentage
    
    def Isequal(self, dbneon):
        assert (self.name == dbneon.name)
        assert (self.id == dbneon.id)
        assert (self.basic_salary == dbneon.basic_salary)
        assert (self.monthly_worked_days == dbneon.monthly_worked_days)
        assert (self.days_leave == dbneon.days_leave)
        assert (self.transportation_allowance == dbneon.transportation_allowance)
        assert (self.daytime_overtime_hours == dbneon.daytime_overtime_hours)
        assert (self.nighttime_overtime_hours == dbneon.nighttime_overtime_hours)
        assert (self.daytime_holiday_overtime_hours == dbneon.daytime_holiday_overtime_hours)
        assert (self.nighttime_holiday_overtime_hours == dbneon.nighttime_holiday_overtime_hours)
        assert (self.sick_leave_days == dbneon.sick_leave_days)
        assert (self.health_contribution_percentage == dbneon.health_contribution_percentage)
        assert (self.pension_contribution_percentage == dbneon.pension_contribution_percentage)
        assert (self.solidarity_pension_fund_contribution_percentage == dbneon.solidarity_pension_fund_contribution_percentage)
    
    def primary_key(name, id, module):
        value = module.QueryWorker(name, id)
        if value is not None:
            raise faileprimarykey("Ya ingresaste este usuario: {} - {}".format(name, id))
        
    @staticmethod
    def notexist(employer):
        # Verificar si algún atributo es None
        if any(value is None for value in employer.__dict__.values()):
            raise not_exist("Falta un valor al crear la clase Employerinput")
    
    def valor_presente(atributo):
        lista_atributos=parametros_constructor = [
                                            "name", "id", "basic_salary", "monthly_worked_days", "days_leave", "transportation_allowance",
                                            "daytime_overtime_hours", "nighttime_overtime_hours", "daytime_holiday_overtime_hours",
                                            "nighttime_holiday_overtime_hours", "sick_leave_days", "health_contribution_percentage",
                                            "pension_contribution_percentage", "solidarity_pension_fund_contribution_percentage"]
        if atributo  not in lista_atributos:
            raise updatenotfount("no se encuentra el valor para realizar el update")
    




class Employeroutput():
    def __init__(self, name,id,basic_salary, workdays, sick_leave, transportation_aid, dayshift_extra_hours, nightshift_extra_hours,
                 dayshift_extra_hours_holidays, nightshift_extra_hours_holidays, leave_days, percentage_health_insurance,
                 percentage_retirement_insurance, percentage_retirement_fund,devengado,deducido,amounttopay):
        self.name = name
        self.id = id
        self.basic_salary = basic_salary
        self.workdays = workdays
        self.sick_leave = sick_leave
        self.transportation_aid = transportation_aid
        self.dayshift_extra_hours = dayshift_extra_hours
        self.nightshift_extra_hours = nightshift_extra_hours
        self.dayshift_extra_hours_holidays = dayshift_extra_hours_holidays
        self.nightshift_extra_hours_holidays = nightshift_extra_hours_holidays
        self.leave_days = leave_days
        self.percentage_health_insurance = percentage_health_insurance
        self.percentage_retirement_insurance = percentage_retirement_insurance
        self.percentage_retirement_fund = percentage_retirement_fund
        self.devengado=devengado
        self.deducido=deducido
        self.amounttopay=amounttopay
    
    def Isequivalent(self, dbneon):
        assert (self.name == dbneon.name)
        assert (self.id == dbneon.id)
        assert (self.basic_salary == dbneon.basic_salary)
        assert (self.workdays == dbneon.workdays)
        assert (self.sick_leave == dbneon.sick_leave)
        assert (self.transportation_aid == dbneon.transportation_aid)
        assert (self.dayshift_extra_hours == dbneon.dayshift_extra_hours) 
        assert (self.nightshift_extra_hours == dbneon.nightshift_extra_hours) 
        assert (self.dayshift_extra_hours_holidays == dbneon.dayshift_extra_hours_holidays)
        assert (self.nightshift_extra_hours_holidays == dbneon.nightshift_extra_hours_holidays)
        assert (self.leave_days == dbneon.leave_days) 
        assert (self.percentage_health_insurance == dbneon.percentage_health_insurance)
        assert (self.percentage_retirement_insurance == dbneon.percentage_retirement_insurance) 
        assert (self.percentage_retirement_fund == dbneon.percentage_retirement_fund) 
        assert (self.devengado == dbneon.devengado) 
        assert (self.deducido == dbneon.deducido)
        assert (self.amounttopay == dbneon.amounttopay)
        return True
    
    def employernotfound(query):
        if query is None:
            raise not_found("no se ha encontrado su busqueda")   
            