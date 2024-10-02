def verificaFibonacci(numero):
    a, b = 0, 1 
    while b < numero: 
        a, b = b , a + b 
    if b == numero or numero == 0:
        return f"O numero {numero} pertence à sequencia de Fibonacci"
    else:
        return f"O numero {numero} não pertence à sequencia de Fibonacci"
        
numero = int(input("Qual numero deseja testar: "))
resultado = verificaFibonacci(numero)
print(resultado)
