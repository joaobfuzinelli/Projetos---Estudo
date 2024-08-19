#Variavel "idade", que armazena uma informação tipo int
idade = 18

#Função "verificador", que verifica o valor inteiro que está armazenado na variavel "idade"
def verificador():
    try:
        if idade < 18:
            print("Você não pode entrar")
        elif idade >= 25:
            print("A sua idade é maior ou igual a 25")
        else:
            print("Você pode entrar")
    except KeyboardInterrupt:
        print("O usuário cancelou a operação")

DataChecker = verificador()

#Neste exemplo básico, foram utilizados os operadores "<" & ">="