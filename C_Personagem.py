# ------------------------------------------ Importações ///
import pickle



# ------------------------------------------ ATRIBUTOS /// 

Pontos = 15
 
Vigor = 0 
Reflexo = 0 
Percepcao = 0 
Vontade = 0 
Vitalidade = 0
Zanites = 0 
Nome = ""

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
Escolher_Nome = False 
Nome = ''

# ------------------------------------------ Loop Principal ///

while Pontos > 0:
    
    if Escolher_Nome == False: 
        Escrever_nome = input("Qual vai ser o nome do seu personagem?")
        Nome = Escrever_nome
        Escolher_Nome = True

    print("Você tem 15 pontos!\n")

    Vigor =  Vigor + int(input("Adicione pontos de atributo ao Vigor!"))
    Pontos -=   Vigor
    if Pontos <= 0:
        break
    if Vigor > 18: 
        print("Numero de pontos excedido, porfavor, tente novamente!")
        break


    # Mostrar os pontos de atributo restantes
    print(f'\nVocê ainda tem {Pontos} Pontos!')

    Reflexo = Reflexo + int(input("Adicione pontos de atributo ao Reflexo!"))
    Pontos -= Reflexo
    if Pontos <= 0:
        break
    if Reflexo > 18: 
        print("Numero de pontos excedido, porfavor, tente novamente!")
        break
    
    print(f'\nVocê ainda tem {Pontos} Pontos!')

    Percepcao = Percepcao + int(input("Adicione pontos de atributo a Percepcao!"))
    Pontos -= Percepcao
    if Pontos <= 0:
        break
    if Percepcao > 18: 
        print("Numero de pontos excedido, porfavor, tente novamente!")
        break

    print(f'\nVocê ainda tem {Pontos} Pontos!')

    Vontade = Vontade + int(input("Adicione pontos de atributo a Vontade!"))
    Pontos -= Vontade
    if Pontos <= 0:
        break
    if Vontade > 18: 
        print("Numero de pontos excedido, porfavor, tente novamente!")
        break

    if Pontos > 1: 
        print("Voce nao gastou todos os seus ponto, tente denovo, por favor")
        break
    
    if Raca == False:

        Escolher_Raca = input("Porfavor Escolha sua classe :\nAndroide\nGorf\nHumano\nPisonico\nZark").upper()
        print(str(Escolher_Raca))

        if Escolher_Raca == "ANDROIDE":
            Raca == True
            Androide()
        
        if Escolher_Raca == "GORF":
            Raca == True
            Gorf()

        if Escolher_Raca == "HUMANO":
            Raca == True
            Humano()

        if Escolher_Raca == "PISONICO":
            Raca == True
            Pisonico()

        if Escolher_Raca == "ZARK":
            Raca == True
            Zark()

        if Raca == True:
            break

# Lista com todos os atributos dos personagens
Atributos = [Nome,Raca_c,Vigor,Vontade,Vitalidade,Percepcao,Reflexo,Zanites]

# Variavel que abre o arquivo, com o nome e local onde deve ser escrito
Save_Personagem = open(f"Personagens/{Nome}.pickle", 'wb')

# Funcao da biblioteca pickle para salvar os arquivos " dump "
pickle.dump(Atributos, Save_Personagem )

# Fechar o arquivo para que ele seja salvo e nao receba alteracoes indesejadas 
Save_Personagem.close()