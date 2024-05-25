# Q.1 :- write a python program to create a dictionary representing a student's grades in different subject . calculate the average grade
def sum(d1):
    sum =0
    for i in d1.values():
        sum = sum+i

    return sum

d1 = {"Math" : 83, "English" : 74, "computer": 90}
print("average =" , sum(d1)/len(d1))



# Q.2 :- write a python program to check if the key is present in the existing dictionary . if not , add a key with a default value
d2 = {'a':1, 'b':2, 'c':3, 'd':4}
new_d2 = {}
if('e' in d2):
    new_d2 = {**d2}
    print("true")
else:
    new_d2 = {**d2, **{'e':5}}

print(new_d2)



# Q.3 :- write a python program to iterate over the key value pairs of a dictionary and display them
d3 = {'char1':'r', 'char2':'a', 'char3':'k', 'char4':'h'}
for key, value in d3.items():
    print(f"{key}:{value}")



# Q.4 :- write a python program to remove a key value pair from a dictionary
d4 = {'char1':'r', 'char2':'a', 'char3':'k', 'char4':'h'}
d4.pop("char2")
print(d4)