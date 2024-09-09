#Bem vind0 à maquina de venda automática de ingressos de cinema

#Solicite a idade do cliente:
idade = int (input("Por favor, digite a sua idade: "))

#Verifica a idade para sugestão de filmes
if idade < 12:
    print("Recomendamos o filme infantil PROCURANDO NEMO.")
    quantidade_ingressos = 5
elif idade <= 12 and idade < 18:
    print("Recomendamos o filme adolescente ENCANTADA.")
    quantidade_ingressos = 3
else:
    print("Recomendamos o filme emocionante É ASSIM QUE ACABA.")
    quantidade_ingressos = 0

#Verifica a disponibilidade de ingressos
#Suponha que haja 10 ingressos disponíveis
if quantidade_ingressos > 0:
    print("Ingressos estão disponíveis. Divirta-se no cinema.")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")