#Variavel "nome" que recebe o valor "João Bruno"
nome = "João Bruno"

#Função definida "NameChecker" que ira retornar um tipo string no terminal, usando o If, else, e elif
def NameChecker():
    try:
        if nome == "João Bruno":
            print(f"Olá {nome}")
        elif nome != "João Bruno":
            print("Olá estranho")
        else:
            print("Tchau!")
    except TimeoutError:
        print("A operação não foi concluida")

Nome = NameChecker()

#Neste exemplo, foram utilizados os operadores "==" & "!="
