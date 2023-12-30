def smallest(a,low,high):
    indexMin = low
    for i in range (low+1 , high+1):
        if a[i]<a[indexMin]:
            indexMin = i
    return indexMin
def swap(a,i,j):
    t = a[i]
    a[i] = a[j]
    a[j] = t
    return a

a=[3,5,1,4,8,4,0]
l=len(a)
print('Unsorted=',a)
for i in range(0,l):
        j=smallest(a,i,l-1)
        swap(a,i,j)
print('Sorted=',a)


