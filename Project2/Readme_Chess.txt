This is the readme file for the second question where we have to implement a chess solver.

I have created a separate class for each of the pieces :- 
	1.Rook
	2.Knight
	3.Bishop
	4.Queen
	5.King
	6.Pawn

I have used the list data structure. A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets. I frequently use the various in-built methods of list like - append, remove, difference.
I have a list (feasible_moves) which stores all the feasible positions of your selected piece.
Also, I have another list (user_positions) which stores all the selected positions of your selected piece.


Steps to compile and run the program:-
1. Compile and run the file "chess.py"
2. After running the file, the console asks to select one piece to move from the following: 
	1.Rook
	2.Knight
	3.Bishop
	4.Queen
	5.King
	6.Pawn
	7.Exit.
	After the desired selection, "ENTER" is expected.
3. Then you are asked to enter the desired position of your piece. After this, "ENTER" is expected.
4. Then you are asked to select position from the list of feasible range.
5. After your selection you go to step 2 again. We also print all your selected positions till now.
6. The program runs until exit operation is selected.
