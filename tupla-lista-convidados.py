#Tupla de convidados
convidados = ("Mariana", "Fabricio", "Guilherme", "Heitor", "Surpresa")

#Lista de confirmações
confirmados = ["Fabricio", "Heitor"]

#Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

#Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)

#Enviar lembrete aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram.")