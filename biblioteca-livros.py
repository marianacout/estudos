import matplotlib.pyplot as plt

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        
    def __str__(self):
        return f"{self.titulo}, por {self.autor}, Publicado em {self.ano_publicacao}"


biblioteca = []
anos = []

def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao) 
    print(f"O livro '{titulo}' foi adicionado à biblioteca.")

def listar_livros():
    print("\nLivros na Biblioteca:")
    for livro in biblioteca:
        print(livro)
        
adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e Preconceito", "Jane Austin", 1813)
adicionar_livro("1984", "George Orwell", 1949)
adicionar_livro("Cem Anos de Solidão", "Gabriel Garcia Marquez", 1967)
adicionar_livro("Apanhador no Campo de Centeio", "J.D. Salinger", 1951)

listar_livros()

anos = list(set(anos)) 
anos.sort()

contagem_por_ano = [anos.count(ano) for ano in anos]

plt.plot(anos, contagem_por_ano, marker='o', linestyle='-', color= 'red')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por ano de Publicação')

for i, valor in enumerate(contagem_por_ano):
    plt.text(anos[i], valor, str(valor), ha='center', va='bottom')
    
plt.grid(True)

plt.show()