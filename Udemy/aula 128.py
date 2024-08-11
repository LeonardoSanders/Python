#Métodos úteis no Set
# add, update, clear, discard

s1 = set()
s1.add('Léo')
s1.add(1)
print(s1)
s1.update(('Olá, mundo',))
print(s1)
s1.discard('Léo') #Remove um elemento específico do set.
print(s1)
s1.clear() #Limpa todos os elementos presentes no Set.
print(s1)
