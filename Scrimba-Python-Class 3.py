# Tuples == Immutable

friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2])
print(friends_tuple[2])
print('#' * 20)

# Sets - blazingly fast unordered Lists - Don't accept duplicates values

friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')

friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set))
print(friends_set & my_friends_set)

print(friends_set.difference(my_friends_set))
print(friends_set - my_friends_set)

print(friends_set.union(my_friends_set))
print(friends_set | my_friends_set)

print(friends_set.symmetric_difference(my_friends_set))
print(friends_set ^ my_friends_set)

print(friends_set)

empty_list = []
empty_list1 = list()

empty_tuple = ()
empty_tuple1 = tuple()

empty_set = {}  # this is wrong, this is a dictionary
empty_set1 = set()

print('#' * 20)

