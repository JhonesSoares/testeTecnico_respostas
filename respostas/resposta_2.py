#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verificar_letra_a(texto):
    texto_minusculo = texto.lower()
    quantidades_de_a = texto_minusculo.count('a')
    #print(quantidades_de_a)
    
    if 'a' in texto_minusculo:
        print('No seu texto contem a letra "a".')
        print(f'E a letra "a" aparece {quantidades_de_a} vezes no seu texto.')
    else:
        print(f'No seu texto não contém letra "a".')    


texto = str(input('Digite uma frase de efeito: '))
verificar_letra_a(texto)