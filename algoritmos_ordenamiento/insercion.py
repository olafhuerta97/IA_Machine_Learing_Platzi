import random

def ordenamiento_por_insercion(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        pos = i

        while pos > 0and lista[pos - 1] > valor_actual:
            lista[pos], lista[pos - 1] = lista[pos - 1], lista[pos]

            pos -= 1

        lista[pos] = valor_actual

    return lista


if __name__ == '__main__':

	tamano_lista = int(input('Digite el tamaño de la lista: '))

	lista = [random.randint(0,100) for i in range(tamano_lista)]

print(ordenamiento_por_insercion(lista))
