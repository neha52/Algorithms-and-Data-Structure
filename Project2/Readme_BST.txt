This is the readme file for the first question where we have to create a Balanced Binary Search Tree.

I have used an AVL tree in order to have a balanced binary search tree. AVL trees are height-balanced binary
search trees. The key idea in an AVL tree is that the for every node, heights of left and right subtree can differ by no more than 1; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time, where n is the number of nodes in the tree prior to the operation. Sometimes, insertions and deletions require the tree to be rebalanced. The height of an AVL tree is always O(log n) where n is the number of nodes in the tree.

I have an AVL tree class that can perform insertion, deletion, checking anagrams, displaying preorder traversal operations. In the preorder traversal method, the root node is visited first, then the left subtree and finally the right subtree. For insertion, the first step is to perform the standard BST insertion of the new node and update the height of the root. If the tree is not balanced, then it is rebalanced. For deletion, the first step is to rerform standard BST deletion and update the height of the root. If the tree is not balanced, then it is rebalanced. I use the left rotation and right rotation operations to rebalance the trees. For anagrams, I keep count of each character in a input string. And then compare these count arrays for two different strings (with same length) to check if they are anagrams. For max heap (only if the array has two elements), the value in each internal node has to be greater than or equal to the values in the children of that node.

Steps to compile and run the program:-
1. Compile and run the file "BST.py"
2. After running the file, the console asks for the size of the array (which is an integer value). After the desired size, "ENTER" is expected.
3. Then you are asked to enter the element of the array (strings are expected here). After each element is entered, "ENTER" is expected.
4. Then using preorder traversal, the elements of the tree are printed.
5. Then the height/length of the binary balanced tree is printed.
6. Then the remaining four desired operations could be performed. These are :- adding an element to the BST (Insert an Element), deleting an element from the BST (Delete an Element), finding the number of Anagrams for each input string in the BST (Check for Anagrams), checking if BST is Max Binary Heap or not (Check for Max Heap).
7. The program runs until exit operation is selected.

An example to execute the program is as belows:-

Enter the size of Array :
4
Enter Elements of Array :
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
Counter({'ingk': 1, 'king': 1, 'koor': 1, 'rook': 1})


Anagrams Not Found : dieh 0


Enter your choice:
1. Insert an Element 
2. Delete an Element 
3. Check for Anagrams 
4. Check for Max heap 
5. Exit!
5
