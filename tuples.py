# Q.1 :- write a python program to concatenate two tuples
tuple1 = (1,2)
tuple2 = (3,4)

print(tuple1 + tuple2)


# Q.2 :- write a python program to count the occurrence of an element in a tuple
tuple3 = (4,8,6,2,4,8,5,1,2,4,2,6,1)
key = 6

i = 0
count = 0
while(i<len(tuple3)):
    if(tuple3[i] == key):
        count +=1
    i += 1

print("total count = " + str(count))



# Q.3 :- write a python program to convert a tuple to a list
tuple5 = (1,2,3,4,5,6)
list = list(tuple5)
print(list)


# Q.4 :- write a python program to create a tuple of numbers and calculate the sum of elements
tuple6 = (1,2,3,4,5)

# print(sum(tuple6))

i=0
sum = 0
while(i<len(tuple6)):
    sum += tuple6[i]
    i += 1

print(sum)