import random
import matplotlib as plt
import time
from sys import setrecursionlimit

setrecursionlimit(300000)
arr = []
mergearr = []
case1In = []
case1Me = []
case2Me = []
case2In = []
case1H = []
case2H = []
case1Q=[]
case2Q=[]
case1Mq=[]
case2Mq=[]
print('Enter the input range')
y = int(input())
for x in range(y):
    arr.append(random.randint(1, 50000))
insertarr = arr[:]
mergearr = arr[:]
heapsort = arr[:]
quicksort = arr[:]
median = arr[:]
print('*****************************************INSERTION SORT*******************************************************')


def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


start = time.time()
print('Array before sorting')
for i in range(len(arr)):
    print("%d" % arr[i], ' ', end='')
print(insertion(arr))
print('Array after Insertion sorting')
for i in range(len(arr)):
    print("%d" % arr[i], ' ', end='')
print("\n")
end = time.time()
elapse = end - start
case1In = arr
start1 = time.time()
print('Case 1(Insertion):Running sorting algorithm on the sorted array')
for i in range(len(case1In)):
    print("%d" % case1In[i], ' ', end='')
print(insertion(case1In))
print("\n")
print('Result of sorting on Sorted array')
for i in range(len(case1In)):
    print("%d" % case1In[i], ' ', end='')
end1 = time.time()
elapse1 = end1 - start1
case2In = arr


# start3=time.time()
def Reverse(case2In):
    case2In.reverse()
    return case2In


print("\n")
print('Case 2(Insertion): Running sorting algorithm for reversed input array')
print(Reverse(case2In))
start3 = time.time()
print(insertion(case2In))
for i in range(len(case2In)):
    case2In[i]
    print("%d" % case2In[i], ' ', end='')
end3 = time.time()
elapse3 = end3 - start3
print("\n")
print("Time taken for insertion sorting on an array", elapse * 100)
print("Time taken for insertion sorting on an sorted array", elapse1 * 100)
print("Time taken for insertion sorting on an reversely sorted array", elapse3 * 100)
print(
    "***************************************************MERGE SORT*****************************************************")
startMe = time.time()


def mergeSort(mergearr):
    if len(mergearr) > 1:
        mid = len(mergearr) // 2
        L = mergearr[:mid]
        R = mergearr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                mergearr[k] = L[i]
                i += 1
            else:
                mergearr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            mergearr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            mergearr[k] = R[j]
            j += 1
            k += 1


def printList(mergearr):
    for i in range(len(mergearr)):
        print("%d" % mergearr[i], ' ', end='')
    print()


printList(mergearr)
mergeSort(mergearr)
print("\n")
print("after sorting")
printList(mergearr)
endMe = time.time()
elapseMe = endMe - startMe
startMe1 = time.time()
case1Mer = mergearr
print("\n")
print('Case 1(Merge) :Running sorting algorithm on the below sorted array')
for i in range(len(case1Mer)):
    print("%d" % case1Mer[i], ' ', end='')
print(mergeSort(case1Mer))
print("\n")
print('Result of sorting on Sorted array')
for i in range(len(case1Mer)):
    print("%d" % case1Mer[i], ' ', end='')
endMe1 = time.time()
elapseMe1 = endMe1 - startMe1
case2Mer = mergearr
startMe3 = time.time()


def Reverse(case2Mer):
    case2Mer.reverse()
    return case2Mer


print("\n")
print('Case 2(Merge): Running sorting algorithm for reversed input array')
print(Reverse(case2Mer))
print(mergeSort(case2Mer))
for i in range(len(case2Mer)):
    case2Mer[i]
    print("%d" % case2Mer[i], ' ', end='')
print("\n")
endMe3 = time.time()
elapseMe3 = endMe3 - startMe3
print("Time taken for Merge sorting on an array", elapseMe * 100)
print("Time taken for Merge sorting on an sorted array", elapseMe1 * 100)
print("Time taken for Merge sorting on an reversely sorted array", elapseMe3 * 100)

print('*********************************HEAP SORT********************************************************')

def heapify(heapsort, n, i):
    smallest = i
    l = 2 * i
    r = 2 * i + 1


    if l < n and heapsort[i] < heapsort[l]:
        smallest = l


    if r < n and heapsort[smallest] < heapsort[r]:
        smallest = r

    if smallest != i:
        heapsort[i],heapsort[smallest] = heapsort[smallest],heapsort[i]


        heapify(heapsort, n, smallest)


def heapSort(heapsort):
    n = len(heapsort)


    for i in range(n, -1, -1):
        heapify(heapsort, n, i)


    for i in range(n-1, 0, -1):
        heapsort[i], heapsort[0] = heapsort[0], heapsort[i]
        heapify(heapsort, i, 0)

n = len(heapsort)
print("\n")
print('Array before sorting')
for i in range(n):
    print("%d" %heapsort[i], ' ', end='')
startH=time.time()
print("\n")
print("Array after sorting")
heapSort(heapsort)
for i in range(n):
    print("%d" %heapsort[i], ' ', end='')
endH=time.time()
elapseH=endH-startH
startH1=time.time()
case1H=heapsort
print("\n")
print('Case 1(Heap) :Running sorting algorithm for sorted input array')
for i in range(len(case1H)):
    print ("%d" %case1H[i],' ',end="")
print('Result of sortin on Sorted array')
heapSort(case1H)
for i in range(n):
    print("%d" %heapsort[i], ' ', end='')
endH1=time.time()
elapseH1=endH1-startH1
start2H=time.time()
case2H=heapsort
def Reverse(case2H):
    case2H.reverse()
    return case2H
print("\n")
print('Case 2(Heap): Running sorting alogrithm for reversed input array')
print(Reverse(case2H))
heapSort(case2H)
for i in range(n):
    print("%d" %case2H[i], ' ', end='')
end2H=time.time()
elapse2H=end2H-start2H
print("\n")
print('Time elapse for heap sort')
print("Time taken for Heap sorting on an array", elapseH * 100)
print("Time taken for Heap sorting on an sorted array", elapseH1 * 100)
print("Time taken for Heap sorting on an reversely sorted array", elapse2H * 100)

print('*******************************IN PLACE QUICKSORT*******************************************')


def partition(quicksort, low, high):
    i = (low - 1)
    pivot = quicksort[high]
    for j in range(low, high):
        if quicksort[j] <= pivot:
            i = i + 1
            quicksort[i], quicksort[j] = quicksort[j], quicksort[i]
    quicksort[i + 1], quicksort[high] = quicksort[high], quicksort[i + 1]
    return (i + 1)


def quickSort(quicksort, low, high):
    if low < high:
        pi = partition(quicksort, low, high)
        quickSort(quicksort, low, pi - 1)
        quickSort(quicksort, pi + 1, high)


startQ = time.time()
print("array before sorting")
for i in range(n):
    print("%d" % quicksort[i], ' ', end='')
n = len(quicksort)
quickSort(quicksort, 0, n - 1)
print("\n")
print("Sorted array is:")
for i in range(n):
    print("%d" % quicksort[i], ' ', end=''),
endQ = time.time()
elapseQ = endQ - startQ
start1Q = time.time()
case1Q = quicksort
print("\n")
print('Case 1(In-place Quick): Running sorting algorithm for sorted input array')
for i in range(len(case1Q)):
    print("%d" % case1Q[i], ' ', end='')
print('Result of sorting on Sorted array')
quickSort(case1Q, 0, n - 1)
for i in range(n):
    print("%d" % case1Q[i], ' ', end=''),
end1Q = time.time()
elapse1Q = end1Q - start1Q
start2Q = time.time()
case2Q = quicksort


def Reverse(case2Q):
    case2Q.reverse()
    return case2Q


print("\n")
print('Case 2(In-place Quick): Running sorting algorithm for reverse input array')
print(Reverse(case2Q))
quickSort(case2Q, 0, n - 1)
for i in range(n):
    print("%d" % case2Q[i], ' ', end=''),
end2Q = time.time()
elapse2Q = end2Q - start2Q
print("\n")
print("Time taken for Quick sorting on an array", elapseQ * 100)
print("Time taken for Quick sorting on an sorted array", elapse1Q * 100)
print("Time taken for Quick sorting on an reversely sorted array", elapse2Q * 100)

print("********************MEDIAN OF THREE QUICK SORT************************************")


def quickSortM(L, ascending=False):
    quicksorthelp(L, 0, len(L), ascending)


def insertionM(L, low, high):
    for i in range(low, high):
        key = L[i]
        j = i - 1
        while j >= 0 and key < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key


def quicksorthelp(L, low, high, ascending=False):
    result = 0
    if (low + 10 <= high):
        insertionM(L, low, high)
    else:
        pivot_location, result = Partition(L, low, high, ascending)
        result += quicksorthelp(L, low, pivot_location, ascending)
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result


def median_of_three(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low


def Partition(L, low, high, ascending=False):
    result = 0
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low]
    return i - 1, result


startMq = time.time()
for i in range(n):
    print("%d" % median[i], ' ', end='')
quickSortM(median, True)
print("\n")
print('Array after sorting:')
for i in range(n):
    print("%d" % median[i], ' ', end='')
endMq = time.time()
elapseMq = endMq - startMq
start1Mq = time.time()
case1Mq = median
print("\n")
print('Case 1 (Modified Quick) :Running sorting algorithm for sorted input array')
for i in range(len(case1Mq)):
    print("%d" % case1Mq[i], ' ', end='')
print("\n")
print('Result of sorting on Sorted array')
quickSortM(case1Mq, True)
for i in range(n):
    print("%d" % case1Mq[i], ' ', end=''),
end1Mq = time.time()
elapse1Mq = end1Mq - start1Mq
startMq2 = time.time()
case2Mq = median


def Reverse(case2Mq):
    case2Mq.reverse()
    return case2Mq


print("\n")
print('Case 2 (Modified Quick): Running sorting algorithm for reverse input array')
print(Reverse(case2Mq))
quickSortM(case2Mq, True)
for i in range(n):
    print("%d" % case2Mq[i], ' ', end=''),
end2Mq = time.time()
elapse2Mq = end2Mq - startMq2
print("\n")
print("Time taken for Modified Quick sorting on an array", elapseMq * 100)
print("Time taken for Modified Quick sorting on an sorted array", elapse1Mq * 100)
print("Time taken for Modified Quick sorting on an reversely sorted array", elapse2Mq * 100)
print("\n")

print('Time complexity')
print("Insertion")
print(elapse * 100)
print(elapse1 * 100)
print(elapse3 * 100)

print('\n')
print("Merge")
print(elapseMe * 100)
print(elapseMe1 * 100)
print(elapseMe3 * 100)

print('\n')
print("Heap")
print(elapseH * 100)
print(elapseH1 * 100)
print(elapse2H * 100)

print('\n')
print("In-place Quick")
print(elapseQ * 100)
print(elapse1Q * 100)
print(elapse2Q * 100)

print('\n')
print("Modified Quick")
print(elapseMq * 100)
print(elapse1Mq * 100)
print(elapse2Mq * 100)
