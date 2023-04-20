def fibonacci(num):
    z, x = 0, 1
    while x < num:
        z, x = x, z + x
    if x == num:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."


# Exemplo de uso
for k in range(2,8):
    resultado = fibonacci(k)
    print(resultado)
