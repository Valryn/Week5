def mergeSort(alist, leftdex, rightdex):

    print("Splitting from " + str(leftdex) + " to " + str(rightdex))

    if rightdex - leftdex > 1:
        mid = (rightdex + leftdex) // 2
        mergeSort(alist, leftdex, mid)
        mergeSort(alist, mid + 1, rightdex)

        i = 0
        j = 0
        k = 0

        while i < (mid - leftdex) and j < (rightdex - mid):
            if alist[leftdex + i] <= alist[mid + j]:
                alist[leftdex + k] = alist[leftdex + i]
                i = i + 1
            else:
                alist[leftdex + k] = alist[mid + j]
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

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist, 0, len(alist))
print(alist)