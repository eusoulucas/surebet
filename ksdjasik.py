
def somaMultiplos3ou5(numero):
  soma = 0
  for i in range(numero): 
    if (i % 3) == 0 or (i % 5) == 0:
      soma += i
  return soma

  
soma = somaMultiplos3ou5(500)
print(soma)
