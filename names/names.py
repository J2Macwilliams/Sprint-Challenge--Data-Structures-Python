"""
Assumptions:
-- current algorithm is a polynomial approach
-- Converting to a BST will take time, but perform faster in the long run
-- documents are unsorted BST will be un balanced
-- can't convert to a list, dictionary or set

"""

import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# create instances of BST

bst2 = BSTNode('Jeremy')
# convert both files to a bst with a for loop
# O(n) linear function

for name in names_2:
    bst2.insert(name)

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    if bst2.contains(name_1):
        duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
