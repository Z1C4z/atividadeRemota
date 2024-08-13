import json

contatos = None

try:
    with open("conta.json",'r') as file:
        contatos = json.load(file)
except FileNotFoundError:
     with open("conta.json",'w') as file:
        contatos = {}
except json.JSONDecodeError:
    print("arquivo conrropido")
    contatos = {}
except Exception as e:
    print(f"erro {e}")

try:
    a = input("digite o nome")
    b = input("digite o numero")
    b = int(b)
    contatos[a] = b
    with open("conta.json",'w') as file:
        json.dump(contatos,file)
except ValueError:
    print("erro de valor")
except TypeError:
    print("erro de tipo")
except Exception as e:
    print(f"erro: {e}")