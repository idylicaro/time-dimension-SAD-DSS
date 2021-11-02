from datetime import date, timedelta, datetime
import calendar
import locale
import pyodbc

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR')
except:
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')


# pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')

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
get_trimestre_name = lambda n, y: f'{n}º Trimestre / {y}'
get_semestre_name = lambda n, y: f'{n}º Semestre / {y}'


def get_trimestre(n):
    if n <= 3:
        return 1
    elif 3 < n <= 6:
        return 2
    elif 6 < n <= 9:
        return 3
    elif n > 9:
        return 4


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


with open('./url.txt', 'r') as f:
    DB_URL = f.readline()
    if not DB_URL:
        print("Can't read you DB URL!")
        exit(1)
    f.close()

old_start_date = start_date = datetime.strptime(input('Data inicial (dd/mm/year):'), '%d/%m/%Y').date()
old_end_date = end_date = datetime.strptime(input('Data final (dd/mm/year):'), '%d/%m/%Y').date()

history = [(old_start_date, old_end_date)]

connection = pyodbc.connect(DB_URL)
cursor = connection.cursor()

flag = True
while flag:

    for single_date in daterange(start_date, end_date):
        day = single_date.strftime("%d")
        month = single_date.strftime("%m")
        year = single_date.strftime("%Y")
        weekDay = calendar.weekday(int(year), int(month), int(day))

        cursor.execute(
            "insert into DIM_TEMPO(Data, Dia, DiaSemana, FimSemana, Quinzena, Mes, NomeMes, FimMes, Trimestre, NomeTrimestre, Semestre, NomeSemestre, Ano) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            single_date.strftime("%Y%m%d"), int(day), get_week_day_name(weekDay), isWeekend(weekDay), get_quinzena(int(day)), int(month), single_date.strftime("%B").title(),
            isEndOfMonth(day, calendar.monthrange(int(year), int(month))[1]), get_trimestre(int(month)), get_trimestre_name(get_trimestre(int(month)), int(year)), get_semestre(int(month)),
            get_semestre_name(get_semestre(int(month)), int(year)), year)


        print('Data:', single_date.strftime("%d-%m-%Y"))
        print('Dia:', day)
        print(get_week_day_name(weekDay))
        print('FimdeSemana:', isWeekend(weekDay))
        print('Quinzena:', get_quinzena(int(day)))
        print('Mes:', month)
        print(single_date.strftime("%B").title())
        print('FimdeMes:', isEndOfMonth(day, calendar.monthrange(int(year), int(month))[1]))
        print('Trimestre:', get_trimestre(int(month)))
        print(get_trimestre_name(get_trimestre(int(month)), int(year)))
        print('Semestre:', get_semestre(int(month)))
        print(get_semestre_name(get_semestre(int(month)), int(year)))
        print('Ano:', year)
        print('\n')

        want_continue = input("Digite 'y' se quer continuar a incluir mais datas e 'n' para parar: ")
        if want_continue != 'y':
            flag = False
            exit(1)

        start_date = datetime.strptime(input('Data inicial (dd/mm/year):'), '%d/%m/%Y').date()
        end_date = datetime.strptime(input('Data final (dd/mm/year):'), '%d/%m/%Y').date()

        for x in history:
            # Start 02/11/2021 < End 21/11/2021 Break
            # End 21/11/2021 > Start 02/11/2021 Break
            if start_date < x[1] or end_date > x[0]:
                print('Esta data é invalida, vai gerar duplicidade!')
                flag = False
                exit(1)

connection.commit()
