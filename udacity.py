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

def question2(a)

    return string


print(question1('udacity','ud'))
