from datetime import date, timedelta, datetime

start_date = datetime.strptime(input('Data inicial (dd/mm/year):'), '%d/%m/%Y').date()
end_date = datetime.strptime(input('Data final (dd/mm/year):'), '%d/%m/%Y').date()
# date_final = input('Data final (dd/mm/year)')


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%d-%m-%Y"))