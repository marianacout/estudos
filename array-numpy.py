import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print("Array original:")
print(my_array)


squared_array = my_array ** 2 
sum_of_elements = np.sum(my_array) 

print("\nArray ao quadrado:")
print(squared_array)
print("\nSoma dos elementos:")
print(sum_of_elements)

element_at_index_2 = my_array[2] 
print("\nElemento no índice 2:", element_at_index_2)