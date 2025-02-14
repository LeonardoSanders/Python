from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000

data_emprestimo = datetime(2020, 12, 20)
delta_ano = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_ano

datas_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final_emprestimo:
    datas_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

valor_parcelas = valor_emprestimo / len(datas_parcelas)

for data in datas_parcelas:
    print(f'{data.strftime('%d/%m/%Y')} - R$ {valor_parcelas:,.2f}')