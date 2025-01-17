s = '8hypotheticall024y6wxz'

lista_com = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9','A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_input = list(s.upper())
result = ''

for c in lista_input:
    if c in lista_com:
        lista_com.remove(c)

for i in lista_com:
    result += i.lower()

print(result)