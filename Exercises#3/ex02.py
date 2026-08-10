# 2. Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição

i = 1
j = 1

while i <= 10:
    print(f"{i} x {j} = {i * j}")
    
    j += 1  
    
    if j > 10:
        j = 1
        i += 1
        print()