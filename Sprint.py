def linha():
    print ( "_" * 30)

# Menu para escolha de como o usúario realizará o login
def menu_pessoa():
     print ('''
======INFORME COMO DESAJA LOGAR NO SITE=======
        (1) Pessoa fisica 
        (2) Pessoa Juridica
==============================================''')
     escolha = int(input(""))
     return escolha

#login para acessar o site
def Login(escolha):
    novamente = 'sim'
    while novamente == 'sim' :
        match  escolha:
            case 1:
                novamente = "sim"
                while novamente == "sim" or novamente == "s"  :
                    Nome = input("Nome de usuario: ")
                    senha = input("senha: ") 
                    if Nome == 'XXX' and senha == 'XXX':
                        login = [(Nome, senha)]
                        break
                    else:
                        novamente = input("nome ou senha incorreta! Deseja digitar novamente? (Caso nâo queira o programa será finalizado) ")
                        if novamente == 'não' or novamente == 'n':
                            exit(print("Programa Finalizado Volte sempre"))
            case 2:
                novamente = "s"
                while novamente == "sim" or novamente == "s" :
                    Nome_emp = input("Digite o Nome da empresa: ")
                    cnpj = float(input("Informe eu cnpj: "))
                    if Nome_emp == "XXX" and cnpj == "XXX":
                        login = [(Nome_emp) (cnpj)]
                    else:
                        novamente = input("nome ou cnpj incorreta! Deseja digitar novamente? (Caso n queira o programa será finalizado) ")
                        if novamente == 'não' or novamente == 'n':
                            exit(print("Programa Finalizado Volte sempre"))
            case _:
                print ('Escolha invalida')
                novamente = input("Gostaria de escolher novamente? ")
                if novamente == 'não' or novamente == 'n':
                    exit(print("Programa Finalizado Volte sempre"))
        return login

# Coletar dados da bike para validação
def coleta_dados_bike():
    dados = {} 
    list_cor = []  
    Marca = (input("Digite a Marca da bike: "))
    Numeracao = (input("Digite a numeração da bike: ")) 
    cor = (input("Digite a cor da bike(Ex: Amarela , Preta): "))
    cores = cor.split(",")
    list_cor.append(cores)
    ano_bike = int(input("Digite o ano de frabricação da bike: "))
    valor_mercado = float(input("Digite o valor de mercado da bike: "))
    funcao = input("Digite a função da bike (ex: Trabalho, lazer, competição, )")
    modelo = input("Informe o modelo da sua bike (Ex: Bmx, ...)")

    dados = {'Marca ' : Marca, 'cor' : list_cor, 'Ano' : ano_bike, 'Valor de Mercado' : valor_mercado, 
            'função' : funcao, "Modelo" : modelo, "Numeracao": Numeracao}
    return dados

# Munu para caso o usúario tenha feito alguma modificação na bike
def menu_acessorio():
    print ('''
==================Acessorio==================
(1) Caso sua bike tenha acessorios 
(2) aso não tenha acessorios
==============================================''')
    escolha = int(input(""))
    return escolha

# 
def acessorios(escolha):
    match escolha:
        case 1:
            acessorio = {}
            lista_acessorio = []
            acessorio = input("Informe as Modificação feitas: ")
            acessorios = acessorio.split (" , ")
            lista_acessorio =acessorios.append(acessorios)
            acessorio = {"Acessorio " : lista_acessorio}
            return acessorio
        case 2: 
            print ('Ok, vamos continuar')

#
def exibir_dados(dados, acessorio):
    print("===============CONFIMAÇÂO DE DADOS=======================")
    print(f''' Marca: {dados[0]} 
    Cor: {dados[1]}
    Cor: {dados[2]}
    Cor: {dados[3]}
    Cor: {dados[4]}
    Cor: {dados[5]}
    Cor: {dados[6]}
    Cor: {dados[7]}
''')

#
def exibir():
    Login(menu_pessoa())
    linha()
    coleta_dados_bike()
    linha()
    acessorios(menu_acessorio())
    linha()
    exibir_dados()

#
def principal():
    exibir()


#PROGRAMA PRINCIPAL
principal()