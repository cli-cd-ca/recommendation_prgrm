Flower recommendation/data search program

I decided to use a binary search tree data structure for this project because the runtime would be faster than a linked list and allow for key-value storage with identical keys and different values, which creates more nodes 
(7853) to test in a BST. 

The BST in this program stores data about different types of flowers. The flower data consists of lists for every named flower. The keys in the BST are the flower types each flower belongs to and the tree stores a flower's 
data list at all of the flower's keys. 

The BST class uses an iterative method to insert new tree nodes and a recursive solution to store the nodes and build a balanced tree using the middle node as the root and dividing the halves into subtrees repeatedly. The 
final tree has a minimum height of floor(log n), where n is the total number of nodes. The time complexity for the insertion methods are O(h) and O(n), respectively, where h is the height of the tree. The space complexity is 
O(1) for the iterative method because no extra space is needed and O(n) for the recursive solution from storing nodes in a list. The BST search method also uses recursion and has both a time and space complexity of O(h), 
where h is log n in the balanced tree. 

The main program implements an autocomplete using the beginning of a word with the get list values function to retrieve flower types the user can search for and the merge sort algorithm to alphabetize them. The get list values 
function takes O(n) time with a space complexity of O(n) for the result list. The merge sort and merge functions sort in O(n*m log n) time instead of O(n log n) because there is an inner for loop in the merge function, with the 
same O(n) space complexity for the result list. 

To run the program, download the zip files and run the main flower_recom_.py file. Thanks!