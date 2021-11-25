import pickle

def Alterar_Atributos():
    
    Loop = True 
    
    while Loop == True:
        # Variavel usada para alterar os atributos dos personagens
        Var_atr = 0

        # Indicar qual arquivo deve ser lido // Ler arquivo 
        Nome_Do_Personagem = input("Nome do Personagem")

        try:
            
            # Deifinir arquivos para leitura
            Ler_Arquivo = open(f'Personagens/{Nome_Do_Personagem}.pickle', 'rb')
            Ler_Atributos = pickle.load(Ler_Arquivo)

            # Receber atributo que o jogador deseja alterar
            Atributo = input("Qual atributo você deseja alterar?")
            
            # try está sendo usado para não interromper o codigo caso de algum erro
            try:
                if Atributo == "vigor" or Atributo == "Vigor" or  Atributo == "VIGOR":
                    
                    # Definir arquivo onde vão ser salvos os novos atributos
                    Escrever_Arquivo = open(f'Personagens/{Nome_Do_Personagem}.pickle', 'wb')
                    
                    # Alterar atributos
                    A_vigor = int(input("Quantos pontos você deseja colocar?"))
                    Var_atr = A_vigor
                    Ler_Atributos[2] += Var_atr
                    
                    # Salvar Atributos novos no arquivo do personagem
                    pickle.dump(Ler_Atributos, Escrever_Arquivo)     

                    # Fechar arquivos para evitar alterações indesejadas            
                    Ler_Arquivo.close()
                    Escrever_Arquivo.close()


                if Atributo == "vontade" or Atributo == "Vontade" or  Atributo == "VONTADE":
                    
                    # Definir arquivo onde vão ser salvos os novos atributos
                    Escrever_Arquivo = open(f'Personagens/{Nome_Do_Personagem}.pickle', 'wb')
                    
                    # Alterar atributos
                    A_Vontade = int(input("Quantos pontos você deseja colocar?"))
                    Var_atr = A_Vontade
                    Ler_Atributos[3] += Var_atr
                    
                    # Salvar Atributos novos no arquivo do personagem
                    pickle.dump(Ler_Atributos, Escrever_Arquivo)     

                    # Fechar arquivos para evitar alterações indesejadas            
                    Ler_Arquivo.close()
                    Escrever_Arquivo.close()

                if Atributo == "vitalidade" or Atributo == "Vitalidade" or  Atributo == "VITALIDADE":
                    
                    # Definir arquivo onde vão ser salvos os novos atributos
                    Escrever_Arquivo = open(f'Personagens/{Nome_Do_Personagem}.pickle', 'wb')
                    
                    # Alterar atributos
                    A_Vitalidade = int(input("Quantos pontos você deseja colocar?"))
                    Var_atr = A_Vitalidade
                    Ler_Atributos[4] += Var_atr
                    
                    # Salvar Atributos novos no arquivo do personagem
                    pickle.dump(Ler_Atributos, Escrever_Arquivo)     

                    # Fechar arquivos para evitar alterações indesejadas            
                    Ler_Arquivo.close()
                    Escrever_Arquivo.close()

                if Atributo == "percepcao" or Atributo == "Percepcao" or  Atributo == "PERCEPCAO" or Atributo == "Percepção" or Atributo == "percepção":
                    
                    # Definir arquivo onde vão ser salvos os novos atributos
                    Escrever_Arquivo = open(f'Personagens/{Nome_Do_Personagem}.pickle', 'wb')
                    
                    # Alterar atributos
                    A_Percepcao = int(input("Quantos pontos você deseja colocar?"))
                    Var_atr = A_Percepcao
                    Ler_Atributos[5] += Var_atr
                    
                    # Salvar Atributos novos no arquivo do personagem
                    pickle.dump(Ler_Atributos, Escrever_Arquivo)     

                    # Fechar arquivos para evitar alterações indesejadas            
                    Ler_Arquivo.close()
                    Escrever_Arquivo.close()

                if Atributo == "reflexo" or Atributo == "Reflexo" or  Atributo == "REFLEXO":
                    
                    # Definir arquivo onde vão ser salvos os novos atributos
                    Escrever_Arquivo = open(f'Personagens/{Nome_Do_Personagem}.pickle', 'wb')
                    
                    # Alterar atributos
                    A_Reflexo = int(input("Quantos pontos você deseja colocar?"))
                    Var_atr = A_Reflexo
                    Ler_Atributos[6] += Var_atr
                    
                    # Salvar Atributos novos no arquivo do personagem
                    pickle.dump(Ler_Atributos, Escrever_Arquivo)     

                    # Fechar arquivos para evitar alterações indesejadas            
                    Ler_Arquivo.close()
                    Escrever_Arquivo.close()
                
                # Funcao para sair ou continuar alterando atributos 
                Continuar_Alterando = input("Deseja Alterar mais algum atributo? s/n")
                
                if Continuar_Alterando == "s":
                    pass
                if Continuar_Alterando == "n":
                    Loop = False


            # Menssagem caso De algum problema na hora de atualizar os atributos
            # Estou usando o except para não dar erro e parar o bot repentinhamente
            except:
                print("Erro ao atualizar Atributos, Tente novamente")

        # Mensagem caso o nome digitado seja invalido
        except:
            print("Nome incorreto, porfavor digite denovo")