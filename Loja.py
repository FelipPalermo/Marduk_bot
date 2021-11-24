import time
import random

def Timer_RNG():
    # 20 minutos = 1200 segundos 
    for i in range(10):
        time.sleep(1)


# gera 26 numeros aleatorios para basearmos a probabilidade dos itens da loja 
porcentagem = list(range(26))

# Itens separados por categoria
Armas_Comuns = ["pistola .38", "Munição leve", "adaga", "granada de fragmentação"]
Armas_Raras = ["Canhao laser", "Granada de plasma", "Espada jedi", "Drone de combate inteligente"]



while True:
    
    # escolhe numeros aleatorios para serem o que vamos receber na loja 
    chance = random.choice(porcentagem)

    if chance > 5:
        AC_I1 = print(random.choice(Armas_Comuns))

    if chance > 20:
        AR_I1 = print(random.choice(Armas_Raras))

    if chance > 5:
        AC_I2 = print(random.choice(Armas_Comuns))

    if chance > 20:
        AR_I2 = print(random.choice(Armas_Raras))

    if chance > 5:
        AC_I3 = print(random.choice(Armas_Comuns))

    if chance > 20:
        AR_I3 = print(random.choice(Armas_Raras))

    if chance > 5:
        AC_I4 = print(random.choice(Armas_Comuns))

    Timer_RNG()