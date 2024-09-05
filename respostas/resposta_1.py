#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# verifica numero usuario
def sequncia_fibonacci(numero):
    fib_sequencia = [0, 1]
    #print(fib_sequencia[-1])

    while fib_sequencia[-1] < numero:
        #print(fib_sequencia)
        novo_valor = fib_sequencia[-1] + fib_sequencia[-2]
        #print(novo_valor)

        fib_sequencia.append(novo_valor)

    return fib_sequencia

def pertence_fibonacci(numero):
    sequencia = sequncia_fibonacci(numero)
    #print(sequencia)

    if numero in sequencia:
        return f"O número {numero} pertence a sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence a sequência de Fibonacci."


numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)


