filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]


#Boas vindas ao usuário:
print("Bem-vindo à classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para sair. \n") #(\n é usado pra quebra de linha)


#Loop pra interar sobre cada filme na lista
for filme in filmes:
    classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (ou 0 para sair): ")

    if classificacao == '0': #verifica se o usuário prefere sair
        print("Que pena que você não irá classificar mais os filmes.")
        break #encerra o looping principal

    classificacao = int(classificacao) #converte a classificação para um número inteiro
    if classificacao < 1 or classificacao > 5: #verifica se a classificação está dentro do intervalo válido
        print("Por favor, digite uma classificação válida de 1 a 5.")
    else:
        print(f"Você classificou '{filme}' com {classificacao} estrelas. \n") #exibe a classificação e passa para o próximo filme

print("Obrigado por classificar seus filmes!") #agradece ao finalizar.