def intersectionOfArrays(arr1, arr2):
    SetOfarray = set(arr1)
    return SetOfarray.intersection(arr2)

def unionOfArrays(arr1, arr2):
    SetOfarray = set(arr1)
    return SetOfarray.union(arr2)

array1 = [1,2,3,5,6,56,2367,12]
array2 = [6,3,8,9,2,45,34,23]
array3 = [[1, 2], [2, 5], [5, 6], [3, 7], [4,5], [8,4]]
#Intersection of 2 arrays
print("Intersection of two arrays "+str(array1)+" and "+str(array2)+" is "+str(intersectionOfArrays(array1, array2)))
#Union of 2 arrays
print("Union of two arrays "+str(array1)+" and "+str(array2)+" is "+str(unionOfArrays(array1, array2)))
#Overlapping arrays
for index1 in range(len(array3)):
    for index2 in range(index1+1, len(array3)):
        #Code for overlapping timeslots
        if intersectionOfArrays(range(array3[index1][0], array3[index1][1]+1), range(array3[index2][0], array3[index2][1]+1)):
            print("Array overlapping with "+str(array3[index1])+" is "+ str(array3[index2]))
        #Code to cover timeslots around 12 O'clock
        elif array3[index2][0] >= array3[index2][1]:
              tempList= [*range(array3[index2][0], 13), *range(1,array3[index2][1]+1)]
              if intersectionOfArrays(range(array3[index1][0], array3[index1][1]+1),tempList):
                  print("Array overlapping with "+str(array3[index1])+" is "+ str(array3[index2]))