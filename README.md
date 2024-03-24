### brief explanation ###
---------------------------

building a program for giving users to manage zoo system
when the user can interaction with dynamic
menu of filter searching animal by code and name,
adding new animal to the zoo and removing
animal from the zoo.
the user can exit from the program in any time.


### code explanation ###
---------------------------

# line 1:
import time library for making sleeping execution to achieve better representation for the users

# lines 3-5:
we have 3 strings consists codes and names of the animals. each block is seperated by ',' character

# line 7:
define a list with len 3 where the list consists those 3 strings

# line 8:
creating new dictionary. this dictionary should consist keys of animal codes and values of animal names
based on the strings given

# line 10:
iteration on each string in the list

# line 11:
creating list using split for each string in the last list seperated by ',' character
its mean the list consist every block in the string without the ','
the string "Dog12,CAT3,LiOn7,DolphiN11,fish6" will create this list:
["Dog12", "CAT3", "LiOn7" , "DolphiN11", "fish6"]

# line 12:
iteration on each string on the list after seperated them by ','

# line 13:
filter all the digits in each string and put the result into code variable
casting the result to int representing code number of the animal

#line 14:
filter all the alpha characters in each string and put the result into name variable

#line 15:
adding to the dictionary a new key-value consists the key of code in line13 and the value of name in line14
the value will convert into lower characters
its mean the dict will be like this after 1 iteration: {12:'dog'}

#lines 18-19 :
creating a function that searching animal by code giving as parameter
the function return True if the code was given located in the dictionary, otherwise False

#lines 22-23:
creating a function that searching animal by name giving as parameter
notice that the name could be any character and the function needs to return
a new dictionary consist all the matches based on the name giving as a parameter
for example: 'H' will return the following dictionary:
{11:'dolphin', 6:'fish'}
no matches will return empty dictionary : {}

#lines 26-30:
creating a function that adding new animal to the dictionary based on the code and name giving
as parameters.
if the code already exist in the zoo we will return False, otherwise we will add this animal
and return True

#lines 33-37:
creating a function that removing animal based on the code giving as a parameter.
if the code doesn't exist in the zoo we will return False,
otherwise we will remove this animal and return True

#line 40:
creating a while loop : the while loop will stop only if the user will press 5 for exit the program

#lines 42-49:
printing the instructions for the user by showing him the menu options:
1 for searching animal by code
2 for searching animal by name
3 for adding new animal
4 for removing animal
5 for exit

#line 51:
creating a variable named 'choice'. the user should press one of the options 1-5
the choice of the user will initialize into the variable choice

#lines 53-63:
if the user will press 1 he should press some number representing the animal code for searching animal
if the function will return True we will print the code and the name of this animal
if the code doesn't exist in the zoo we will print to the user that the code doesn't exist

#lines 65-81:
if the user will press 2 he should press some name for searching animal
we will print to the user all the dictionary animals details matches with the searching input
if the dictionary is empty we will print: "no results"

#lines 83-98:
if the user will press 3 he should press code and name of the animal he wants to add to the zoo
if the function will return True its means this code animal doesn't exist and the function will
add the new animal. after that we will print the new dictionary after adding this animal.
if the code is already exist we will print to the user: this code already exist!

#lines 100-114:
if the user will press 4 he should press code animal for removing animal from the zoo
if the function will return False its mean there is no code such that input, so we will print
this code doesn't exist!
if the function will return True, the function will remove this animal,
and we will print the new dictionary animals after removing

#lines 116-118:
if the user will press 5 the program will break






