# O Count é um método de itertools considerado um iterador sem fim
from itertools import count

c1 = count()
r1 = range(10)

#Para verificar se um dado método/função é um iterável e iterador é preciso verificar
# se possui o atributo iter(iterável) e next(iterador):

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))
#Ou seja, count é iterável e iterador mas range não!
#A principal diferença entre o Count e o Range é que Count não tem fim, ou seja, é
#possível definir o Start e Step da contagem, mas não o limite!