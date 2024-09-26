class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    def acelerar(self, incremento):
        self.velocidade += incremento
        
    def frear(self, decremento):
        self.velocidade -= decremento
        
    def status(self):
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAno: {self.ano}, \nVelocidade: {self.velocidade} km/h."

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia
        
    def acelerar(self, incremento): 
        self.velocidade += incremento + self.potencia
        
    
class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo
        
    def status(self):
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAno: {self.ano}, \nTipo: {self.tipo}, \nVelocidade: {self.velocidade} km/h."
    
carro1 = Carro("Toyota", "Corolla", 2022, 150)
bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

carro1.acelerar(50)
bicicleta1.acelerar(20)

print("Status do Carro:")
print(carro1.status())

print("\nStatus da Bicicleta:")
print(bicicleta1.status())