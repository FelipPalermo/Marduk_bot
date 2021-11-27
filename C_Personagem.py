# ------------------------------------------ Importações ///
import pickle



# ------------------------------------------ ATRIBUTOS /// 

Pontos = 12
Vigor = 0 
Reflexo = 0 
Percepcao = 0 
Vontade = 0 
Vitalidade = 0
Zanites = 400 
Nome = ''

# ------------------------------------------ RAÇAS ///

def Androide():
    global Pontos
    global  Vigor
    global Reflexo
    global Percepcao
    global Vitalidade
    global Raca_c

    Pontos += 2
    Vigor += 1 
    Reflexo += 1
    Percepcao += 1
    Vitalidade += 9
    Raca_c = 'Androide'

def Gorf():
    global  Vigor
    global Reflexo
    global Percepcao
    global Vitalidade 
    global Raca_c

    Vigor += 2
    Vitalidade += 11
    Raca_c = 'Gorf'

def Humano():
    global  Vigor
    global Reflexo
    global Percepcao
    global Vitalidade 
    global Vontade
    global Raca_c

    Vontade += 1 
    Vigor += 1 
    Reflexo += 1
    Percepcao += 1
    Vitalidade += 10
    Raca_c = 'Humano'

def Pisonico():
    global Pontos
    global Vigor
    global Reflexo
    global Percepcao
    global Vitalidade 
    global Vontade
    global Raca_c

    Pontos += 2
    Vigor += 1 
    Reflexo += 1
    Percepcao += 1
    Vontade += 2
    Vitalidade += 9
    Raca_c = 'Pisonico'
     
def Zark():
    global Reflexo
    global Percepcao
    global Vontade
    global Vitalidade
    global Raca_c
    Reflexo += 2
    Percepcao += 1 
    Vontade += 1
    Vitalidade += 11 
    Raca_c = 'Zark'

# ------------------------------------------ Variaveis QUe serao mudadas no Loop ///

Raca = False
Raca_c = ''
Loop_PT = False
Pereicias_Teinadas = 0
Atributos = []

# ------------------------------------------ Loop Principal ///

def Criar_Personagem():
    
    global Pontos
    Escolher_Nome = False
    global Vigor
    global Reflexo 
    global Percepcao
    global Vontade
    global Vitalidade
    global Atributos 
    global Nome
    Loop_criar_Personagem = False



    while Loop_criar_Personagem == False:
        
            if Escolher_Nome == False: 
                Escrever_nome = input("Qual vai ser o nome do seu personagem?")
                Nome = Escrever_nome
                Escolher_Nome = True

            print(f'\nVocê ainda tem {Pontos} Pontos!')

            Vigor =  Vigor + int(input("Adicione pontos de atributo ao Vigor!"))
            Pontos -=   Vigor
            if Pontos <= 0:
                break
            if Vigor >= 7: 
                print("Numero de pontos excedido, porfavor, tente novamente!")
                break


            # Mostrar os pontos de atributo resstantes
            print(f'\nVocê ainda tem {Pontos} Pontos!')

            Reflexo = Reflexo + int(input("Adicione pontos de atributo ao Reflexo!"))
            Pontos -= Reflexo
            if Pontos <= 0:
                break
            if Reflexo >= 7: 
                print("Numero de pontos excedido, porfavor, tente novamente!")
                break
            
            print(f'\nVocê ainda tem {Pontos} Pontos!')

            Percepcao = Percepcao + int(input("Adicione pontos de atributo a Percepcao!"))
            Pontos -= Percepcao
            if Pontos <= 0:
                break
            if Percepcao >= 7: 
                print("Numero de pontos excedido, porfavor, tente novamente!")
                break

            print(f'\nVocê ainda tem {Pontos} Pontos!')

            Vontade = Vontade + int(input("Adicione pontos de atributo a Vontade!"))
            Pontos -= Vontade
            if Pontos <= 0:
                break
            if Vontade >= 7: 
                print("Numero de pontos excedido, porfavor, tente novamente!")
                break
            
            Loop_criar_Personagem = True

def Selecionar_Raca():
    
    while Raca == False:

        Escolher_Raca = input("Porfavor Escolha sua classe :\nAndroide\nGorf\nHumano\nPisonico\nZark").upper()
        print(str(Escolher_Raca))

        if Escolher_Raca == "ANDROIDE":
            Raca == True
            Androide()
            break     

        if Escolher_Raca == "GORF":
            Raca == True
            Gorf()
            break

        if Escolher_Raca == "HUMANO":
            Raca == True
            Humano()
            break

        if Escolher_Raca == "PISONICO":
            Raca == True
            Pisonico()
            break

        if Escolher_Raca == "ZARK":
            Raca == True
            Zark()
            break

        if Escolher_Raca == "AMONGUS":
            print("Eu achei que alguem podia tentar isso, então sim, você achou um easter egg")
            print("Mas infelizmente ele não acrescenta nada pro jogo, é so uma menssagem minha pra você mesmo")
            print("Eu acho que o maior concorrente a fazer isso é o lucairo, mas não duvido de ninguem")
        
        else:
            print("Nome de raça incoreto, porfavor insira sua raça denovo\n")



def Salvar_Personagem():

    global Vigor
    global Reflexo 
    global Percepcao
    global Vontade
    global Vitalidade
    global Atributos 
    global Raca_c
    global Nome

    # Lista com todos os atributos dos personagens
    Atributos = [Nome,Raca_c,Vigor,Vontade,Vitalidade,Percepcao,Reflexo,Zanites]


    # Variavel que abre o arquivo, com o nome e local onde deve ser escrito
    Save_Personagem = open(f"Personagens/{Nome}.pickle", 'wb')

    # Funcao da biblioteca pickle para salvar os arquivos " dump "
    pickle.dump(Atributos, Save_Personagem)

    # Fechar o arquivo para que ele seja salvo e nao receba alteracoes indesejadas 
    Save_Personagem.close()



# Inicia Criação do personagem e distribui os pontos primarios
Criar_Personagem()

# Seleciona raca
Selecionar_Raca()

# Salva opções escolhidas do usuario
Salvar_Personagem()

