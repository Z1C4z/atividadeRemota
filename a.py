try:
    ano = input("Insira seu ano de nascimento")
    if ano < 2024 and ano > 1900:
        print("data valida")
    else:
        print("data invalida")
except FloatingPointError:
    print("Insira um valor inteiro")
except:
    print("digite um numero")