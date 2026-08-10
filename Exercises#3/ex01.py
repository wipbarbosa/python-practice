#1. Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)

i = 1
while i <= 10:
    print(f"--- Tabuada do {i} ---")
    
    j = 1
    while j <= 10:
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
        j += 1 
        
    print() 
    i += 1 