import time

def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i < pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

def bublesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr

def getarray(filename):
    with open(filename,"r") as f:
        file_content = f.read()
    return file_content

def main():
    filename ="wiki.txt"
    array = getarray(filename)
    ml = list(array)
    qst = time.time()
    print("Quick sorting: ", quicksort(ml))
    print("Quick sorts duration: ", time.time() - qst )
    bst = time.time()
    print("Bubble sorting: ", bublesort(ml))
    print("Bubble sortig duration: ", time.time() - bst )

main()
