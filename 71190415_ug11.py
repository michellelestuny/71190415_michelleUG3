def mergesort(list1):
    print('Memecah List', list1)
    n = len(list1)
    if n < 2:
        return list1
    else:
        mid=n//2
        left=list1[:mid]
        right=list1[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list1[k]=left[i]
                i=i+1
            else:
                list1[k]=right[j]
                j=j+1
            k=k+1
        while i < len (left):
            list1[k]=left[i]
            i=i+1
            k=k+1
        while j < len (right):
            list1[k]=right[j]
            j=j+1
            k=k+1
    print('Menggabungkan List', list1)

def mergesort(list2):
    print('Memecah List', list2)
    n = len(list2)
    if n < 2:
        return list2
    else:
        mid=n//2
        left=list2[:mid]
        right=list2[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list2[k]=left[i]
                i=i+1
            else:
                list2[k]=right[j]
                j=j+1
            k=k+1
        while i < len (left):
            list2[k]=left[i]
            i=i+1
            k=k+1
        while j < len (right):
            list2[k]=right[j]
            j=j+1
            k=k+1
    print('Menggabungkan List', list2)

def mergesort(list3):
    print('Memecah List', list3)
    n = len(list3)
    if n < 2:
        return list3
    else:
        mid=n//2
        left=list3[:mid]
        right=list3[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list3[k]=left[i]
                i=i+1
            else:
                list3[k]=right[j]
                j=j+1
            k=k+1
        while i < len (left):
            list3[k]=left[i]
            i=i+1
            k=k+1
        while j < len (right):
            list3[k]=right[j]
            j=j+1
            k=k+1
    print('Menggabungkan List', list3)
    
list1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
list2 = [20,21,22,23,24,25,26,27]
list3 = [30,29,31,33,19,20,31,21,59]
print(mergesort(list1))
print(mergesort(list1))
print(mergesort(list1))