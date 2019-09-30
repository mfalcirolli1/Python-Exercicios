# Tuplas com Times de Futebol

classificacao = ('FLAMENGO', 'PALMEIRAS', 'SANTOS', 'CORINTHIANS', 'INTERNACIONAL', 'SÃO PAULO', 'GRÊMIO', 'BAHIA', 'ATHLETICO', 'ATLÉTICO-MG', 'BOTAFOGO', 'GOIÁS', 'VASCO', 'CEARÁ', 'FORTALEZA', 'FLUMINENSE', 'CRUZEIRO', 'CSA', 'AVAÍ', 'Chapecoense')

print('-='*30)
print(f'Classificação do Campeonato Brasileiro 2019 (30 de Setembro): {classificacao}')
print('-='*30)
print(f'Faze de grupos da Copa Libertadores: {classificacao[0:4]}')
print('-='*30)
print(f'Qualificatórias da Copa Libertadores: {classificacao[4:6]}')
print('-='*30)
print(f'Zona de Rebaixamento: {classificacao[-4:]}')
print('-='*30)
print(f'Ordem alfabética: {sorted(classificacao)}')
print('-='*30)
print(f'Chapecoense está na {classificacao.index("Chapecoense")+1}ª posição.')