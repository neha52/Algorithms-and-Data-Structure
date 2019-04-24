# -*- coding: utf-8 -*-
# Python code uses AVL Tree as Data Structure 
# AVL tree class which supports Insertion, 
# deletion operations  
from collections import Counter
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
        

class AVLTree(object): #class AVLTree for performing required actions
    
    def Left_Rotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Performs rotation 
        y.left = z 
        z.right = T2 
  
        # Updates heights 
        z.height = 1 + max(self.Get_Height(z.left),  
                         self.Get_Height(z.right)) 
        y.height = 1 + max(self.Get_Height(y.left),  
                         self.Get_Height(y.right)) 
  
        # Returns the new root 
        return y 
    
    def Right_Rotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Performs rotation 
        y.right = z 
        z.left = T3 
  
        # Updates heights 
        z.height = 1 + max(self.Get_Height(z.left), 
                          self.Get_Height(z.right)) 
        y.height = 1 + max(self.Get_Height(y.left), 
                          self.Get_Height(y.right)) 
  
        # Returns the new root 
        return y 
  
    def Get_Height(self, root): #returns height of the tree
        if not root: 
            return 0
  
        return root.height 
  
    def Get_Balance(self, root): #checks for balance of the tree
        if not root: 
            return 0
        #checks the diffrence of height in left and right subtree
        return self.Get_Height(root.left) - self.Get_Height(root.right) 
  
    #returns smallest element of the tree which is leftmost leaf node 
    #of left subtree
    def Get_MinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.Get_MinValueNode(root.left) 
  
    def Preorder(self, root):#Preorder displays as : root,left child,right child
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") #displays root
        self.Preorder(root.left) 
        self.Preorder(root.right) 
  
    # Recursive function to Insert a node with 
    # given element from subtree with given root. 
    # Returns root of the modified subtree. 
    def Insert(self, root, key): 
          
        # Performs normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.Insert(root.left, key) 
        else: 
            root.right = self.Insert(root.right, key) 
  
        # Updates the height of the ancestor node 
        root.height = 1 + max(self.Get_Height(root.left), 
                          self.Get_Height(root.right)) 
  
        # Gets the balance factor 
        balance = self.Get_Balance(root) 
  
        # If the node is unbalanced, then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.Right_Rotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.Left_Rotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.Left_Rotate(root.left) 
            return self.Right_Rotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.Right_Rotate(root.right) 
            return self.Left_Rotate(root) 
  
        return root 
    
    
     # Recursive function to Delete a node with 
    # given element from subtree with given root. 
    # Returns root of the modified subtree. 
    def Delete(self, root, key): 
  
        # Performs standard BST Delete 
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.Delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.Delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.Get_MinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.Delete(root.right, 
                                      temp.val) 
  
        # If the tree has only one node then, return it 
        if root is None: 
            return root 
  
        # Updates the height of the ancestor node 
        root.height = 1 + max(self.Get_Height(root.left), 
                            self.Get_Height(root.right)) 
  
        # Gets the balance factor 
        balance = self.Get_Balance(root) 
  
        # If the node is unbalanced, then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.Get_Balance(root.left) >= 0: 
            return self.Right_Rotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.Get_Balance(root.right) <= 0: 
            return self.Left_Rotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.Get_Balance(root.left) < 0: 
            root.left = self.Left_Rotate(root.left) 
            return self.Right_Rotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.Get_Balance(root.right) > 0: 
            root.right = self.Right_Rotate(root.right) 
            return self.Left_Rotate(root) 
  
        return root  
    
      
    # function to check whether both srings are anagrams or not
    def Check_Anagram(self, str1, str2): 
  
    # Create two count arrays for 2 elements and initialize all values as 0 
        count1 = [0] * NO_OF_CHARS 
        count2 = [0] * NO_OF_CHARS 
  
    # For each character in input strings, increment count 
    # in the corresponding count array 
        for i in str1: 
            count1[ord(i)]+=1
  
        for i in str2: 
            count2[ord(i)]+=1
  
    # If both strings are of different length, return 0 i.e not anagrams
    # This serves as basic condition
        if len(str1) != len(str2): 
            return 0
  
    # Compare count arrays for characters in strings
        for i in range(NO_OF_CHARS): 
            if count1[i] != count2[i]: 
                return 0    # indicates not anagrams
  
        return 1    #indicates are anagrams
    
Tree = AVLTree()  # calling class AVLTree
#initializatins
root = None
arr = []
g_arr=[]
NO_OF_CHARS = 256

print("Enter the size of Array :") #take size of array
n= int(input())
print("Enter Elements of Array :") # input elements in array
for i in range(n):
    x= input("") or int(input())
    arr.append(x)
g_arr=arr       # final array of elements
for i in range(n): 
    root1 = Tree.Insert(root, arr[i]) 
    root= root1         #root of the tree


g_count=0
x=0

print("Preorder Traversal of the given Tree" ) 
Tree.Preorder(root) # display Preorder traversal of tree
print()

h= Tree.Get_Height(root)
he= h-1
print("Height of Balanced Tree", he) #display height of balanced tree

choice= 0
    
while choice!=5:
    print("Enter your choice:" )

    print("1. Insert an Element ")
    print("2. Delete an Element ")
    print("3. Check for Anagrams ")
    print("4. Check for Max heap ")
    print("5. Exit!")
    choice= int(input())
    if choice==1:
        print("Enter an Element for Insertion :")

        ele_ins= input("") or int(input())
        arr.append(ele_ins)
        g_arr = arr
        #print(array)
        root = Tree.Insert(root, ele_ins) # call for Insertion function

        print("\n")
        # Preorder Traversal 
        print("Preorder Traversal after Insertion -" ) 
        Tree.Preorder(root)
        print("\n")
        
        h= Tree.Get_Height(root) # call for getting height of the tree
        he= h-1
        print("Height of Balanced Tree", he) # displays height of tree
        print("\n")
        
    if choice==2:
        print("Enter an Element for Deletion :")
    # Delete 
        key= input("") 
        for i in range(len(g_arr)):
            #checks if the desired element to Delete exists in the array
            if key==g_arr[i-1]: 
                
                g_arr.remove(key) #removes the element
                print(g_arr)
                root= Tree.Delete(root, key) # call for deletion function

                print("\n")
                print("Preorder Traversal after Deletion of -", key) 
        
                Tree.Preorder(root) 
                print("\n") 
                h= Tree.Get_Height(root)
                he= h-1
                print("Height of Balanced Tree", he) # displays height of tree
            else: #incorrect input
                if(i==n): 
                    print(key, "Element not in the list")
                    print("\n")

    if choice==3:
        i=0
        j=1
        anagram_element= []
        count=0
        for i in range(0,len(g_arr)):
            
            for j in range(1,len(g_arr)):
               
                if(j>i):
                    #checks if the set of strings are anagrams
                    if(Tree.Check_Anagram(g_arr[i],g_arr[j])==1):
                        # calculate count for the found anagrams
                        count+=1
                       
                        anagram_element.append(g_arr[i])
                        anagram_element.append(g_arr[j])



        print(anagram_element) # prints elements which are anagrams
        b= []
        if(len(anagram_element)>0):
            print("Anagram Elements")
            print(Counter(anagram_element))
            print("\n")
        #if element present in list but not in anagram list then it concludes
        #that the element doesn't have a anagram.
        b= list(set(g_arr)-set(anagram_element)) 
        for x in b:
            print("Anagrams Not Found :", x, 0)
            print("\n")
    if choice==4:
        if(len(arr)==2):
            # if there are 2 elements then it is in form of Max Heap
            array= Tree.Preorder(root)
            print("Preorder Traversal", array)
            for i in range(len(array)):
                if(array[i]>array[i+1]): #further condition of Max Heap
                    print("This is a max Heap")
        else:
            print("Not a max Heap")
            print("\n")        
    if choice==5:
        break # exits the loop
            

'''
OUTPUT :
Enter the size of the array :

4
Enter the elements of array :

king

ingk

rook

queen
Preorder Traversal of the given Tree
king ingk rook queen 
Height of Balanced Tree 2
Enter your choice:
1. Insert an Element 
2. Delete an Element 
3. Check for Anagrams 
4. Check for Max heap 
5. Exit!

1
Enter an Element for Insertion :

koor


Preorder Traversal after Insertion -
king ingk queen koor rook 

Height of Balanced Tree 2


Enter your choice:
1. Insert an Element 
2. Delete an Element 
3. Check for Anagrams 
4. Check for Max heap 
5. Exit!

2
Enter an Element for Deletion :

queen
queen Element not in the list


['king', 'ingk', 'rook', 'koor']


Preorder Traversal after Deletion of - queen
king ingk rook koor 

Height of Balanced Tree 2
Enter your choice:
1. Insert an Element 
2. Delete an Element 
3. Check for Anagrams 
4. Check for Max heap 
5. Exit!

1
Enter an Element for Insertion :

dieh


Preorder Traversal after Insertion -
king ingk dieh rook koor 

Height of Balanced Tree 2


Enter your choice:
1. Insert an Element 
2. Delete an Element 
3. Check for Anagrams 
4. Check for Max heap 
5. Exit!

4
Not a max Heap


Enter your choice:
1. Insert an Element 
2. Delete an Element 
3. Check for Anagrams 
4. Check for Max heap 
5. Exit!

3
['king', 'ingk', 'rook', 'koor']
Anagram Elements
Counter({'king': 1, 'ingk': 1, 'rook': 1, 'koor': 1})


Anagrams Not Found : dieh 0


Enter your choice:
1. Insert an Element 
2. Delete an Element 
3. Check for Anagrams 
4. Check for Max heap 
5. Exit!

5
'''
