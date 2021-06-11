import random, string


# tamanho da senha
size = int(input('Digite o tamanho da senha: '))

# estrutura da senha que será gerada
chars = string.ascii_letters + string.digits + '@!#%$&().-_+'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))
