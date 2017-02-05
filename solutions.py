from operator import itemgetter # for question 3



def question1(s, t):
    if s == '' or t == '' or s == None or t == None:
        return False
    else:
        indexes = [] # hold the index in string s where the characters in string t are found
        for i in xrange(0,len(t)): # iterate through t 
            if t[i] in s: # check if it is in s
                indexes.append(s.index(t[i])) # if it is then add the index to the list
        indexes.sort(key=int) # sorted in numerical order
        if len(indexes) == len(t): # check if all the characters of t were found in string s
            for i in xrange(0, len(indexes)):  # iterate through the index list
                if indexes[i] == min(indexes) and indexes[i] + 1 in indexes: # check if the indexes are in order in string s 
                    return True # if they are then it can be an anagram
                return False
        return False


def question2(a):
    if a == '' or a == None: # if an empty string is entered I return the empty list before declaring variables
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




def question3(G):
    edges, vertices = edgeWeightSort(G) # after this weight list will not be sorted by weight
    # http://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
    edges_sorted = sorted(edges, key=itemgetter(0)) # edges will be sorted by weight with vertices 
    return verticeConnected(edges_sorted, vertices)


def edgeWeightSort(G):
    edges = []
    vertices = {}
    for startingVertice in G: # going through the vertices in G which is now sorted by edge weight
        vertices[startingVertice] = [startingVertice] # add vert to the dictionary
        for edge in G[startingVertice]: 
            endingVertice = edge[0]# the other vertice in the edge
            weight = edge[1] # weight of edge between the two vertices
            edges.append([weight, startingVertice, endingVertice]) # list of edge weight and the vertices at the end of the edges
    return edges, vertices


def verticeConnected(edges_sorted, vertices):
    minSpanTree = {} # dictionary to hold and build answer
    # https://docs.python.org/3/tutorial/datastructures.html
    for edge in edges_sorted: # unpacking the sorted edge list
        startingVertice = edge[1] # starting vertice    
        endingVertice = edge[2] # ending
        weight = edge[0] # edge weight
        if startingVertice not in vertices[endingVertice] and endingVertice not in vertices[startingVertice]:
            # https://www.tutorialspoint.com/python/dictionary_setdefault.htm
            minSpanTree.setdefault(startingVertice, []).append((endingVertice, str(weight))) # build up dictionary with the vertices and its edges with other verts
            # http://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method
            minSpanTree.setdefault(endingVertice, []).append((startingVertice, str(weight))) # add the reverse 
            vertices[startingVertice], vertices[endingVertice] = verticeList(
                vertices[startingVertice], vertices[endingVertice]) # add in the connected vertices to list
    return minSpanTree


def verticeList(vlist1, vlist2):
    # https://docs.python.org/2.7/tutorial/datastructures.html
    vertConcat = vlist1 + list(set(vlist2) - set(vlist1)) # removing the duplicate vertices
    return vertConcat, vertConcat

def question4(T, r, n1, n2):
    if inputCheck(T, r, n1, n2) == False:
        return None

    current_parent = r
    previous_parent = r
    child_left, child_right = returnChildren(T, current_parent)
    while True:
        if child_left is None and child_right is None:
            return None # node is not there thus the branch has ended 
        if n1 < current_parent and current_parent < n2:# the current parent appears to be between the two nodes and is the branching point making it the least or lowest common ancestor
            return current_parent 
        if n1 == current_parent or n2 == current_parent: # the target node is the same a the parent node in this case the last ancestor is the least common of the two nodes
            return previous_parent
        if n2 < current_parent: # shows that it is in the left branch because higher number than the root going to the right side so this checks left branch
            previous_parent = current_parent # keep track of previous parent
            current_parent = child_left # new 'root' parent to check down for target node
            child_left, child_right = returnChildren(T, current_parent) # find the children for new parent
        if n1 > current_parent: # target node is not down the left branch so we check the right branch
            previous_parent = current_parent
            current_parent = child_right
            child_left, child_right = returnChildren(T, current_parent) # find children

def inputCheck(T, r, n1, n2):
    if T is None or T == []: # need a matrix
        return False
    if n1 is None or n2 is None: 
        return False
    if r is None or r == n1 or r == n2: # r cannot be n1 or n2 because the tree will keep on building as 3 would be the root and the child would repeat
        return False
    if r < 0 or n1 < 0 or n2 < 0:
        return False
    return True


def returnChildren(T, value):
    child_left = None # declare variable to avoid a referenced before assignment error
    child_right = None
    for index in xrange(0, len(T[value])):
        if T[value][index] == 1: # iterating though the matrix checking the root for a 1
            if index < value: # node spot is less than the node meaning its on the left
                child_left = index # child node in row
            else:
                child_right = index # right branch node
    return child_left, child_right





def question5(ll, m):
    if ll is None or m is None or m == 0: # either no linked list or elements in the list
        return None
    length = ll_length(ll) # determine the length of the list which helps see if m is a spot in the list
    i = 1 # loop counter
    node = ll.head # this grabs the last element instered into the linked list.  So it is the last element in the list and we then count backwards to find the mth form this spot
    # the last position is considered 1 (this just confused me because I thought it would be zero so I just wanted to make this clear)
    if m == 1: # this would return the last element in ll 
        return node.data
    elif m > length: # if m is longer than the length the list is too small to find the mth element
        return None
    while i < m: 
        node = node.next # move to the next element from the back
        i += 1 # increment I to keep track of how many time this loop is ran
        # this code should only run m number of times so when i is no longer less than m we have found the mth element
    return node.data

def ll_length(ll):
    node = ll.head 
    length = 1 # length starts at 1 in this instance
    # https://discussions.udacity.com/t/question-5-is-the-last-element-the-first-from-the-end-or-the-0th-from-the-end/175547/4
    while node.next is not None: # will end when no more elements are in the list
        length += 1 # increment length
        node = node.next # move to the next element in the list and repeat
    return length

# https://discussions.udacity.com/t/linked-list-technical-interview/184747/2
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, newnext):
        self.next = newnext
  
class LinkedList(object):
    def __init__(self, data):
        self.head = Node(data)

    def append(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp






print(question1('udacity','ticy'))
print("expect true")
# True
print(question1('udacity','ac'))
print("expect true")
# True
print(question1('udacity','uc'))
print("expect false")
# False
print(question1('udacity',''))
print("expect false")
# False
print(question1('udacity','uy'))
print("expect false")
# False
print(question1('aca', 'aa'))
print("expect false")
# False
print(question1('aca', 'ac'))
print("expect true")
# True
print(question1('aca', 'z'))
print("expect false")
# False
print ("")



print(question2("alracecaral"))
# racecar
print(question2("lkaabccbaie"))
# abccba
print(question2(""))
# ''

print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5)],
                 'C': [('B', 5)]})
# {'A': [('B', '2')], 'C': [('B', '5')], 'B': [('A', '2'), ('C', '5')]}

print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5), ('D', 3)],
                 'C': [('B', 5), ('D', 4)],
                 'D': [('C', 4), ('B', 3)]})
# {'A': [('B', '2')], 'C': [('D', '4')], 'B': [('A', '2'), ('D', '3')], 'D': [('B', '1'), ('C', '4')]}

print question3({})
# {}

print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                1,
                4)
# 3

print question4([],
                3,
                1,
                4)
# None

print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                3,
                4)
# None

print question4([[0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                2,
                4)
# 3



ll = LinkedList(5)
ll.append(9)
ll.append(7)
ll.append(20)

print question5(ll, 1)
# 20

print question5(ll, 0)
# None

print question5(ll, 2)
# 7

print question5(ll, None)
# None





