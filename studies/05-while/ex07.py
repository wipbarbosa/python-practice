
contagem = 0
while contagem <5:

    numeros = int(input("Digite 5 numeros"))
    if contagem == 0:
        maior = numeros
        menor = numeros
        soma = numeros
    elif contagem !=0:
        if maior < numeros:
            maior = numeros
        if menor > numeros:
            menor = numeros

        soma = soma + numeros
    
        
        
    

    contagem =  contagem +1




print(maior)
print(menor)
print(soma)
