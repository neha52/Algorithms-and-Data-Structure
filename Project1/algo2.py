# -*- coding: utf-8 -*-
array = [] #create an array.
x = float (input ("Enter the value of X: "))
n = int(input("Enter the number of elements you want:"))
if(n<2):            #check if array more than two elements.
    print ("Enter valid number of elements!")
else:
    print ('Enter numbers in array: ') #take input from user.
    for i in range(int(n)):
        no = input()
        array.append(int(no))
    
def heap(array, n, i): 
    largest = i                    # Initialize largest as root. 
    l = 2 * i + 1 
    r = 2 * i + 2  
                 
    # See if left child of root exists and is greater than root. 
    if l < n and array[i] < array[l]: 
        largest = l 
  
    # See if right child of root exists and is greater than root. 
    if r < n and array[largest] < array[r]: 
        largest = r 
   
    if largest != i:                # If required, change root.
        array[i],array[largest] = array[largest],array[i] 
        # swap root with element greater than root.
   
        heap(array, n, largest)       # Heapify the root.
  
# The main function to sort an array 
def hSort(array): 
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heap(array, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i] # swap 
        heap(array, i, 0)
        


try:
    hSort(array)    #sort the array using heapsort.
    def median(array):      #compute median of array.
        mid = len(array)//2     #if length=odd, compute middle element.
        if len(array) % 2: # To check if the length of array is odd or even.
            return array[mid]
        else:
            med = (array[mid] + array[mid-1]) / 2 #if length=even, compute mean of middle elements.
            return med
    
    with open('algo2.txt', 'w') as filehandle: # open file algo1.txt to print
        for items in array:                # sorted array with write privilege.
            filehandle.write( '%d ' % items)
    filehandle.close()
    
    med = median(array)
    #function to compute longest sub-array with median greater than equal to X.
    def LongSubArray(array, med): 
        if x > med:
            for i in range (int(n)):
                if i>=n or x <= med: #conditions based on desired output.
                    break
                array.remove(array[0])
                med = median(array) #median of longest subarray.
        return ("Longest Subarray is :" ,array ,"of length" ,len(array))
        
    f = open('algo2.txt', 'a')      #open same file to append output.
    f.write(" : is the Sorted Array \n \n")
    f.write(str(LongSubArray(array, med))) #called function to print longest subarray.
    f.close()
    
except ValueError as err: #errors
    print("Something went Wrong",err)
except:
    print("Something went Wrong")
