#Password generator Project
import random


letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',  
          't','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S', 
          'T','U','V','W','X','Y','Z']
 
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','+','/','^']
print("Welcome to The Password Generator!")
nr_letters=int(input("how many Letters Would you like in you password ? "))
nr_numbers=int(input("how many numbers Would you like in you password ? "))
nr_symbols=int(input("how many symbols Would you like in you password ? "))
#---------------------------------------------------------------------------
#easy Level (asd123!@#)

# password= ""                                      # password variable which is in string format

# for char in range(1,nr_letters+1):                #This for loop is Used to work nr_letters Times
#     random_char=random.choice(letters)
#     # print(random_char)
#     password = password + random_char             # String Concetanation

# for char in range(1,nr_numbers+1):                #This for loop is Used to work nr_numbers Times
#     random_char=random.choice(numbers)
#     # print(random_char)
#     password = password + random_char             # String Concetanation
    
# for char in range(1,nr_symbols+1):                #This for loop is Used to work nr_symbols Times
#     random_char=random.choice(symbols)
#     # print(random_char)
#     password = password + random_char             # String Concetanation


# print(f"your password is {password}")

#---------------------------------------------------------------------------------------------

#Hard Level (a!sd@1#23)



password_list=[]

for char in range(1,nr_letters+1):                       
      password_list.append(random.choice(letters))

for char in range(1,nr_numbers+1):                       
      password_list.append(random.choice(numbers))

for char in range(1,nr_symbols+1):                       
      password_list.append(random.choice(symbols))


print(password_list)           
random.shuffle(password_list)                                   # this is used to Shuffle the list
print(password_list)


password=""
for char in password_list:                                       # to convert from list to string
    password+= char 
print(f"Your Strong password is {password}")
