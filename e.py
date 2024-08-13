lista=[]
try:
    for i in range(6):
        a = input("Digite um numero")
        lista.append(float(a))
        m = sum(lista) / len(lista)

        ord = sorted(lista)
        meio = len(ord) // 2
        if len(ord) % 2 == 0:
            me = (ord[meio - 1] + ord[meio]) / 2
        else:
            me = ord[meio]

        aux = {}
        for n in lista:
            if n in aux:
                aux[n] += 1
            else:
                aux[n] = 1
        mo = max(aux, key=aux.get)
        print(f"media ={m}/nmediano = {me}/nmoda = {mo}")
except ValueError:
    print("erro de valor")
except TypeError:
    print("erro de tipo")