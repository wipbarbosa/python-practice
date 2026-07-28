contador = 0
soma = 0 


while contador < 5:

    nota = int(input("Digite 5 notas"))
     
    while nota < 0 or nota > 10:

        print ("somente aceita notas entre 0 e 10")
        nota = int(input("Digite 5 notas"))
    
    soma = soma + nota
    contador = contador +1

            
       
media = soma /5

print (contador)
print(soma)
print (media)

    
    
        


        