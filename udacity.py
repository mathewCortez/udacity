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






print(question1('udacity','ud'))


print(question2(alracecaral))
 


