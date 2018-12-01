max_degree_solver.py solves the given graph and rowdy groups by first assigning the 
students with the least friendships to eah bus to guarantee that there are no empty bus. 
Then assign the student with the most friendships and each of his/her neighbor to 
the bus that will add more friendships with the current students assigned on that bus.
Next, it assigns the student with the second most friendships and each of his/her neighor
to the bus. It does this repeatedly until all the students have been assigned.

How to run:
Change the following variables with the desired input:
path_to_inputs - a string variable of the inputs path containing all size_category folders
path_to_outputs - a string variable that corresponds the path of the outputs
size_category - a list of strings of size categories of the inputs
number - input number

Then run python max_degree_solver.py