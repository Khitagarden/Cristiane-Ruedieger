#Vamos criar um menu

#restaurante

print("""Menu principal:

    [ 1 Frutos do mar
        [(1)Lagosta,
         (2)Duzia de Ostras,
         (3)Casquina de Siri]]


    [ 2 Massas
        [(1)Macarrão a carbonara,
         (2)Lasanha Bolonhesa,
         (3)Pizza Margherita,
         (4)Nhoque a Bolonhesa,
         (5)Capelete a bolonhesa]]

    [ 3 Carnes
        [(1)Bife acebolado,
         (2)Bife a Parmegiana,
         (3)Bife a Role,
         (4)Peito a Milanesa]]

    [ 4 Acompanhamentos
        [(1) Arroz a Grega,
         (2) Arroz Branco com feijão,
         (3)Batata frita,
         (4)Polenta Frita,
         (5)Salada]]
""")

Menu_principal = int(input("Escolha um menu: "))

if Menu_principal == 1:
    print("""Frutos do mar:
         (1)Lagosta
         (2)Duzia de Ostras
         (3)Casquina de Siri
    """)

    Frutos_do_mar = int(input("Escolha seu prato: "))

    if Frutos_do_mar == (1):
        print("Voce escolheu lagosta")
    elif Frutos_do_mar == (2):
        print("Voce escolheu uma Duzia de Ostras")
    elif Frutos_do_mar == (3):
        print("Voce escolheu Casquinha de Siri")

if Menu_principal == 2:
    print("""Massas:
        (1)Macarrão a carbonara,
        (2)Lasanha Bolonhesa,
        (3)Pizza Margherita,
        (4)Nhoque a Bolonhesa,
        (5)Capelete a bolonhesa
    """)

    Massas = int(input("Escolha seu prato: "))

    if Massas == (1):
        print("Voce escolheu Macarrão a carbonara")
    elif Massas == (2):
        print("Voce escolheu Lasanha Bolonhesa")
    elif Massas == (3):
        print("Voce escolheu Pizza Margherita")
    elif Massas == (4):
        print("Voce escolheu Nhoque a Bolonhesa")
    elif Massas == (5):
        print("Voce escolheu Cappelete a Bolonhesa")

if Menu_principal == 3:
    print("""Carnes:
        (1)Bife acebolado,
        (2)Bife a Parmegiana,
        (3)Bife a Role,
        (4)Peito a Milanesa
    """)

    Carnes = int(input("Escolha seu prato: "))

    if Carnes == (1):
        print("Voce escolheu Bife acebolado")
    elif Carnes == (2):
        print("Voce escolheu Bife a Parmegiana")
    elif Carnes == (3):
        print("Voce escolheu Bife a Role")
    elif Carnes == (4):
        print("Voce escolheu Peito a Milanesa")

if Menu_principal == 4:
    print("""Acompanhamentos:
        (1)Arroz a Grega,
        (2)Arroz Branco com feijão,
        (3)Batata frita,
        (4)Polenta Frita,
        (5)Salada
    """)

    Acompanhamentos = int(input("Escolha seu prato: "))

    if Acompanhamentos == (1):
        print("Voce escolheu Arroz a Grega")
    elif Acompanhamentos == (2):
        print("Voce escolheu Arroz Branco com feijão")
    elif Acompanhamentos == (3):
        print("Voce escolheu Batata frita")
    elif Acompanhamentos == (4):
        print("Voce escolheu Polenta Frita")
    elif Acompanhamentos == (5):
        print("Voce escolheu Salada")
else:
    print("Voce precisa escolher um Menu e um prato")

arq = open('Atividade3.txt', 'a')
for x in Menu_principal:
    arq.write(x + ',')
arq.write('\n')

arq.close()