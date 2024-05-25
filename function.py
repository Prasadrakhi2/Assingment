#  Q.1 :- write a python function to calculate the factorial of a number
def factorial(num1):
    return 1 if (num1 == 1 or num1 == 0) else num1*factorial(num1-1)

num1 = 5
print(factorial(num1))



# Q.2 :- Write a python function to check if a number is in given range
def isPresent(num2):
    if num2 in range(2,8):
        print(str(num2) + " is present")
    else:
        print(str(num2) + " is not present")


num2 = 9
isPresent(num2)



# Q.3 :- write a python function to find the greatest common divisor of two no
def hcf(a,b):
    if(b == 0):
        return a
    else:
        return hcf(b, a%b)

a = 50
b = 40
print("the gdc of 50 and 40 is = " , hcf(a,b))




# Q.4 :- write a python function to check if a string is a palindrome
def isPalindrome(num4):
    revs = num4 [::-1]
    if(num4 == revs):
        print("given string is palindrome")
    else:
        print("given string is not a palindrome")


num4 = "aba" 
isPalindrome(num4)

