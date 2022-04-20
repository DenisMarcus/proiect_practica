n = int(input())
k = int(input())
lista = list(map(int, input().strip().split()))[:n]
# impartim lista initiala in cdoua liste

crescator = []  # in prima vom adauga primele k elemente
for c_i in range(k):
    crescator.append(lista[c_i])
# print("Lista cu primele k =", k, "numere este:", crescator)

descrescator = []  # in a doua restul, adica n-k elemente
for d_i in range(k, n):
    descrescator.append(lista[d_i])
# print("Lista cu elementele ramase este:", descrescator)

# la ordonarea celor doua liste am folosit metoda SelectSort

# pe prima o vom ordona crescator
for i in range(k):
    min_index = i

    for j in range(i + 1, k):
        if crescator[j] < crescator[min_index]:
            min_index = j
    (crescator[i], crescator[min_index]) = (crescator[min_index], crescator[i])
# print("Lista crescatoare:", crescator)

# pe a doua o vom ordona descrescator
for i in range(n - k):
    max_index = i

    for j in range(i + 1, n - k):
        if descrescator[j] > descrescator[max_index]:
            max_index = j
    (descrescator[i], descrescator[max_index]) = (descrescator[max_index], descrescator[i])
# print("Lista descrescatoare este:", descrescator)

lista_noua = crescator + descrescator  # am creat noua lista conform problemei
print("Lista finala este:", lista_noua)
