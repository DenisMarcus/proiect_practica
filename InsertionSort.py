import time

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
    fisier = open("lista_elemente.in", "r")
    linie = fisier.readline().strip().split(' ')
    for i in range(len(linie)):
        list_elemente.append(linie[i])
    fisier.close()

    start_time = time.time()
    insertionSort(list_elemente)
    print("Timpul de procesare este de: %.3f seconds " % (time.time() - start_time))

    scriere_fisier = open("lista_finala.out", "w")
    for j in range(len(list_elemente)):
        scriere_fisier.write(str(list_elemente[j]))
        scriere_fisier.write(' ')
    scriere_fisier.close()
        
