def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não add a situação.
    :return: dicionário com várias informações sobre a situa da turma.
    '''
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['\033[situação'] = 'RUIM'
    return r


resp = notas(5.5, 1.5, 8.5, sit=True)
print(resp)
help(notas)
