from datetime import date, timedelta, datetime
import holidays
import calendar
import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR')
except:
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')


# Table
# DIM_TEMPO
# Id_tempo
# Data
# Dia
# Dia Semana
# FimSemana
# Quinzena
# Mes
# NomeMes
# FimMes
# Trimestre
# NomeTrimestre
# Semestre
# NomeSemestre
# Ano

def get_week_day_name(n):
    if n == 0:
        return 'Segunda-Feira'
    elif n == 1:
        return 'Terça-Feira'
    elif n == 2:
        return 'Quarta-Feira'
    elif n == 3:
        return 'Quinta-Feira'
    elif n == 4:
        return 'Sexta-Feira'
    elif n == 5:
        return 'Sabado'
    elif n == 6:
        return 'Domingo'


isWeekend = lambda n: 'SIM' if n == 5 or n == 6 else 'NÃO'
isEndOfMonth = lambda d, dm: 'SIM' if d == dm else 'NÃO'
get_quinzena = lambda n: 1 if n <= 15 else 2
get_semestre = lambda n: 1 if n <= 6 else 2
get_trimestre_name = lambda n: f'{n}º trimestre'
get_semestre_name = lambda n: f'{n}º semestre'


def get_trimestre(n):
    if n <= 3:
        return 1
    elif 3 < n <= 6:
        return 2
    elif 6 < n <= 9:
        return 3
    elif n > 9:
        return 4


start_date = datetime.strptime(input('Data inicial (dd/mm/year):'), '%d/%m/%Y').date()
end_date = datetime.strptime(input('Data final (dd/mm/year):'), '%d/%m/%Y').date()


# date_final = input('Data final (dd/mm/year)')


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


for single_date in daterange(start_date, end_date):
    day = single_date.strftime("%d")
    month = single_date.strftime("%m")
    year = single_date.strftime("%Y")
    weekDay = calendar.weekday(int(year), int(month), int(day))
    print('Data:', single_date.strftime("%d-%m-%Y"))
    print('Dia:', day)
    print(get_week_day_name(weekDay))
    print('FimdeSemana:', isWeekend(weekDay))
    print('Quinzena:', get_quinzena(int(day)))
    print('Mes:', month)
    print(single_date.strftime("%B").title())
    print('FimdeMes:', isEndOfMonth(day, calendar.monthrange(int(year), int(month))[1]))
    print('Trimestre:', get_trimestre(int(month)))
    print(get_trimestre_name(get_trimestre(int(month))))
    print('Semestre:', get_semestre(int(month)))
    print(get_semestre_name(get_semestre(int(month))))
    print('Ano:', year)
    print('\n')

br_holidays = holidays.Brazil(state='SE')
# date(year, mm, dd) in custom_holidays # return true or false

# dia_semana = calendar.weekday(ano, mes, dia) # return a number of week
