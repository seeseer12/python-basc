#set of collection of unordered items and unique
#immutable in nature
# we cannot add list and dict in set as they are muttable in nature
# num={
    
#     1,2,3,4,
# }
# print(num)
# print(len(num)) 


collection=set()
collection.add(22)
collection.add((2,3,55,66,5))
collection.remove(22)
# print(collection)




# basically set is muttable but it can contains only immuatble datatypes
# collection.clear() clears all set
# print(collection)


# print(collection.pop()) -> pops any random 

# some other set operations
a={1,2,3,4,4,5,"shishir"}
print(type(a))
print(a.union(collection))
print(collection.intersection(a))
print(collection.difference(a))




