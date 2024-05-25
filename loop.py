# Q.1 :- Write a python program to print the fibonacci sequence up to n terms



# Q.2 :- write a python program t find the sum of all numbers stored in a list
l2 = [1,2,3,4,5,6]
i = 0
sum = 0
while(i<len(l2)):
    sum += l2[i]
    i += 1

print("Total sum = " , sum)



# Q.3 :- write a python program to check whether a number is prime or not
l3 = [1,2,3,4,5]
evenCount = 0
oddCount = 0
i = 0
while(i<len(l3)):
    if(l3[i]%2 == 0):
        evenCount += 1
    else:
        oddCount += 1

    i += 1 


print("total no of even elements = " , evenCount)
print("total no of odd elements = ", oddCount)



# Q.4:- write a python program to check whether a number is prime ir not
def isPrime(l4):
    i = 2
    while(i<(l4-1)):
        if(l4%i == 0):
            return -1
            break
        else:
            i += 1

        
l4 = 11
print("number is not prime" if (isPrime(l4)==-1) else "number is prime")