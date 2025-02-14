import calendar

#imprime o calendario do ano
#print(calendar.calendar(2025))

#imprime o calendario de um mês específico
#print(calendar.month(2025, 3))

#imprime o primeiro dia da semana do mes[index] e o ultimo dia do mes(int)
num_primeiro_dia, ultimo_dia = calendar.monthrange(2025, 3)

#Retorna o index do primeiro dia do mes
print(calendar.day_name[num_primeiro_dia])

#Retorna o index do ultimo dia do mes
print(calendar.day_name[calendar.weekday(2025, 3, ultimo_dia)])

#É possível obter uma lista de numeros de dias do mes, que possuem index relacionados aos dias 
# da semana:

for week in calendar.monthcalendar(2025, 3):
    print(week)
    #PS: os dias correspondentes a 0 nao fazem parte do respectivo mes

    for day in week:
        if day == 0:
            continue

        print(day)
        #Imprime somente os dias que pertecem ao respectivo mes