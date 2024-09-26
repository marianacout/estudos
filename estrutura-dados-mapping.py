dict_1 = {}
dict_1['nome'] = "Maria"
dict_1['idade'] = 25
print(dict_1)

dict_2 = {'nome': 'Maria', 'idade': 25}

dict_3 = dict([('nome', "Maria"), ('idade', 25)])

dict_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))
print(dict_1 == dict_2 == dict_3 == dict_4)
print(dict_4)