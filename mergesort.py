def juntarLista(arr1, arr2):
    fullList = []
    fullList.extend(arr1)
    fullList.extend(arr2)
    return fullList


def margesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        e = arr[:mid]
        d = arr[mid:]
        
        margesort(e)
        margesort(d)


        i = j = k = 0
        while i < len(e) and j < len(d):
            if e[i] <= d[j]:
                arr[k] = e[i]
                i += 1
            else:
                arr[k] = d[j]
                j += 1
            k += 1

        while i < len(e):
            arr[k] = e[i]
            i += 1
            k += 1

        while j < len(d):
            arr[k] = d[j]
            j += 1
            k += 1
    return arr

    
l1 = input().split(',')
l2 = input().split(',')

arr = juntarLista(l1,l2)
resultado = margesort(arr)
localFilme = len(resultado)//2
localFilmeadd = localFilme + 1 
print(f'Os amigos decidiram assistir a {resultado[localFilme]} que estava na posição {localFilmeadd} da lista.')
