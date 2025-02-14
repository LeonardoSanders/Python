from datetime import datetime

data_str = '2025-02-11 20:47:00'
data_fmt = '%Y-%m-%d %H:%M:%S'
data = datetime.strptime(data_str, data_fmt)
print(data)

d1 = datetime.now()
print(d1)