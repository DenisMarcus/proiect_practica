def bubbleSort(list_elemente):
    n = len(list_elemente)
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(n - 1):
            if list_elemente[i] < list_elemente[i + 1]:
                list_elemente[i], list_elemente[i + 1] = list_elemente[i + 1], list_elemente[i]
                has_swapped = True


if __name__ == '__main__':
    list_elemente = []
    fisier = open("lista_elemente.in", "r")
    numar_elemente = fisier.readline()
    n = int(numar_elemente)
    linie = fisier.readline().strip().split(' ')
    for i in range(len(linie)):
        list_elemente.append(int(linie[i]))
    fisier.close()

    bubbleSort(list_elemente)

    scriere_fisier = open("lista_finala.out", "w")
    for j in range(len(list_elemente)):
        scriere_fisier.write(str(list_elemente[j]))
        scriere_fisier.write(' ')
    scriere_fisier.close()
