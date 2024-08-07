# Calculo do primeiro digito
CPF_enviado_usuario = '02837351393' # '74682489070'
nove_digitos = CPF_enviado_usuario[:9]
CPF_soma_1 = 0
contador_1 = 10
for digitos1 in nove_digitos:
    CPF_soma_1 += int(digitos1) * contador_1
    contador_1 -= 1
CPF_resto_1 = (CPF_soma_1 * 10) % 11
CPF_p_digit = CPF_resto_1 if CPF_resto_1 <= 9 else 0
# Calculo do segundo digito
dez_digitos = nove_digitos + str(CPF_p_digit)
CPF_soma_2 = 0
contador_2 = 11
for digitos2 in dez_digitos:
    CPF_soma_2 += int(digitos2) * contador_2
    contador_2 -= 1
CPF_resto_2 = (CPF_soma_2 * 10) % 11
CPF_s_digit = CPF_resto_2 if CPF_resto_2 <= 9 else 0
cpf_gerado_calculo = f'{nove_digitos}{CPF_p_digit}{CPF_s_digit}'
if CPF_enviado_usuario == cpf_gerado_calculo:
    print('CPF válido')
else:
    print('CPF inválido')