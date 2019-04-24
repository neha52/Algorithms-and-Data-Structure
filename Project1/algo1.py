# -*- coding: utf-8 -*-

array = [] #create an array.
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
  
# The main function to sort an array.
def hSort(array): 
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heap(array, n, i) 
  
    # One by one extract elements. 
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i] # swap 
        heap(array, i, 0) 
    
def MinDifference(array, n):          #function to find minimum differences.
    d1 = 10**20   #initialize d1 first minimum difference
    d2 = 10**20   #and d2 seconf minimum difference to a large value.
    pair1=0       # initialize pair1 and pair2 to zero.
    pair2=0                               
  
    #find first minimum difference.
    for i in range(n-1): 
        if array[i+1] - array[i] < d1:
            d1 = array[i+1] - array[i]
            pair1 = array[i], array[i+1]
    
    #find second minimum difference.
    for i in range(n-1): 
        a = array[i+1] - array[i]
        if (a<d2 and a>d1):  #find 'a' such that it is minimum difference but
            d2=a             #greater than first minimum difference.
            pair2 = array[i], array[i+1]
        
    #return the pairs having first and second minimum difference.
    return ("First minimum difference is:", d1 ,"between pair", pair1,"and"
            " Second minimum distance is:", d2 ,"between pair", pair2)
hSort(array)

with open('algo1.txt', 'w') as filehandle: # open file algo1.txt to print 
    for items in array:                    # sorted array with write privilege.
        filehandle.write( '%d ' % items)
filehandle.close()
    
f = open('algo1.txt', 'a')       #open same file to append output.
f.write(" : is the Sorted Array \n \n")
f.write(str(MinDifference(array, n))) #called function to print minimum differences.
f.close()
