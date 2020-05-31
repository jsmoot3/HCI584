print("*********************************************************************************")
print("****************************  Start Of File *****************************************************")
''
print("#Assigment one for HCI 584")
print("#by James Smoot\n")
print("*********************************************************************************")
print("******************************** Part 0 *****************************************\n")
# part 0
# This is just a simple example to demonstrate how the start and end
# breakpoint system works
# Task: create a variable with your name and print out Hello <name>

print("start of part 0")
print ("This is the first assigment for this class")
name = input("What is your Name ")
print("What's Up", name)
print("end of 0\n")
print("*********************************************************************************")
print("****************************** Part 1 *****************************************\n")
# part 1
# task:  L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# using both, indexing and slicing on L, assemble and print a new list N that contains:
# [0,2,3,[5,6],8,10] 
# as an example, here's  how i've constructed a similar list X which contains [[2, 3], [10]] from L:
#
# L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
# X = [ L[2][1:-1], L[-1][2] ] 
# print(x)  => [[2, 3], [10]]
# You need to do something similar but end up with [0,2,3,[5,6],8,10] instead. One way to work 
# through this is to break the process down in small steps, store result of each step in a new variable
# and use those variables in the next step
print("start of part 1") # set breakpoint here
L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
print(L)
# your code
print("This is the output ----->")
output = "[{0},{1},{2},[{3},{4}],{5},{6}]".format(L[0], L[2][1], L[2][2], L[3][0][0], L[3][1][0], L[4][0], L[4][2])
print (output)
print("end of 1\n") # set breakpoint here 
print("**************************************************************************************")
print("*************************** Part 2 *************************************************\n")


# part 2
# Task: Break s into sentences (which end in a .), count them and print them out using a loop:
# result: (I truncated them with ...)
# there are 4 sentences:
# Python is an interpreted, high-level, general-purpose programming language
#  Created by Guido van Rossum and first released in 1991, Python ...
#  Its language constructs and object-oriented approach aim to help programmers ...
print("start of part 2") # set breakpoint here
s = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
# your code here
print("s: " + s)
output2 = s.split('.')
num2 = len(output2)
print("There are {0} lines ".format(num2))
print("This is the output ----->")
for x in output2:
    print(x)
print("end of 2\n") # set breakpoint here 
print("**********************************************************************************")
print("**************************** Part 3 **********************************************")

# part 3
# Task: 
# - break s into a list of words (i.e. now separated by space)
# - print out the word list (with a loop) so that every 2. word is in full uppercase.
# - optionally remove all periods and commas
# result:
# Python
# IS
# an
# INTERPRETED
# high-level
# GENERAL-PURPOSE
# programming
# LANGUAGE
print("start of part 3") # set breakpoint here
# your code here
print ("s: " + s)
output3 = s.replace(",", "").split(" ")
count = 0
for x in output3:    
    if count % 2 != 0 or count == 0:
        print(x.upper())
    else: 
        print(x)
    count += 1

print("end of 3\n") # set breakpoint here 
print("*********************************************************************************")
print("*************************** Part 4 **********************************************")

# part 4
# task: abbreviate a potentially long string s to have the x first and x last chars with ... in between
# for x = 5 this would be: "A very long description" => "A ver...ption" (... is called filler)
# in a loop, set x from 5 to and to 15 and print out x and the abbreviated version 
# there'll be an issue where the result would actually be longer(!) than the un-abbreviated s. 
# For these cases, do not perform your abbreviation, simply print out s. Note that this
# should work for any other string a or filler as well, so don't hardcode things!
# 
# Optional:
# write a general function abbr(s, filler="...", total_width=15) which abbreviates s
# to total_width chars and uses the string filler in between them. Again, make sure the
# result would not be longer than s!
# call your function a couple of times with different parameters and also test edge cases
print("start of part 4") # set breakpoint here
s = "A very long description" # a long string
print("s: " + s)
filler = "..."
# your code here
newString = ""
for w in range(len(s)) :
   # print(w)
   if w < 5 or w > 17:
        newString += s[w]
        if w == 4 :
            newString += filler
print(newString)
print("end of 4\n") # set breakpoint here 
print("*************************************************************************************")
print("****************************  End Of File *******************************************")