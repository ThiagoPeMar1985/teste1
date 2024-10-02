def conta_letra(string):
    count = 0
    for char in string:
        if char.lower() =='a':
            count +=1
    return f"A letra a apareceu {count} vezes neste texto."

resultado = conta_letra(input("digite o texto: "))
print(resultado)