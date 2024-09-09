#lista de notas do estudante
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

#função regular para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

#função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

#calcular a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

#verificar se os estudantes foram aprovados
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

#resultados
print("Notas dos estudante:", notas)
print("Média das notas:", media_arredondada)
print("Situação do estudante:", situacao)
