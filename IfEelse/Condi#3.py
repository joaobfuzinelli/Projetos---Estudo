#Variavel "numero" que armazena o valor tipo int "500"
numero = 501


#Função NumberCheck com If&Else que retorna um texto dependendo do valor que está na variável "numero"
def NumberCheck():
    try:
        if numero > 500:
            print(f"Esse número é maior que 500, ele é: {numero}")
        elif numero < 500:
            print(f"Esse número é menor que 500, ele é: {numero}")
        else:
            print("Esse número é 500")
    except KeyboardInterrupt:
        print("O usuário cancelou a operação")

numbertest = NumberCheck()