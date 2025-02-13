from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_ini = datetime.strptime('13/03/1995 09:30:30', fmt)
data_fim = datetime.strptime('12/02/2025 12:20:20', fmt)
delta = data_fim - data_ini
print(delta)
print(data_ini.strftime('%d/%m/%Y'))
