# Palindrome
# Prime
# fibonnacci
# reverse the string
# reverse the array
# even odd



######
# even odd 
# a = int(input("write a integer: "))

# if a == 0 or a%2 == 0:
#     print("number is even")  
    
# else:
#     print("number is odd")
######


#####
# Prime number 

# a = int(input("write an integer: "))

# start = a 
# num = 2

# while num < a :
#     if a % num == 0:
#       print("number is not prime")
#       break
    
#     else:
#         num += 1

# if (num == a):
#     print("number is prime")

######


#####
# fibonacci series

# a = int(input("write an integer: "))

# fb = [0,1]

# count = 2 

# while count < a:
#     nextnum = fb[-1] + fb[-2]
#     fb.append(nextnum)
#     count += 1 

# print(fb)
    

####
# reverse string 

# st = input("Enter string: ")
# rstr = ""
# if len(st) > 0:
#     for i in st:
#       rstr = i + rstr
#     print(rstr)

#####
#palindrome

x = int(input("enter your input as a integer: "))

if x < 0:
    print("not palindrome")
else:
    result = str(x) == str(x)[::-1]
    print("is palindrome: ",result)

        
    
        
    





