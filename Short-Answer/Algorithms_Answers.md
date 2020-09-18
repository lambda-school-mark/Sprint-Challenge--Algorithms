#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) its linear because it is based on the input of n and grow at same rate

b) 0(n logn) first loop is based on n, but the second loop increases complexity also based on n

c) O(n) a recursive function is linear unless its complexity is increased, but it grows at same rate each time it is called

## Exercise II

Start at midpoint and then continue finding the midpoint of top or bottom, by ruling out half on each drop, you are minimizing the amount of both dropped and broken eggs. This means you would probably use a binary search, resulting in a time complexity of O(log n)
