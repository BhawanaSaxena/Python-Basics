'''This section shows various approaches to work with deques
'''
from collections import deque
#  #returns last 3 lines
#def anything(filename,n=10):
#     #Returns the last n lines of a file
#     return deque(open(filename),n)
#
# print(anything("article.txt"),3)
#o/p:deque(['the (before a singular or plural noun)\n', '\n', 'Indefinite article\n', '\n', 'a (before a singular noun beginning with a consonant sound)\n', 'an (before a singular noun beginning with a vowel sound)\n', '\n', 'Count nouns - refers to items that can be counted and are either singular or plural\n', '\n', 'Non-count nouns - refers to items that are not counted and are always singular'], maxlen=10) 3

from collections import defaultdict

x = (('a',1),('b',3),('c',4),('d',7),('b',5),('d',3))
# d = defaultdict(list) #we have used a list as default_factory
#
# for key,value in x:
#     d[key].append(value)
#
# #print(d)
# #o/p :defaultdict(<class 'list'>, {'a': [1], 'b': [3], 'c': [4], 'd': [7]})
#
# #print(d.items())
# # o/p : dict_items([('a', [1]), ('b', [3]), ('c', [4]), ('d', [7])])
#
# print(d.keys()) #o/p:dict_keys(['a', 'b', 'c', 'd'])
# print(d.values()) #o/p : dict_values([[1], [3, 5], [4], [7, 3]])


# s = "Plassy Class"
# d = defaultdict(int)
# for key in s:
#     d[key]+=1
# print(d.items())
#o/p:dict_items([('P', 1), ('l', 2), ('a', 2), ('s', 4), ('y', 1), (' ', 1), ('C', 1)])