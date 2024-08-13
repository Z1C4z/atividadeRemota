file = input("escreva o nome do arquivo com sua tipagem: ")
try:
    a = open(file,'r')
    print(a)
except FileNotFoundError:
    print("arquivo nao encontradio")
except PermissionError:
    print("permisao negada")
except UnicodeDecodeError:
    print("erro ao codificao")
except Exception as e:
    print(f"erro inesperado {e}")