n1 = input('Digite um texto: ')

# Todos os "is" de strings:

print('\n--- RESULTADOS ---')

# Verifica se contém apenas letras
print('É alfabético?       ', n1.isalpha())
# Verifica se contém apenas números
print('É numérico?         ', n1.isnumeric())
# Verifica se contém apenas espaços
print('Só tem espaços?     ', n1.isspace())
# Verifica se contém letras e números
print('É alfanumérico?     ', n1.isalnum())
# Verifica se está todo em maiúsculas
print('Está em maiúsculas? ', n1.isupper())
# Verifica se está todo em minúsculas
print('Está em minúsculas? ', n1.islower())
# Verifica se está no formato de título
# Exemplo: "Python"
print('Está em formato de título? ', n1.istitle())
