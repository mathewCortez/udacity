def question1(s, t):
    s = (sorted(s)) # sort string alphabetical order and make them lists
    t = (sorted(t))
    if len(s) >= len(t): # find out which string is longer so I can have the smaller list iterate over the long one
        for letter in t: # iterate over small list
            if letter not in s: # if any of the letters are not in larger list then it is not any sort of anagram and I return false
                return False
    else:
        for letter in s:    # same as code above just with the t list being longer
            if letter not in t:
                return False
        
    return True # is anagram


def question2(a):
    if a == '': # if an empty string is entered I return the empty list before declaring variables
        return ""
    end = 1 # holds value for longest palindrome / for string splicing with start
    start = 0 # when it will start / again needed for splicing
    length = len(a)
    low = 0 #low and high are use to compare string characters
    high = 0
    for i in xrange(1, length): # xrange to save memory although its not a big memory savor 
        # test each spot as the center of the string / for even palindrome
        low = i - 1 
        high = i
        # if the two consecutive characters are the same then we could have the beginning of a palindrome
        while low >= 0 and high < length and a[low] == a[high]:
            if high - low + 1 > end:
                start = low # set new starting point for longest palindrome
                end = high - low + 1 # set new longest length
                
            low -= 1 # move low down and high up to see if the palindrome continues
            high += 1
        # same as code above but for when the palindrome is odd like racecar 
        low = i - 1 # one below palindrome center
        high = i + 1 # one above
        while low >= 0 and high < length and a[low] == a[high]:
            if high - low + 1 > end:
                start = low
                end = high - low + 1
            low -= 1
            high += 1
 
    return a[start:start + end]

'''class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal'''
    
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

'''# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()'''



print(question1('udacity','ud'))


print(question2("alracecaral"))



