from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1000000
parcelas = 60
valor_parcelas = valor_emprestimo/parcelas

data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_anos

datas_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final_emprestimo:
    datas_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

print(f'Vencimento das parcelas | Valor da Parcela')

for parcelas in datas_parcelas:
    print(parcelas.strftime('%d/%m/%Y'), f'- R$ {valor_parcelas:,.2f}')