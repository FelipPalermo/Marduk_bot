import pickle

Nome = ''
Inventario = []

def Criar_Inventario():

    # Pergunta qual o nome do personagem para comparar depos
    Nome = input("QUal o nome do seu personagem?")
    
    # Sender_ID te, que ser uma string com o ID do jogador 
    Sender_ID = "Jorge"
    # Abre e fecha o arquivo do jeito "pytonico"
    with open(f"Inventario/{Nome}.pickle", "wb") as Inv:
        Inventario.append(Sender_ID)
        pickle.dump(Inventario, Inv)


Criar_Inventario()