# Q.1 :- write a python program to find the sum of  all elements in a list 
list1 = [1,2,3,4,5]

i=0
sum = 0

while(i < len(list1)):
    sum += list1[i]
    i = i+1

print(sum)



# Q.2 :- write a python program to remove duplicate from a list
list2 = [1,2,3,4,2,1]
result = []

for i in list2:
    if i not in result:
        result.append(i) 

print("list before remove duplicate = " + str(list2))
print("list after remove duplicate=" + str(result))



#Q.3 :- write a python program to find the index of a specific element in list
list3 = [1,2,3,4,5,6]
key = 2

i=0
while(i < len(list3)):
    if(list3[i] == key):
        print("index = " + str(i))
        break

    i += 1
else:
    print("not found")
    


# Q.4 :-write a python program to sort a list of strings in alphabetical order
list4 = ["mango" , "apple" , "banana"]
print("list before sorting" + str(list4))
list4.sort()
print("list after sorting" + str(list4))
