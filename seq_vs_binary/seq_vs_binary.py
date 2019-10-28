rec_count = 0

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    opcount = 0

    while first<=last and not found:
        midpoint = (first + last)//2
        opcount += 1
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found, opcount

def binarySearchRec(alist, item):
    global rec_count
    rec_count += 1
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binarySearchRec(alist[:midpoint], item)
          else:
            return binarySearchRec(alist[midpoint+1:], item)
def sequentialSearch(alist, item):
    pos = 0
    found = False
    opcount = 0
    while pos < len(alist) and not found:
        opcount += 1
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found, opcount

