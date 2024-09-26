import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [120, 90, 150, 80, 200]

plt.bar(meses, vendas, color='black')

plt.xlabel('Mês')
plt.ylabel('Vendas (em unidades)')

plt.title('Vendas Mensais')

plt.show()