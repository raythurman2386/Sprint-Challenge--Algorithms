#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) since it doesn't matter what the amount is only that the calculation runtime is linear, that is it only runs through one time.

b) O(n log n) The outer for loop will run at O(n) although the inner while loop increments j \*= 2, so the while would run less than n

c) O(n) calling the function recursively is still a linear run time.

## Exercise II

_Binary Search_
Start on the middle floor and drop the egg
if the egg breaks
adjust the scope of floors to be tested to that floor and below
repeat until egg doesn't break,
if the number of floors to be tested is 3 or 1 f is that floor plus one
else keep repeating

runtime should be O(log n)
