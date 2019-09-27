# Validação de dados

sexo = str(input('Informe qual é o seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Tente novamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
