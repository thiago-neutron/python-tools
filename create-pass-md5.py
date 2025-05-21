import random
import hashlib

def gerar_senha(tamanho=20):
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    caracteres_especiais = '!@#$%&*()-_=+[]{}<>?/'

    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais
    senha = ''

    # Garantir pelo menos um de cada tipo
    senha += random.choice(letras_maiusculas)
    senha += random.choice(letras_minusculas)
    senha += random.choice(numeros)
    senha += random.choice(caracteres_especiais)

    # Preencher o restante da senha
    for _ in range(4, tamanho):
        senha += random.choice(todos_caracteres)

    # Embaralhar a senha e retornar o hash MD5
    senha = ''.join(random.sample(senha, len(senha)))
    return senha, hashlib.md5(senha.encode()).hexdigest()

# Gerar 30 senhas
senha, hash_md5 = gerar_senha(20)
print("Senha:", senha)
print("MD5:", hash_md5)
