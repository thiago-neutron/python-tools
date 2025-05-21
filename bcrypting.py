import bcrypt

# ----------------------------
# 🔐 Configurações e variáveis
# ----------------------------

# Senha original (em bytes)
senha_plana = b"MinhaSenhaSegura123!"

# Custo (fator de trabalho) - padrão seguro: 12
# Isso significa 2^12 = 4096 rounds
custo = 12

# Gerar salt aleatório com custo ajustável
salt = bcrypt.gensalt(rounds=custo)

# Gerar o hash da senha com o salt
hash_senha = bcrypt.hashpw(senha_plana, salt)

# ----------------------------
# 🔍 Verificação
# ----------------------------

# Senha a ser verificada (em bytes)
senha_tentativa = b"MinhaSenhaSegura123!"  # pode mudar para testar falhas

# Verificação: True se bater, False se for incorreta
senha_correta = bcrypt.checkpw(senha_tentativa, hash_senha)

# ----------------------------
# 📤 Saída
# ----------------------------

print(f"Senha original: {senha_plana.decode()}")
print(f"Salt usado: {salt}")
print(f"Hash gerado: {hash_senha}")
print(f"Senha correta? {senha_correta}")
