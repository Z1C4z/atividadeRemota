try:
    a = input("digite a temperatura em celcius: ")
    if "," in a:
        a = a.replace(',', '.')
    a = float(a)
    if a < 0 and a > 1000:
        raise ValueError("temperatura invalida")
    b = (a * 9/5) + 32
    print(b)
except TypeError:
    print("digite um numero")
