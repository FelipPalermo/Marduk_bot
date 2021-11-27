import pickle
import C_Personagem
Nome = C_Personagem.Nome
PT_Lista = []

def Selecionar_Pericias_Treinadas():
    
    #Nome_p = input("Nome do personagem que deseja adicionar as pericias treinadas")
    Loop = True

    Pericias_Treinadas = ["Ciencia", "Crime","Hacking", "Labia", "Luta", 
                        "mecanica", "Medicina", "Nanotecnologia",
                        "Pilotagem", "Pisionismo", "Sobrevivencia"]

    Mostrar_Pericias = 0 
    for i in Pericias_Treinadas:
        
        print(f" {Mostrar_Pericias} = {i} ")
        Mostrar_Pericias += 1 

    while Loop == True:
        
        # Try para não quebrar o bot
        try:
            
            # Pericias Treinadas
            PT_1 = int(input("Escolha Uma das pericias de 0 a 10"))
            
            # Pericias Chose 1 
            PC1 = Pericias_Treinadas[PT_1]

            PT_2 = int(input("Escolha Uma das pericias de 0 a 10"))
            PC2 = Pericias_Treinadas[PT_2]

            PT_3 = int(input("Escolha Uma das pericias de 0 a 10"))
            PC3 = Pericias_Treinadas[PT_3]

            PT_4 = int(input("Escolha Uma das pericias de 0 a 10"))
            PC4 = Pericias_Treinadas[PT_4]

            Loop = False
        
        except:
            print("Algo deu errado, por favor, tente novamente!")

    # Transforma as escolhas do jogador em uma lista
    C_Personagem.Atributos = [C_Personagem.Nome,C_Personagem.Raca_c,C_Personagem.Vigor,
    C_Personagem.Vontade,C_Personagem.Vitalidade,C_Personagem.Percepcao,C_Personagem.Reflexo,
    C_Personagem.Zanites,PC1, PC2, PC3, PC4]

    # Salva a lista criada a cima em um arquivo
    Salvar_Arquivo = open(f"Personagens/{Nome}.pickle", "wb")
    pickle.dump(C_Personagem.Atributos, Salvar_Arquivo)
    Salvar_Arquivo.close()

Selecionar_Pericias_Treinadas()


def Atribuir_Pontos_PT():

    Pontos_PT = True

    while Pontos_PT == True:
        
        # Abrir arquivo com as pericias treinadas
        Abrir_PT = open(f"Personagens/{C_Personagem.Nome}.pickle", "rb")
        Ler_PT = pickle.load(Abrir_PT)
        Escrever_PT = open(f"Personagens/{C_Personagem.Nome}.pickle", 'wb')

        # Mostrar quantos pontos o jogador ainda tem para gastar
        print(f'\nVocê ainda tem {C_Personagem.Pontos} Pontos!')

        # PericiaTreinada Input ChosePoints1 
        PTI_CP1 = int(input(f"Quantos pontos você quer atribuir a {Ler_PT[8]}?"))
        Ler_PT[8] = f'{Ler_PT[8]} : {PTI_CP1}'
        
        # Checar se os pontos são iguais a zero
        # Se forem o programa fecha
        if C_Personagem.Pontos == 0 or C_Personagem.Pontos <= 0:
            
            print("você não tem pontos o suficiente para adiconar")
            Ler_PT[8] = f'{Ler_PT[8]} : 0'

        # Se não o programa continua
        else : 
            C_Personagem.Pontos -= PTI_CP1
            
        
        # Todas as vezes que inserimos um valor referente a um index da lista
        # Fechamos o arquivo, caso o contrario buga e não da certo.
        Escrever_PT = open(f"Personagens/{C_Personagem.Nome}.pickle", 'wb')
        pickle.dump(Ler_PT, Escrever_PT)
        Escrever_PT.close()

        # Mostrar quantos pontos o jogador ainda tem para gastar
        print(f'\nVocê ainda tem {C_Personagem.Pontos} Pontos!')

        PTI_CP2 = int(input(f"Quantos pontos você quer atribuir a {Ler_PT[9]}?"))
        
        
         # Checar se os pontos são iguais a zero
        # Se forem o programa fecha
        if C_Personagem.Pontos == 0 or C_Personagem.Pontos <= 0:
            
            print("você não tem pontos o suficiente para adiconar")
            Ler_PT[9] = f'{Ler_PT[9]} : 0'

        # Se não o programa continua
        else : 
            Ler_PT[9] = f'{Ler_PT[9]} : {PTI_CP2}' 
            C_Personagem.Pontos -= PTI_CP2

        # Todas as vezes que inserimos um valor referente a um index da lista
        # Fechamos o arquivo, caso o contrario buga e não da certo.
        Escrever_PT = open(f"Personagens/{C_Personagem.Nome}.pickle", 'wb')
        pickle.dump(Ler_PT, Escrever_PT)
        Escrever_PT.close()

        # Mostrar quantos pontos o jogador ainda tem para gastar
        print(f'\nVocê ainda tem {C_Personagem.Pontos} Pontos!')

        PTI_CP3 = int(input(f"Quantos pontos você quer atribuir a {Ler_PT[10]}?")) 
        
         # Checar se os pontos são iguais a zero
        # Se forem o programa fecha
        if C_Personagem.Pontos == 0 or C_Personagem.Pontos <= 0:
            
            print("você não tem pontos o suficiente para adiconar")
            Ler_PT[10] = f'{Ler_PT[10]} : 0'

        # Se não o programa continua
        else : 
            Ler_PT[10] = f'{Ler_PT[10]} : {PTI_CP3}'
            C_Personagem.Pontos -= PTI_CP3

        # Todas as vezes que inserimos um valor referente a um index da lista
        # Fechamos o arquivo, caso o contrario buga e não da certo.
        Escrever_PT = open(f"Personagens/{C_Personagem.Nome}.pickle", 'wb')
        pickle.dump(Ler_PT, Escrever_PT)
        Escrever_PT.close()

        # Mostrar quantos pontos o jogador ainda tem para gastar
        print(f'\nVocê ainda tem {C_Personagem.Pontos} Pontos!')

        PTI_CP4 = int(input(f"Quantos pontos você quer atribuir a {Ler_PT[11]}?"))
         

         # Checar se os pontos são iguais a zero
        # Se forem o programa fecha
        if C_Personagem.Pontos == 0 or C_Personagem.Pontos <= 0:
            
            print("você não tem pontos o suficiente para adiconar")
            Ler_PT[11] = f'{Ler_PT[11]} : 0'

        # Se não o programa continua
        else : 
            Ler_PT[11] = f'{Ler_PT[11]} : {PTI_CP4}'
            C_Personagem.Pontos -= PTI_CP4
        
        # Todas as vezes que inserimos um valor referente a um index da lista
        # Fechamos o arquivo, caso o contrario buga e não da certo.
        Escrever_PT = open(f"Personagens/{C_Personagem.Nome}.pickle", 'wb')
        pickle.dump(Ler_PT, Escrever_PT)
        Escrever_PT.close()

        Pontos_PT = False

Atribuir_Pontos_PT()



