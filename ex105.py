# Analisando e gerando Dicionários


def analise(*n, sit=False):
    """
    -> Analisar notas de vários alunos
    :param n: Notas
    :param sit: Situação geral dos alunos
    :return: Dicionários com várias informações
    """
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n) / len(n)

    if sit:
        if dic['média'] > 7:
            dic['Situação'] = 'Ótimo'
        elif 5 <= dic['média'] < 7:
            dic['Situação'] = 'Regular'
        elif dic['média'] < 5:
            dic['Situação'] = 'Péssimo'

    return dic


resp = analise(5, 8, 7, 9, 7.5, 8.5, 9.5,  sit=True)
print(resp)
help(analise)

