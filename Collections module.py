'''Collections module implements specliazed container datatypes providing alternatives to Python's in built
general purpose container: dict,list,set and tuple.

deque - list like container with fast append and pop from both the ends

Counter - dict subclass for counting hashable objects

'''
from collections import Counter

# Creating counter object --

# Lets tally occurence of words in a list
# cnt = Counter()
# for word in ["red","blue","purple","black","white","pink","blue","red","black"]:
#     cnt[word]+=1
#
# print(cnt)

# O/p of program is : Counter({'red': 2, 'blue': 2, 'purple': 1, 'black': 2, 'white': 1, 'pink': 1})

# ===========================================================================


# Find ten most common words in text file:
import re
# findall - it searches for all occurences of a regular expression pattern in a given string and returns list of the matched substring
#  \w+ is the regular expression pattern,it matches any sequence of one or more word characters(letters,digits, or underscores)
# words = re.findall(r"\w+",open("article.txt").read().lower())
# print(Counter(words).most_common(10))

# output is [('a', 14), ('the', 11), ('noun', 8), ('are', 7), ('and', 7), ('before', 6), ('of', 5), ('article', 5), ('is', 5), ('to', 5)]


# c = Counter() #an empty counter
# print(c)
# o/p : Counter()

# c = Counter("Collections") #a new counter from an iterable
# print(c)
# o/p : Counter({'o': 2, 'l': 2, 'C': 1, 'e': 1, 'c': 1, 't': 1, 'i': 1, 'n': 1, 's': 1})


# c= Counter({"blue":45,"green":34}) #a new counter from mapping
# print(c)
# o/p : Counter({'blue': 45, 'green': 34})


# c = Counter(hi = 12,bye=15) #a new Counter from keyword args
# print(c)
# o/p:Counter({'bye': 15, 'hi': 12})


# c = Counter(a=2,b=4,c=7,d=12)
# print(list(c.elements()))
# o/p:['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']

# print(Counter("abracadabra").most_common(3))
# [('a', 5), ('b', 2), ('r', 2)]


# c = Counter(a=4,b=2,c=4,d=-2)
# d = Counter(a=2,b=-3,c=4,d=-1)
# c.subtract(d)
# print(c)
# o/p : Counter({'b': 5, 'a': 2, 'c': 0, 'd': -1})

# ======================================================

from collections import deque

d = deque("ghi")  # make a deque with 3 items
# print(d)
# for elem in d:
#     print(elem.upper())

# o/p : deque(['g', 'h', 'i'])
# G
# H
# I

# d.append("l") #append to the right the element
# print(d)
# d.appendleft("a") #append to the left
# print(d)
# d.pop() #return and remove from rightmost item
# print(d)
# d.popleft() #return and remove from leftmost item
# print(d)
# print(list(d))

# o/p :
# deque(['g', 'h', 'i', 'l'])
# deque(['a', 'g', 'h', 'i', 'l'])
# deque(['a', 'g', 'h', 'i'])
# deque(['g', 'h', 'i'])
# ['g', 'h', 'i']


# list the contents of a deque in reverse
# d = list(d)
# print(d[0] + "\n" + d[-1]) #indexing on list of deque
# o/p : g
#      i


# list the contents of a deque in reverse
# d = reversed(d)
# print(list(d))

# search the deque
#print("h" in d)  # O/p : True


# add multiple elements at once
d.extend("lmn")
# print(d)
#o/p : deque(['g', 'h', 'i', 'l', 'm', 'n'])


#right rotation
# print(d.rotate(1))
# print(d)  deque(['n', 'g', 'h', 'i', 'l', 'm'])
# d.rotate(1)
# print(d)  deque(['m', 'n', 'g', 'h', 'i', 'l'])

#left rotation
# d.rotate(-1)
# print(d)  deque(['h', 'i', 'l', 'm', 'n', 'g'])
# d.rotate(-1)
# print(d)  deque(['i', 'l', 'm', 'n', 'g', 'h'])


# d.extendleft("zqx") #extends and add items to the left one by one
# print(d)  deque(['i', 'l', 'm', 'n', 'g', 'h'])


#empty the deque
# d.clear()
# print(d) deque([])

#Trying to pop element from a blank deque
# d.pop() IndexError: pop from an empty deque


