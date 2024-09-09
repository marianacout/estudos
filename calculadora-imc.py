peso = float(input("Digite o seu peso: "))

altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura * altura)
print(f"Seu IMC é: {imc}.")

if imc < 18.5:
    print("Você está abaixo do peso.")

elif imc >= 18.5 and imc <= 24.9:
    print("Você está com o peso ideal.")
elif imc >=25 and imc <= 29.9:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc <=34.9:
    print("Você está com obesidade grau I.")
elif imc >=35 and imc <= 39.9:
    print("Você está com obesidade grau II.")

else:
    imc >= 40
    print("Você está com obesidade grau III.")

print("Obrigada por calcular com a gente!")