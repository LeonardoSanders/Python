
#dir(nome da variável) - Utilizado para verificar todos os atributos presentes no elemento.
#O comando deve ser utlizado dentro do debugger do Python!

string = 'Léo'

#hasattr - Utilizado para verificar se determinada variável possui determinado método
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

#getattr - Retorna o valor especifico de dentro de uma variável específica.
#É possível utilizar variáveis em forma de métodos:
metodo = 'lower'
if hasattr(string, metodo):
    print('Existe lower')
    print(getattr(string, metodo)())