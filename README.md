# Red-Blue-Nim-game-


Programming language used Python.

To Run the code
1)Install Python if alrready not installed
2) Open Command Prompt in the system
3) Locate the directory folder where the files are present
4) Execute the following command
	red_blue_nim.py <num-red> <num-blue> <first-player> <depth>

->replace the words in < and >  with the respective values.

<num-red> is number of Red marbles (Required)
<num-blue> is number of Blue marbles (Required)
<first-player> is to declare whether human will start first or computer(optional)(Required when depth is given)
<depth> to give the depth limit for depth limit search implementation

->In the first player insert whether 'human' or 'computer' if not entered it assumes as computer.
->depth should be replaced with depth limit search and to give depth, first player is required to enter.  

Example
        With depth
		red_blue_nim.py 5 3 human 9
        
        Without depth and first player
		red_blue_nim.py 5 3 


Eval function is defined in eval python file which is used to calculate the score of the leaf nodes by adding the value of marbles and determine whether positive or negative value to identify the Min Max algorithm and find appropriate path.

<> human.py file takes inputs from humans and execute.
<> computer.py file calls other python files and genrate a MinMax tree to decide which marble to choice.
<> piles.py has the class used to create tree.
<> child_path.py sets the node values and implements alpha beta pruning.
