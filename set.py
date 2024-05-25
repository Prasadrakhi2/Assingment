# Q.1 :- write a python program to create a set of unique elements from a list
list = [1,2,3,4,1,5,6,1,2]
set1 = set(list)
print(set1)

# Q.2 :- write a python program to check if two sets have any elements in common
set2 = {1,2,3,4,5}
set3 = {6,4,8,9}
print(set2.isdisjoint(set3))



# Q.3 :- write a python program to perform set operations like union, intersection, and difference between two sets
s1 = {1,2,3}
s2 = {2,4,5}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)



# Q.4 :- write a python program to check if a set is a subset of another set
s3 = {1,2,3,4,5,6}
s4 = {3,6}
print(s4.issubset(s3))