import random 

class cadastro:
    def __init__(self, numero_de_caracteres):
        self.numero_de_caracteres = numero_de_caracteres

    def password(self, num):
        senha = ''
        for caractere in range(num):
            aleatorio = random.randint(48, 122)
            senha += chr(aleatorio)
        return senha


num = int(input('gerar senha com quantos caracteres >>>'))
test = cadastro(num)
print(f'PASSWD = {test.password(num)}') 