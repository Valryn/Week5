def mergeSort(alist, leftdex = 0, rightdex = None):
    # Allow for missing parameters
    if rightdex is None:
        rightdex = len(alist) - 1

    print("Splitting from " + str(leftdex) + " to " + str(rightdex))
    print(alist[leftdex:rightdex + 1])

    # Check for base case, a list size of at least 1.
    list_size = rightdex - leftdex
    if list_size > 0:

        mid = ((rightdex + leftdex) // 2)

        print(mid)
        print(leftdex)
        print(rightdex)

        # Recursively mergeSort two halves of the list
        mergeSort(alist, leftdex, mid)
        mergeSort(alist, mid + 1, rightdex)

        # Establish helpers
        left_size = mid - leftdex + 1
        right_size = rightdex - mid
        left_start = leftdex
        right_start = mid + 1

        i = 0
        j = 0
        temp = []
        # Merge left and right sublists by adding the smallest values to a temp list in order
        while i < left_size and j < right_size:
            if alist[left_start + i] <= alist[right_start + j]:
                temp.append(alist[left_start + i])
                i += 1
            else:
                temp.append(alist[right_start + j])
                j += 1

        # Add the remaining values to the temp list
        while i < left_size:
            temp.append(alist[left_start + i])
            i = i + 1

        while j < right_size:
            temp.append(alist[right_start + j])
            j = j + 1

        print("Copying sublist to mainlist.....")
        print("Mainlist: " + str(alist))
        print("Sublist = " + str(temp))

        z = 0
        # Overwrite the main list with the temp sublist
        for num in temp:
            alist[left_start + z] = num
            z += 1

        print("New list: " + str(alist))

    print("Merging from " + str(leftdex) + " to " + str(rightdex))
    print(alist[leftdex:rightdex + 1])


mylist = [34, 15, 53, 32, 12, 64, 67, 21]
mergeSort(mylist)
print("Result: " + str(mylist))
