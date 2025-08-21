from cabecalho import exibir_cabecalho

print('=='*30)
exibir_cabecalho('D051 - Pergunte se o usuário tem senha correta e login correto', '21/08/2025')
print('=='*30)

login_correto = "admin"
senha_correta = "1234"
login = input('Digite seu login: ').strip().lower()
senha = input('Digite sua senha: ').strip()

if login == login_correto and senha == senha_correta:
    print('Acesso concedido. Bem-vindo!')
else:
    print('Acesso negado. Login ou senha incorretos.')