def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: \033[32mNÃO VOTA!\033[m'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO \033[33mOPCIONAL\033[m.'
    else:
        return f'Com {idade} anos: VOTO \033[31mOBRIGATÓRIO!!\033[m'


nas = int(input('Em que ano você nasceu: '))
print(voto(nas))
