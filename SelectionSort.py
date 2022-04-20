import time


def selectionSort(list_elemente):
    for i in range(len(list_elemente)):
        min_index = i

        for j in range(i + 1, len(list_elemente)):
            if list_elemente[j] < list_elemente[min_index]:
                min_index = j
        (list_elemente[i], list_elemente[min_index]) = (list_elemente[min_index], list_elemente[i])


if __name__ == '__main__':
    list_elemente = []
    fisier = open("lista_elemente.in", "r")
    linie = fisier.readline().strip().split(' ')
    for i in range(len(linie)):
        list_elemente.append(linie[i])
    fisier.close()

    start_time = time.time()
    selectionSort(list_elemente)
    print("Timpul de procesare este de: %.3f seconds " % (time.time() - start_time))

    scriere_fisier = open("lista_finala.out", "w")
    for j in range(len(list_elemente)):
        scriere_fisier.write(str(list_elemente[j]))
        scriere_fisier.write(' ')
    scriere_fisier.close()
