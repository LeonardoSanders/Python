from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000

data_emprestimo = datetime(2020, 12, 20)
delta_ano = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_ano