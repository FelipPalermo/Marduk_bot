import pickle


def Ler_Atributos():
    Loop = True 

    while Loop == True :
        try : 
            # Variavel que vai buscar pelos atributos pelo nome retonado
            Nome_Personagem = input("Qual o nome do seu personagem?")
            print(Nome_Personagem)

            # Ler o arquivo criado previamente
            abrir = open(f'Personagens/{Nome_Personagem}.pickle', 'rb')
            ler_pickle = pickle.load(abrir)

            # Ler atributos dos personagens 
            print(f'            HP : {ler_pickle[4]}')
            print(f'            Zanites : {ler_pickle[7]}\n')

            print(f'            Nome : {ler_pickle[0]}     Raca : {ler_pickle[1]}\n')

            print("------------------------ Atributos ------------------------\n")

            
            print(f'Vigor : {ler_pickle[2]}         Vontade : {ler_pickle[3]}')
            print(f'Percepcao : {ler_pickle[5]}     Reflexo : {ler_pickle[6]}\n')

            print("-------------------- Pericias Treinadas --------------------\n")

            print(f'{ler_pickle[8]}         {ler_pickle[9]}')
            print(f'{ler_pickle[10]}        {ler_pickle[11]}')

            # Fechar o arquivo para evitar alterações indesejadas 
            abrir.close()
            Loop = False

        except: 
            print("Nome incorreto, tente novamente!")



Ler_Atributos()