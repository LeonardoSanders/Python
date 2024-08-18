#Introdução à Generator functions em Python

def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Continuando...')
    yield 3
    print('Vou acabar...')
    return 'Acabou!'
#yield funciona como um "pause" na função. Ela retorna um valor mas não encerra a execução da função igual ao return
#É preciso usar o método "next" para obter o valor de yield na variável generator!

gen = generator()
for n in gen:
    print(n)


# generator = (n for n in range(1000000))
def generator2(n=0, max=10):
    while True:
        yield n
        n += 1
        if n > max:
            return 


gen2 = generator2()
for n in gen2:
    print(n)