nome = input('Qual é seu nome? ')
idade = int(input('Qual é sua idade? '))

if 18 <= idade <= 24:
    print(f'Olá {nome}, pode entrar na festa!!')
elif 25 <= idade <= 34:
    print(f'Olá {nome}, pode entrar na festa, porém pague {idade * 2}!!')
else:
    print(f'Olá {nome}, não pode entrar na festa!!')
