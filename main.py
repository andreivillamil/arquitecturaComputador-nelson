def mostrar_no_es_primo(num_in):
    print(f"El número", num_in, "no es primo")
    return


def mostrar_es_primo(num_in):
    print(f"El número", num_in, "es primo")
    return


def validar_primo():
    num_in = int(input("Ingrese un número positivo: "))
    if num_in == 0:
        mostrar_no_es_primo(num_in)
        return
    if num_in == 1:
        mostrar_no_es_primo(num_in)
        return
    if num_in == 2:
        mostrar_es_primo(num_in)
        return
    if num_in % 2 == 0:
        mostrar_no_es_primo(num_in)
        return
    mitad = int(num_in/2)
    for i in range(3, mitad):
        if num_in % i == 0:
            print(f"El número divisor es:", i)
            mostrar_no_es_primo(num_in)
            return
    mostrar_es_primo(num_in)
    return


if __name__ == '__main__':
    validar_primo()

