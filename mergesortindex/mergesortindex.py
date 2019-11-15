def mergeSort(alist, leftdex, rightdex):

    print("Splitting from " + str(leftdex) + " to " + str(rightdex))

    print(alist[leftdex:rightdex+1])

    if rightdex - leftdex > 0:

        mid = ((rightdex + leftdex) // 2)

        print(mid)
        print(leftdex)
        print(rightdex)

        mergeSort(alist, leftdex, mid)
        mergeSort(alist, mid + 1, rightdex)

        i = 0
        j = 0
        k = 0
        print(mid)
        print(leftdex)
        print(rightdex)

        while i < (mid - leftdex + 1) and j < (rightdex - mid):
            if alist[leftdex + i] <= alist[mid + j + 1]:
                alist[leftdex + k] = alist[leftdex + i]
                i = i + 1
            else:
                alist[leftdex + k], alist[mid + j + 1] = alist[mid + j + 1], alist[leftdex + k]
                j = j + 1
            k = k + 1

        while i < (mid - leftdex):
            alist[k] = alist[leftdex + i]
            i = i + 1
            k = k + 1

        while j < (rightdex - mid):
            alist[k] = alist[mid + j]
            j = j + 1
            k = k + 1
    print("Merging from " + str(leftdex) + " to " + str(rightdex))
    print(alist[leftdex:rightdex+1])

alist = [54,26,93,17]
mergeSort(alist, 0, len(alist)-1)
print(alist)

