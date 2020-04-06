Restate the Problem 
* There is an array.
* it contains an unspecified number of integers
* two of the numbers add up to a specific target

Ask Clarifying Questions 
* data types - is there only one data type?
* edge cases - are there negative numbers? floats? repeated numbers?
* Do the indices need to be returned in the order they appear in the array?

State Assumptions 
* each input has exactly one solution
* the array contains only integers
* the target is an integer

Think Out Loud 

Brainstorm Solutions 
* The brute force solution would be to search for all possible pairs of numbers - sort the array in increasing order, initialize two indices and test whether they add up to the target. loop through numbers at indices until a combination is found which sums to the target
* An alternative solution would be to sort the integers into a hash table, from which they would be quicker to search

Explain Rationale 
* Using the hash table would get us to the answer faster so I'm going to try that
* Hash Tables are commonly used as look-up table data structures because they are really fast and reliable when storing key-value pairs where quick look-up is required.

Discuss tradeoffs 
* The brute force solution would take longer, but also take up less space - time complexity: O(n^2), space complexity: O(1)
* The hashtable solution would have a shorter time complexity, but use up more space. - time complexity 0(n), space complexity 0(n)

Suggest Improvements 
* edge cases - 
* other sides of the problem
* third way of solving it uses incremeting, and has a time complexity of O(n), and a space complexity of O(1), because it does not use any extra data structures