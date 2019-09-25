# Média

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}.'.format(n1, n2, m))
if m >= 7:
    print('Sendo a nota mínima para aprovação = 7.0 e mínima para recuperação = 5.0, o Aluno está \033[1;32mAPROVADO!\033[m')
elif 5 <= m <= 6.9:
    print('Sendo a nota mínima para aprovação = 7.0 e mínima para recuperação = 5.0, o Aluno está de \033[1;35mRECUPERAÇÃO!\033[m')
else:
    print('Sendo a nota mínima para aprovação = 7.0 e mínima para recuperação = 5.0, o Aluno está \033[1;31mREPROVADO!\033[m')