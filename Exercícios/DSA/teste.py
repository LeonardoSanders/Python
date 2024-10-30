palavra_certa = 'banana'
palavra_usuario = ['_', '_', '_', '_', '_', '_']
letra = input('Digite uma letra: ')

for i, letras in enumerate(palavra_certa):
    if letras == letra:
        palavra_usuario[i] = letra

print(palavra_usuario)