#Name: Keyshawn Forde               ID: 100864963
#Assignment 2
#Function imported for sound effects
import time
import winsound

#Merge Sort function
def merge_sort(productarray_ID, depth=0):
    if len(productarray_ID) > 1:
        mid = len(productarray_ID) // 2
        Left = productarray_ID[:mid]
        Right = productarray_ID[mid:]

        print("Dividing the array:", productarray_ID)
        print("Left half:", Left)
        print("Right half:", Right)

        #sorts the left side
        merge_sort(Left)
        #sorts the right side
        merge_sort(Right)

        # Two iterators for traversing the two halves
        i = j = k = 0

        # Merge the two halves
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                productarray_ID[k] = Left[i]
                i += 1
            else:
                productarray_ID[k] = Right[j]
                j += 1
                #sound effect for sort swap 
                winsound.Beep(1000, 50)
            k += 1

        #For remaining values
        while i < len(Left):
            productarray_ID[k] = Left[i]
            i += 1
            k += 1
           

        while j < len(Right):
            productarray_ID[k] = Right[j]
            j += 1
            k += 1

            #prints the merged arrays
            print("Merged Array:", productarray_ID)

#Initial array
productarray_ID = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
#prints the orginal array
print("The Original Array:", productarray_ID)
merge_sort(productarray_ID)
#prints the sorted array
print("The Sorted Array:", productarray_ID)