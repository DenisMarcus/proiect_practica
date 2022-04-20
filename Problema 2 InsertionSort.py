import math


def insertionSort(list_elemente):
    for i in range(1, len(list_elemente)):

        element_pivot = list_elemente[i]

        j = i - 1
        while j >= 0 and element_pivot < list_elemente[j]:
            list_elemente[j + 1] = list_elemente[j]
            j -= 1
        list_elemente[j + 1] = element_pivot


if __name__ == '__main__':
    list_elemente = []
    list_patrate_perfecte = []
    fisier = open("lista_elemente.in", "r")
    numar_elemente = fisier.readline()
    n = int(numar_elemente)
    linie = fisier.readline().strip().split(' ')
    for i in range(len(linie)):
        list_elemente.append(int(linie[i]))
    fisier.close()

    for k in range(len(list_elemente)):
        if math.sqrt(list_elemente[k]) == int(math.sqrt(list_elemente[k])):
            list_patrate_perfecte.append(list_elemente[k])

    insertionSort(list_patrate_perfecte)

    scriere_fisier = open("lista_finala.out", "w")
    for j in range(len(list_patrate_perfecte)):
        scriere_fisier.write(str(list_patrate_perfecte[j]))
        scriere_fisier.write(' ')
    scriere_fisier.close()
