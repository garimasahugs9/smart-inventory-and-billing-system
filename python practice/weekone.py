'''=====================================================================================================================================
                                                    Week 1: 
                         Basics - Variables, Data Types, Input/Output, Loops, Conditionals
========================================================================================================================================='''



# Q1. Write a Python program to swap two variables.
'''
 a = 10
b = 30
temp = a
a=b 
b = temp
print (b)
'''
# Q2. Take user input and display it back to the user.
'''
a = "hello"
print (a)
'''

#Q3. Write a program to check if a number is even or odd.
'''
a = int(input('enter any value'))
if a % 2==0 :
    print ('even')
else:
    print ("odd")
'''

#Q4. Create a program that prints the multiplacation table of a given number.
'''
a = int(input('enter any value'))
for i in range(1,11):
    print(f'{a} x {i} = {i*a}')
    '''

#Q5. Write a program to find the largest of three numbers.
'''a = int(input('enter any value'))
b = int(input('enter any value'))
c = int(input('enter any value'))
if a > b>c:
    print ('a is greater')
elif c>b>a:
    print('c is greater')
else :
    print('b is greatest')'''

#Q6. Convert temperature from Celsius to Fahrenheit.
'''
a = int(input('enter celsius value'))
fahrenheit = (a * 1.8)+32
print (fahrenheit)
'''

#Q7. Write a program to calculate the factorial of a number using a loop.
'''
a = int(input('enter any value'))
factorial = 1
for i in range (1,a+1):
    factorial = factorial * i
print (factorial)
'''

#Q8. Create a program to count the number of vowels in a string.
'''
a = input('enter any value to check vowel')
vowel = "aeiouAEIOU"
count = 0
for char in a:
    if char  in vowel:
        count +=1
print(count)
'''


#Q9. Write a Python script to reverse a given string.
'''
a = input('enter any string to reverse it : ')
rev =''
for char in a:
    rev = char + rev
print(rev)
'''

#Q10. Check if a number is a palindrome.
'''
a = int(input('enter any value'))
rev = 0
num = a
while(num>0):
    rem = num%10 
    rev = rev*10 +rem
    num = num//10
if rev == a :
    print('it is palindrome')
else:
    print('it in not palindrome')
'''
#Q11. Write a program to find the sum of first N natural numbers.
'''
a = int(input('enter any value'))
sum =0
for i in range (1,a+1):
    sum += i
print(sum)
'''

    
#Q12. Create a number guessing game.
'''import random
num = random.randint(1,10)
print(num)
tries =0
while True:
    a = int(input('enter any value'))
    if a==num:
        print ('you gauess the right number')
        tries +=1
    elif num<a:
        print('go a little lower')
        tries +=1
    elif num>a:
        print('go a little higher')
        tries +=1
    else :
        print ('better luck next time')
        tries +=1
'''


#Q13. Write a program to print all prime numbers between 1 and 100.
'''
n = int(input('enter any value'))
count = 0
for i in range(1,n+1):
    if n%i==0 :
        count +=1

if count==2:
    print('its a prime num')
else:
    print('its not a prime num')

print (count)
'''

#Q14. Check if a given year is a leap year or not.
'''
year = int(input('enter any value'))
if (year % 4 == 0 and year % 100 != 0 )or(year % 400 == 0):
    print('it is a leap year')
else:
    ('its not a leap year')
 '''

#Q15. Create a program to print the Fibonacci series up to N terms.

#Q16. Write a program to find the GCD of two numbers.
#Q17. Write a program to find the LCM of two numbers.

#Q18. Check whether a character is a vowel or consonant.
'''
a = input('enter any value to check vowel or vowel: ')
vowel = "aeiouAEIOU"
count = 0
for char in a:
    if char  in vowel:
        print("vowel")
    else:
        print("consonant")
'''
#Q19. Write a program to calculate the sum of digits of a number.
'''
n = int(input("Enter any value: "))
sum = 0
if n < 0:
    n = -n

while n > 0:
    rem = n % 10
    sum += rem
    n = n // 10
print(sum)
'''

#Q20. Create a program to find the second largest number in a list
'''a=[45,22,63,25,52,12]
a.sort()
print (a[-2])'''
    

#Q21. Write a program to count the number of digits in an integer.
'''
n = int(input("Enter any value: "))
count = 0

if n < 0:
    n = -n

while n > 0:
    rem = n % 10
    count += 1
    n = n // 10

print(count)
'''
#Q22. Create a program to print all Armstrong numbers between 1 to 1000.
#Q23. Write a Python program to print a pattern of stars in a triangle.
'''
def generate_pyramid(n):
    # Your code here
    pyramid =[]
    for i in range(1,n+1):
        spaces = " "*(n-i)
        stars = "*"*(2*i-1)       
        pyramid.append(spaces+stars+spaces)       
    return pyramid
generate_pyramid(10)
'''
#Q24. Create a calculator app using if-else.
'''
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = num1 + num2
    print("Result:", result)

elif choice == 2:
    result = num1 - num2
    print("Result:", result)

elif choice == 3:
    result = num1 * num2
    print("Result:", result)

elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid choice")'''


#Q25. Write a program to display the ASCII value of a character.
#Q26. Convert a decimal number to binary using loops.
#Q27. Create a program to find the square root of a number.
'''
a = int(input('enter any value'))
if n < 0:
    print("Square root of a negative number is not real")
else:
    sqrt = n ** 0.5
    print("Square root =", sqrt)
'''
#Q28. Write a program to find the sum of all even numbers in a list.
'''a=[45,22,63,25,52,12]

sum =0
for i in  a:
    if i%2==0:
        sum += i
print(sum)'''
#Q29. Create a program to check whether a number is prime or not.
'''n = int(input('enter any value'))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count +=1

if count==2:
    print('its a prime num')
else:
    print('its not a prime num')'''
#Q30. Write a program to display the cube of the number up to an integer
'''n = int(input('enter any value : '))
for i in range (1,n+1):
    
    print (i*i*i)
'''




'''======================================================================================================================================
                                                           week 2 (28jan-29jan)
                                            Functions, Lists, Tuples, Dictionaries, Sets
========================================================================================================================================'''

# 1. Write a function to check if a number is even.
'''
def even(n):
    if n % 2==0:
        print ('number is even')
    else:
        print('number is odd')
even(5)
'''

# 2. Create a list and find the sum of all its elements.
'''
list = [23,54,36,65,68,65]
sum = 0
for i in range(len(list)):
    sum += list[i]
print(sum)
'''

# 3. Write a program to find the maximum and minimum in a list.
'''
a = [23,54,36,65,68,65,11]
maximum =  a[0]
minimum = a[0]
for i in range(len(a)):
    if maximum < a[i]:
        maximum = a[i]
print (maximum)
for i in range(len(a)):
    if minimum > a[i]:
        minimum = a[i]
print (minimum)
'''
    
# 4. Create a program that removes duplicates from a list.
'''
a = [23,54,23,36,65,65,68,65,11]
b =[]
for i in range(len(a)):
    if a[i] not in b :
        b.append(a[i])
print(b)
'''

# 5. Write a function to reverse a list.
'''
a=[23, 54, 36, 65, 68, 11]
rev =[]
for i in range(len(a)-1,-1,-1):
    rev.append(a[i])
print(rev)
'''

# 6. Create a tuple and access its elements.
'''
t = (10, 20, 30, 40, 50)

print(t[0])  
print(t[2]) 
print(t[-1])
'''

# 7. Convert a list into a tuple and vice versa.
'''
a = [10, 20, 30, 40]

t = tuple(a)

print(t)
print(type(t))

t = (5, 15, 25, 35)

a = list(t)

print(a)
print(type(a))
'''

# 8. Write a program to merge two dictionaries.
'''
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d3 = {**d1, **d2}
print(d3)
'''
# 9. Write a function to count the frequency of elements in a list.
'''
a=[1,2,2,3,3,3,3,5,5,5,]
b={}
for i in a:
    if i in b.keys():
        b[i]+=1
    else:
        b[i]=1

print(b)
'''

# 10. Create a dictionary of squares of numbers from 1 to 10.
'''
a ={}
for i in range(1,11):
    a[i] = i*i
print(a)
'''

# 11. Write a program to sort a list in ascending order.
'''
a=[23, 54, 36, 65, 68, 11]
a.sort()
print(a)
'''

# 12. Create a program to check if a key exists in a dictionary.
'''
d = {'a': 10, 'b': 20, 'c': 30}

key = input("Enter key to check: ")

if key in d: 
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
    '''

# 13. Create a set and perform union, intersection, and difference
'''
a = {1,2,3,4,5}
b = {4,5,6,7,8}
union = a.union(b)
insn = a.intersection(b)
dif = a.difference(b)
print (union)
print(insn)
print(dif)
'''

# 14. Write a function to find common elements in two lists.
'''
def common_element(a,b):
    c = []
    for i in a:
        if i  in  b and i not in c:
            c.append(i)
    print(c)           
common_element(a=[12,15,45,85,69],b=[15,6,36,68])
'''

# 15. Write a function that returns the factorial of a number.
'''def factorial(a):
    factorial = 1
    for i in range (1,a+1):
   
        factorial = factorial * i
    print (factorial)
factorial(5)'''

# 16. Create a function that checks whether a string is a palindrome.
'''def palindrome(a):
    rev = 0
    num = a
    while(num>0):
        rem = num%10 
        rev = rev*10 +rem
        num = num//10
    if rev == a :
        print('it is palindrome')
    else:
        print('it in not palindrome')
palindrome(120)'''
# 17. Write a function to count vowels in a string.
'''def vowel_count(a):
    vowel = "aeiouAEIOU"
    count = 0
    for char in a:
        if char  in vowel:
            count +=1
    print(count)
vowel_count("hello")'''
# 18. Create a dictionary and iterate over its keys and values.
'''
student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE"
}

# Iterating over keys and values
for key, value in student.items():
    print(key, ":", value)
'''

# 19. Write a function to remove all punctuation from a string.
'''
def remove_punctuation(s):
    result = ""
    punctuation = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"

    for ch in s:
        if ch not in punctuation:
            result += ch

    return result
text = "Hello, world! How are you?"
print(remove_punctuation(text))
'''

# 20. Write a function to capitalize the first letter of each word in a string.
'''
def capitalize_words(s):
    words = s.split()
    result = []

    for word in words:
        result.append(word[0].upper() + word[1:])

    return " ".join(result)
text = "python is very easy"
print(capitalize_words(text))
'''

# 21. Create a list comprehension to get squares of all even numbers in a range.
'''
squares = [i*i for i in range(1, 21) if i % 2 == 0]
print(squares)
'''
# 22. Write a function to check if a string is an anagram.
'''
def check_anagram(a, b):
    if len(a) != len(b): 
        return "Not an anagram"

    a = list(a)
    b = list(b)

    a.sort()
    b.sort()

    if a == b:
        return "It is an anagram"
    else:
        return "Not an anagram"

print(check_anagram("hello", "lloeh"))
'''
# 23. Create a nested dictionary to represent student records.
'''
students = {
    "S101": {
        "name": "Rahul",
        "age": 20,
        "branch": "CSE",
        "marks": {"Math": 90, "Physics": 85, "Chemistry": 88}
    },
    "S102": {
        "name": "Anjali",
        "age": 21,
        "branch": "ECE",
        "marks": {"Math": 78, "Physics": 82, "Chemistry": 80}
    },
    "S103": {
        "name": "Sneha",
        "age": 19,
        "branch": "ME",
        "marks": {"Math": 85, "Physics": 89, "Chemistry": 92}
    }
}

print(students)
'''

# 24. Write a function to flatten a nested list.
'''
def flatten_list(lst):
    flat = []
    for item in lst:
        if type(item) == list:
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat
a = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_list(a))
'''

# 25. Write a program to find the second highest number in a list.
'''
def second_largest(a):
    largest = a[0]
    sec_largest = a[0]
    for i in range(len(a)):
        if a[0]<a[i]:
            sec_largest = largest
            largest = a[i]
        elif i>sec_largest:
            sec_largest =a[i]
    print(largest,sec_largest)
a = [1,2,3,4,5]
second_largest(a)
'''

# 26. Create a function to rotate a list left by k positions.
# 27. Write a function to find the missing number from a list of 1 to N.
# 28. Write a program to remove all None values from a list.

# 29. Write a function to merge two dictionaries and handle key collisions by summing values.
'''
def merge(a,b):
    result={}
    for key in a:
        result[key]= a[key]

    for key in b:
        if key in result:
            result[key] +=b[key]
        else:
            result[key] = b[key]
    return result
a = {'a': 10, 'b': 20, 'c': 30}
b = {'b': 5, 'c': 15, 'd': 40}

print(merge(a,b))
'''
    
# 30. Create a function to find unique elements present in only one of two lists.
'''
def common_element(a,b):
    c = []
    for i in a:
        if i  in  b and i not in c:
            c.append(i)
    print(c)           
common_element(a=[12,15,45,85,69],b=[15,6,36,68])
'''
'''
=========================================================================================================================================
                                                            Week 3: (30jan-)
                                      File Handling, Error Handling, Modules, Comprehensions
=========================================================================================================================================
'''



#raise error
'''
age = int(input("tell your age"))
try:
    if age<10 or age>18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print ("welcome to the club")
except Exception as err:
    print(f'an error occured as {err}')

print ('the club will start soon')
'''
#file handeling - CRUD operation
'''
from pathlib import Path            # to read the path present in this folder
import os

def readfileandfolder():
    path =Path(' ')               # This will direct the path and the empty space Show JIS path mein AAP exist kar rahe ho uska path show karega
    items = list(path.rglob('*'))  # Jitney be file or folder recursively Read Karne ke Liye path.globe kayus hotaa hai
    for i, items in enumerate(items):  # Kisi Bhi list Index or value hoti hai Agar hum chahate hai Ki index or value alag alagh  save ho to hum enumrate function ke through run karte hai
        print(f"{i+1}:{items}")  

def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name :- ")
        p= Path(name)
        if not p.exists() and p.is_file() :
            with open(p,"w") as fs:
                data = input("what you want to write in this file :-")
                fs.write(data)
            print(f" file created succesfully")
        else:
            print("this file already exist")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input ("which file you want to read ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open (p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed successfully")
        else:
            print("the file does not exist")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("tell which fileyou want to update:-")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :-")
            print("press 2 for changing the name of your file :-")
            print("press 3 for changing the name of your file :-")

            res = int(input("tell your response :-"))

            if res == 1:
                name2 = input("tell your new file name")
                p2 =Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p,'w') as fs :
                    data = input("tell what you want to write this is overwrite the data:-")
                    fs.write(data)
            if res == 3:
                with open(p,'a') as fs:
                    data = input ("tell what you want to append:-")
                    fs.write(" "+data)

    except Exception as err :
        print("an error occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delet")
        p= Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("file removes suicessfully")
        else:
            print("no such file exist")
    except Exception as err:
        print(f'An error occured as {err}')

print ('press 1 for creating a file')
print ('press 2 for reading a file')
print ('press 3 for updating a file')
print ('press 4 for deleting a file')

check = int(input("please tell your response:- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()
'''
# Q1. Write a Python script to read a file and print its contents.

 
#p = open(r'C:\Users\HP\OneDrive\Desktop\coding\python\python practice\weekone.py')
#print(p.read())

# Q2. Create a file and write your name into it.
'''
r= open('superman.txt' , 'w')
r.write('my name is garima')
r.close()
'''
# Q3. Handle a ZeroDivisionError using try-except.
'''
a = int(input('tell your number'))
try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")
else:
    print("good there is no exception")
finally:
    print("i will run no matter what")

print('ok i have done the division')
'''
    
# Q4. Write a program to handle file not found error.
'''
filename = input("enter a file name : ")
try:
    f=open(filename,"r")
    print(f.read())
    f.closee()
except FileNotFoundError:
    print("Error:file not found")
'''
# Q5. Create a module with a function and import it in another file.
'''
import module
result = module.add(10,20)
print(result)
'''
# Q6. Use a list comprehension to filter even numbers from a list.
'''
a = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in a if x % 2 == 0]
print(evens)
'''
# Q7. Write a generator that yields even numbers up to N.
'''
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i
n = 10
for num in even_numbers(n):
    print(num)
'''
# Q8. Create a program to count lines and words in a file.
'''
filename = input("enter a file name")
try:
    with open(filename,'r')as f:
        lines = f.readline()
        line_count = len(lines)
        word_count =0
        for line in lines:
            words = line.split()
            word_count += len(words)
        print("Number of lines:", line_count)
        print("Number of words:", word_count)

except FileNotFoundError:
    print("Error: File not found")
    '''
# Q9. Write a program to read a CSV file and print its contents.
'''
import csv
filename = input("Enter CSV file name: ")
try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Error: File not found")
'''
# Q10. Handle multiple exceptions in a single try block
'''
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input, please enter numbers only")

except Exception as e:
    print("Unexpected error:", e)
'''

 
'''
=======================================================================================================================================================================
                                                                                       Week 4:
                                                               OOPs Concepts + Solve 50–100 Logic Building Problems
=======================================================================================================================================================================\

'''
# Q1. Write a Python program to check if a string has all unique characters.
'''
s = input("Enter a string: ")

if len(s) == len(set(s)):
    print("All characters are unique")
else:
    print("String contains duplicate characters")
'''
# Q2. Create a program that removes all duplicate characters from a string.
'''
s = input("enter any string: ")
result= " "
for char in s:
    if char not in result:
        result +=char
print (result)
 '''
# Q3. Write a script to count the frequency of each character in a string.
'''
s = input("enter any string: ")
result= {}
for char in s:
    if char in result:
        result[char] += 1
    else:
        result[char] =1
print (f"{char} : {result}")
'''
# Q4. Write a program that accepts a sentence and calculates the number of upper and lower case letters.
'''
s = input("Enter any sentence: ")

upperc = 0
lowerc = 0

for char in s:
    if char.isupper():
        upperc += 1
    elif char.islower():
        lowerc += 1

print("Uppercase letters:", upperc)
print("Lowercase letters:", lowerc)
'''
# Q5. Create a program to find the longest word in a sentence.
'''
s =input ("enter a sentnce :  ")
a =s.split()
max_length = 0
longest_word =" "
for char in a :
    if len(char)> max_length:
        longest_word = char
        max_length = len(char)
print(longest_word)
print(max_length)
'''
# Q6. Write a program that takes a string and returns the string in reverse order without using [::-1].
'''
s =input ("enter a string :  ")
rev=" "
for char in s:
    rev = char + rev
print(rev)
'''

# Q7. Create a Python function to check if a string is a pangram.
'''
def is_pangram(s):
    s= s.lower()
    letters = set()
    for char in s :
        if char.isalpha():
            letters.add(char)
    return len(letters) == 26
is_pangram("The quick brown fox jumps over the lazy dog")
'''
# Q8. Write a Python script to sort words in a sentence alphabetically.
'''
sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

print("Sorted words:")
for word in words:
    print(word)
'''
# Q9. Write a program to check if two strings are anagrams.
'''
a = input("enter any string 1: ")
b = input("enter any string 2: ")

if len(a)==len(b):
    for char in a:
        if a.count(char) != b.count(char):
            print('not an anargam')
            break
    else:
         print ("it is anargram")
else:
    print('not an anargam')
'''
# Q10. Write a Python program to capitalize the first letter of each word in a sentence.
'''
s = input("enter a sentence :")
b = s.split()
result =[]
for char in b:
    new_word = char[0].upper() + char[1:]
    result.append(new_word)
final_sentence = " ".join(result)

print (final_sentence) 
'''
# Q11. Create a program that extracts numbers from a string and returns their sum.
'''
s = input('enter a string : ')
num = "1234567890"
sum = 0
for char in s :
    if char in num:
        b =int(char)
        sum = sum + b
        
print(sum)
'''
# Q12. Write a program to replace all spaces in a string with underscores.
'''
s = input('enter a string : ')
result =" "
for char in s :
    if char ==" ":
        result += "_" 
    else:
        result += char
print(result)
'''
# Q13. Write a function to count how many times a substring appears in a string.
'''
def count_substring(main_string, sub_string):
    count = 0 
    sub_len = len(sub_string)

    for i in range(len(main_string)-sub_string +1):
        if main_string[i:i + sub_len] == sub_string:
            count +=1
    return count
'''
# Q14. Write a script to convert a string into title case without using .title().
'''
s = input("Enter a string: ")

result = ""
capitalize_next = True

for char in s:
    if char == " ":
        result += char
        capitalize_next = True
    elif capitalize_next:
        result += char.upper()
        capitalize_next = False
    else:
        result += char.lower()

print(result)

'''

# Q15. Write a Python program to merge two dictionaries into one.
'''
d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print (d1)
'''
# Q16. Create a program to filter out all non-alphabetic characters from a string.
'''
s = input("Enter a string: ")

result = ""

for char in s:
    if char.isalpha():
        result += char

print("Filtered string:")
print(result)
'''
# Q17. Write a function that returns True if a string ends with a given suffix.
'''
def ends_with(string, suffix):
    return string.endswith(suffix)

# Example
print(ends_with("football", "ball"))  # True
print(ends_with("football", "bat"))   # False
'''

# Q18. Create a program that counts words, characters, and lines in a paragraph.

# Q19. Write a script to encode a string using Caesar cipher (shift = 3).
# Q20. Write a program that accepts a string and counts vowels and consonants.
'''
a = input('enter any value to check vowel or vowel: ')
vowel = "aeiouAEIOU"
count = 0
for char in a:
    if char  in vowel:
        
        print("vowel")
    else:
        print("consonant")
 '''       
# Q21. Create a script to convert binary string to decimal.
'''
binary = input("Enter a binary number: ")

decimal = 0
power = 0

for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal value:", decimal)
'''
# Q22. Write a program to count the number of words starting with a vowel in a string.
'''
s = input('enter a string :')
a = s.split()
vowel = "aeiouAEIOU"
count = 0
for char in a:
    if char[0] in vowel:
        count += 1
print(count)
'''
# Q23. Create a script that takes a sentence and removes all stop words.
'''
s = input('enter a string :')
a = s.lower()
words = s.split()
filtered_words = []
stop_words = {"is", "on", "the", "a", "an", "of", "in"}
for char in words:
    if char not in stop_words:
        filtered_words.append(char)
        
   
print(" ".join(filtered_words))
'''
# Q24. Write a Python program to split a sentence into words and reverse each word.
'''
s = input('enter a string :')
words = s.split()
rev=" "
for char in words:
    rev = " "+char + rev
print(rev)
'''
# Q25. Write a function that returns a new string made of every third character of the original string.
'''
s = input("enter any string : ")
result = " "
for i in range(0,len(s),3):
    result += s[i]
print(result)
'''
# Q26. Write a program to find all palindromic substrings in a string.
'''
s = input("enter any string : ")
for start in range(len(s)):
    for end in range(start+1,len(s)+1):
        substring = s[start:end]

        if substring == substring[::-1]:
            print(substring)
 
'''           
# Q27. Write a function that compresses a string using run-length encoding.
'''
def compress_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    return result

s = input("enter any string : ")
print(compress_string(s))
'''
# Q28. Write a Python program to count the frequency of each word in a file.
'''
file =open('sample.txt',"r")
text = file.lower()
words = text.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] =1
for word, count in frequency.items():
    print(word, ":", count)

file.close()

'''

# Q29. Write a script that extracts hashtags from a tweet.
'''
s = input("Enter any tweet: ")

words = s.split()
hashtags = []

for word in words:
    if word.startswith("#"):
        hashtags.append(word)

print("Hashtags:", hashtags)
'''

# Q30. Write a function to remove punctuation from a string.
'''
import string

def remove_punctuation(text):
    result = ""

    for char in text:
        if char not in string.punctuation:
            result += char
h
    return result

s = input("Enter a string: ")
print(remove_punctuation(s))
'''
# Q31. Create a program that finds the first non-repeating character in a string.
'''
s = input("Enter a string: ")

freq = {}

# Count frequency
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Find first non-repeating character
for char in s:
    if freq[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")
'''
# Q32. Write a script that converts camelCase to snake_case.
''' 
s = input("Enter a string: ")
result = " "
for char in s:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char
print(result)
'''
# Q33. Write a function to generate acronyms from a sentence.
'''
s = input("Enter a string: ")
w = s.split()
r = " "
for char in w:
    r += char[0].upper()
print (r)
'''
# Q34. Write a script to check if a file contains a specific word.
'''
file = open("sample.txt","r")
s = input("Enter a string: ")
content = file.read()
w= s.lower()
c = content.lower()
if w in c:
    print("Word found in the file")
else:
    print("Word not found in the file")
file.close()
'''
# Q35. Write a Python program to find and replace text in a file.
'''
file = open("sample.txt","r")
s = input("Enter a string: ")
replace = input("enter replacement value")
result=" "
content = file.read()
w= s.lower()
c = content.lower()
if w in c:
    result += replace
else:
    result += w
file.close()
'''
# Q36. Write a script that checks if all characters in a string are digits.
'''
s = input("Enter a string: ")
digits = "1234567890"
for char in s:
    if char in digits:
        print("all are digits")
    else:
        print('not digits')
'''        

# Q37. Write a program to calculate the average word length in a sentence.

# Q38. Create a function that removes all HTML tags from a string.
'''
s = input("Enter a string: ")
result = " "
for char in s:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char
print(result)
'''
# Q39. Write a program to parse a date string and display it in a different format.
'''
date = input("Enter date (YYYY-MM-DD): ")

parts = date.split("-")

year = parts[0]
month = parts[1]
day = parts[2]

new_date = day + "/" + month + "/" + year

print("Formatted date:", new_date)
'''
# Q40. Write a script that finds all email addresses in a given text.

# Q41. Write a program that counts the occurrence of each vowel in a paragraph.
# Q42. Create a function that validates an email address format.
# Q43. Write a script to check if a string is a valid URL.
# Q44. Write a program that extracts all integers from a given text.
'''
s = input('enter text : ')
num = "1234567890"
sum = " "
for char in s :
    if char in num:
        sum += char
print(sum)
'''
# Q45. Create a script to find duplicate words in a paragraph.

# Q46. Write a program that converts a sentence to Pig Latin.
# Q47. Write a script that finds the longest sentence in a paragraph.

# Q48. Write a Python program to read a file and display all lines that contain a given keyword.
# Q49. Write a script to clean a text file by removing extra spaces and blank lines.
# Q50. Write a Python program to count how many sentences are in a paragraph.



'''
=========================================================================================================================================================================
                                                                                 Week 5:
                                                                Statistics Basics – Descriptive Statistics
                                                                Mean, Median, Mode – Concepts & Formulas
                                                        Variance & Standard Deviation – Why do we need them?
                                                                      Range, Quartiles, IQR
                                                            Understanding Data Distribution (Normal vs Skewed)
                                                 Hands-on with Python: mean(), median(), std(), describe() in NumPy & Pandas
==========================================================================================================================================================================
'''


# Q1. Create a NumPy array of 10 random integers between 1 and 100. Find its mean.

# Q2. Calculate the median of the array: [10, 5, 8, 12, 3, 7].
# Q3. Generate an array of 15 random numbers between 1 and 50. Find its standard deviation.
# Q4. Create a 3x3 array with values from 1 to 9. Find the row-wise mean.
# Q5. For the array [4, 6, 8, 10, 12], calculate mean, median, std.
# Q6. Generate a 5x5 NumPy array of random integers (0 to 100). Find the overall mean.
# Q7. Create an array of 50 random integers and calculate the standard deviation.
# Q8. Find indices of non-zero elements from [1,2,0,0,4,0]
# Q9. You have an 2D array, print array element [[7,4]]: 
# [[2,3,4
#  5,7,4
#  8,9,0]]
# Q10. Create 2 array of 2-Dimension and then perform matrix multiplication on them.

'''
========================================================================================================================================================================
                                                                                  Week 6: 
                                                                         Probability & Combinatorics
                                                            Basic Probability Rules (Addition, Multiplication)
                                                               Conditional Probability & Bayes Theorem
                                                            Permutations & Combinations (Simple problems)
                                                                Expected Value & Real-World Examples
=========================================================================================================================================================================
'''
# Q1. A dice is thrown once. Find the probability of getting a 2 or 5.
'''
p(2 or 5)= 2/6= 1/3
'''
# Q2. A card is drawn from a deck of 52 cards. Find the probability of getting a red card or a king
'''
done 
'''
# Q3. A number is chosen from 1 to 10. Find the probability that the number is even or divisible by 3.
'''
s={1,2,3,4,5,6,7,8,9,10}
even = A={2,4,6,8,10}
divisible by 3= B = {3,6}
P(A or B) = P(A) + P(B) - P(A union B)
P(A or B) = 5/10 + 3/10 -1/10
P(A or B) = 5+3-1/10
P(A or B) = 7/10


'''
# Q4. In a bag, there are 3 red and 2 blue balls. A ball is drawn randomly. Find the probability of getting a red ball or a blue ball.
'''
done
'''

# Q5. A spinner has 6 equal parts numbered 1 to 6. Find the probability of spinning a 1 or 6.
'''
done
'''
# Q6. A card is drawn twice with replacement. Find the probability that both cards are spades.
'''
done
'''
# Q7. A card is drawn from a deck and not replaced, then another card is drawn. Find the probability that both are aces.
'''
 done
'''
# Q8. A coin is tossed twice. Find the probability of getting head on both tosses.
'''
done
'''
# Q9. A dice is rolled twice. Find the probability that first die shows 3 and second die shows an even number.
'''
done
'''
# Q10. A bag contains 4 white and 2 black balls. Two balls are drawn without replacement. Find the probability that both are black.
'''
done
'''
# Q11. A coin is tossed once. Find the probability of getting a tail.
'''
done
'''
# Q12. A dice is thrown once. Find the probability of getting a number greater than 4
''' 
done
'''
# Q13. A card is drawn from a deck. Find the probability that it is a queen or a red card.
'''
done
'''
# Q14. A box contains 2 red, 3 blue, and 5 green balls. One ball is drawn. Find the probability that it is green
'''
done
'''
# Q15. A dice is rolled twice. Find the probability that both numbers are odd.
'''
done
'''
# Q16. A coin is tossed 3 times. Find the probability of getting exactly 2 heads.
'''
done
'''

# Q17. A bag has 4 yellow and 1 black ball. A ball is drawn and not replaced, then another ball is drawn. Find the probability that both balls are yellow.
'''
done
'''
# Q18. Two cards are drawn together from a deck. Find the probability that both are kings.
'''
done
'''

# Q19. A spinner with 4 equal sections numbered 1 to 4 is spun twice. Find the probability that both spins show the same number.
'''
done
'''
# Q20. A box has 5 red and 5 blue balls. One ball is drawn at random. Find the probability that it is not blue.
'''
done5
'''

''' 
==========================================================================================================================================================================
                                                                               Week 7,8:
                                                          Inferential Statistics – Hypothesis Testing
                                                                        Population vs Sample
                                                                        Sampling Techniques
                                                           Hypothesis Testing: Null & Alternate Hypotheses
                                                                p-values, Significance Levels (α)
                                                    T-tests & Chi-Square Test (Intuition only, no heavy math)
============================================================================================================================================================================
'''

# Q1. A coin is tossed 50 times and shows 30 heads. State the null and alternate hypotheses to check if the coin is fair.


# Q2. A factory claims its bulbs last 1000 hours on average. Formulate the null and alternate hypotheses for testing this claim.
# Q3. A new teaching method is applied to a class. Formulate hypotheses to test whether the new method improves average student marks.
# Q4. A company claims 40% of customers prefer online shopping. Formulate hypotheses to test this claim.
# Q5. If a hypothesis test gives p-value = 0.03 and 𝛼=0.05, should you reject the null hypothesis?
# Q6. If a test gives p-value = 0.15 and 𝛼 = 0.05, what is your decision about the null hypothesis?
# Q7. Explain what it means if p-value < α in hypothesis testin
# Q8. If 𝛼 = 0.01, what is the confidence level of the test?
# Q9. You have the heights of 10 male and 10 female students. Which test will you perform to check if their average heights are different?
# Q10. A training program is introduced. Employee performance is measured before and after. Which T-test will check if the program improved performance?
# Q11. You roll a dice 120 times and record how many times each number appears. Use a Chi-Square test to check if the dice is fair.
# Q12. A chips brand claims the average packet weight is 50g. You weigh 10 random packets: [49, 52, 51, 50, 48, 49, 50, 51, 52, 50] Use a One-Sample T-Test to check if the claim is true.
# Q13. A hospital claims a new medicine has a 70% success rate. In a trial of 20 patients, 12 recovered. Use a proportion test to check if the success rate matches the claim.
# Q14. A survey of 30 people records gender (Male/Female) and favorite drink (Tea/Coffee). Perform a Chi-Square test to check if drink preference depends on gender.
# Q15. A factory claims its bulbs last 1000 hours on average. You test 8 bulbs: [980, 1005, 995, 1010, 1000, 985, 1020, 990] Use a One-Sample T-Test to verify the claim.

'''
========================================================================================================================================================================
                                                                               Week 9:
                                                     Data Cleaning – Missing Values, Outliers, Encoding, Scaling
                                                        Identifying & Handling Missing Data (drop, fill, impute)
                                                             Detecting & Treating Outliers (IQR, Z-score)
                                                          Encoding Categorical Variables (Label, One-Hot)
                                                           Feature Scaling (Min-Max, Standardization)
===========================================================================================================================================================================
'''

# Q1. Count how many missing values are in a DataFrame.
# Q2. Show which values are missing in a DataFrame (True/False).
# Q3. Remove all rows with missing values.
# Q4. Fill missing values in a column with 0.
# Q5. Fill missing values in a column with "Not Available".
# Q6. Print the maximum and minimum value of a column.
# Q7. Find values in a column that are greater than 100.
# Q8. Replace all values greater than 100 with 100.
# Q9. Sort a column to check for extreme values.
# Q10. Remove the highest value from a numeric column.
# Q11. Convert column Gender with Male/Female into 0/1.
# Q12. Create separate columns for each City from a City column.
# Q13. Count how many times each category appears in a column.
# Q14. Change all values in a column to lowercase.
# Q15. Divide all values in a numeric column by 100.
# Q16. Subtract the minimum value from a numeric column.
# Q17. Convert all column values to range 0 to 1 manually.
# Q18. Show the mean and standard deviation of a numeric column.
# Q19. Subtract column mean from each value (basic standardization).
# Q20. Round all values in a numeric column to 2 decimals.

'''
=============================================================================================================================================================================
                                                                                 Week 10: 
                                                        pandas + numpy Deep Dive – DataFrames, Aggregations, Joins
                                                          pandas for DataFrames (create, read, filter, modify)
                                                                  Aggregations (groupby, agg, pivot_table)
                                                                      Merging & Joining multiple datasets
                                                        numpy for numerical operations (arrays, stats, reshaping)
===============================================================================================================================================================================
'''

# Q1. Create a DataFrame of 5 students with columns: Name, Age, Marks.
# Q2. Display the first 3 rows and last 2 rows of the DataFrame.
# Q3. Show the shape of the DataFrame (rows × columns).
# Q4. Access only the Name column from the DataFrame.
# Q5. Filter all rows where Marks are greater than 50.
# Q6. Add a new column Result with values: "Pass" or "Fail".
# Q7. Update the Marks of the first student to 95.
# Q8. Delete the Result column from the DataFrame.
# Q9. Sort the DataFrame by Marks in descending order.
# Q10. Count the number of unique names in the Name column.
# Q11. Create a DataFrame of Sales with columns: Region, Product, Sales.
# Q12. Calculate the total sales.
# Q13. Calculate the average sales per product.
# Q14. Count how many times each product appears in the dataset.
# Q15. Find maximum and minimum sales per region using groupby and agg.
# Q16. Create a pivot table showing total sales per Region vs Product.
# Q17. Create a pivot table showing average sales per Region.
# Q18. Create a NumPy array of numbers from 1 to 10.
# Q19. Find the sum, mean, and standard deviation of the array
# Q20. Reshape an array of numbers from 1 to 12 into a 3×4 matrix.
# Q21. Create a 2D NumPy array of random integers (3×3).
# Q22. Find the sum of each row and sum of each column.
# Q23. Multiply two 3×3 matrices using NumPy.
# Q24. Find the maximum and minimum value in the array and their indices.
# Q25. Slice a NumPy array to get only even numbers.

'''
===========================================================================================================================================================================
                                                                                  Week 11: 
                                                       Data Visualization – matplotlib, seaborn, EDA Techniques
                                                            matplotlib basics: Line, Bar, Scatter, Pie
                                                       seaborn for advanced plots: Heatmaps, Boxplots, Pairplots
                                                    Exploratory Data Analysis (EDA): Identify trends & patterns
                                                               Visual Storytelling: Making insights clear
============================================================================================================================================================================

'''
# Q1. Create a dataset with the following columns-> Products,Regions,Sales,Profit and 10 rows:
# Q2. Plot a line chart of Sales for all 10 rows (index as X-axis).
# Q3. Plot a bar chart showing total sales for each product.
# Q4. Plot a scatter plot of Sales vs Profit.
# Q5. Create a pie chart showing total sales by region.
# Q6. Plot a histogram of the Sales column.
# Q7. Create a boxplot of Profit to detect outliers.
# Q8. Create a countplot showing how many products are sold in each region.
# Q9. Create a heatmap to show correlation between Sales and Profit.
# Q10. Show total and average sales per region using pandas

'''
============================================================================================================================================================================
                                                                             Week 12:
                                                        Basics – SELECT, WHERE, ORDER BY, LIMIT, Aliasing
                                                                 Introduction to Databases & SQL
                                                              SELECT statements to retrieve data
                                                       Filtering with WHERE (AND, OR, BETWEEN, IN, LIKE)
                                                                Sorting results with ORDER BY
                                                             Limiting results with LIMIT & OFFSET
                                                                     Aliasing columns and tables
===============================================================================================================================================================================

'''
# Q1. Create and Insert Data. Create a table named Employees with the following columns:
# EmployeeID,Name,Department,Salary,JoiningDate.
# Q2. Select all columns from the Employees table.
# Q3. Display only Name and Department columns.
# Q4. Show all employees who work in the IT department.
# Q5. Retrieve employees with a Salary greater than 45,000.
# Q6. Show employees who joined after 2020-01-01.
# Q7. Retrieve employees with a salary between 40,000 and 55,000.
# Q8. Display employees whose department is either HR or Finance.
# Q9. Retrieve employees whose name starts with 'S'.
# Q10. Show employees whose name ends with 'a'.
# Q11. Display employees ordered by salary in descending order.
# Q12. Display the first 3 employees based on joining date.
# Q13. Retrieve employees skipping the first 2 rows using OFFSET.
# Q14. Show employee names as Employee_Name using alias.
# Q15. Display Department as Dept and Salary as Income.
# Q16. Combine aliasing with sorting: Show top 3 highest paid employees with columns Employee_Name and Income.
# Q17. Find the highest salary in the Employees table.
# Q18. Find the total number of employees in each department.
# Q19. Show the average salary of all employees.
# Q20. Display the employee(s) with the lowest salary.

'''
===============================================================================================================================================================================
                                                                                Week 13: 
                                                   GROUP BY, HAVING, Joins (Inner, Left, Right, Full), Subqueries
                                                    GROUP BY & Aggregation functions (SUM, AVG, COUNT, MAX, MIN)
                                                                      Filtering groups with HAVING
                                                    INNER, LEFT, RIGHT, FULL Joins – Combining multiple tables
                                                        Writing Subqueries for filtering and aggregations
===============================================================================================================================================================================
'''

# Q1. Count how many employees are in each Department.
# Q2. Find the average salary per department.
# Q3. Show the highest and lowest salary in each department.
# Q4. Show the total salary paid per department.
# Q5. Count how many employees joined in each year (use YEAR(JoiningDate)).
# Q6. Find departments that have more than 1 employee.
# Q7. Find departments where average salary > 50,000.
# Q8. Find joining years where more than 2 employees joined.
# Q9. Perform an INNER JOIN to show Employee Name with their Department Manager.
# Q10. Perform a LEFT JOIN to list all employees and their managers, even if manager info is missing.
# Q11. Show total salary per department using JOIN + GROUP BY
# Q12. Find the employee with the highest salary using a subquery.
# Q13. Find all employees who earn more than the average salary.
# Q14. Find the second highest salary using a subquery.
# Q15. Find employees who joined after the employee with the lowest salary.
# Q16. List all departments that have any employee earning more than 60,000.
# Q17. Find the total number of employees and total salary in each department.
# Q18. List all employees whose salary is the maximum in their department.
# Q19. Show all departments where no employee earns less than 45,000 (use HAVING).
# Q20. Find employees whose joining year is the same as any HR department employee (use subquery).


'''
=============================================================================================================================================================================
                                                                           Week 14: 
                                                      Advanced SQL – Window Functions, CTEs, Nested Queries + Projects
                                                    Window Functions (ROW_NUMBER, RANK, DENSE_RANK, PARTITION BY)
                                                              Common Table Expressions (CTEs)
                                                              Nested Queries for complex filtering
                                                                Building end-to-end SQL queries
=========================================================================================================================================================================

'''

# Mini Projects:
# Project 1: Analyze an E-commerce dataset: Top-selling products, most active customers, revenue trends.
# Project 2: Build a Student Management Dashboard using SQL: Average scores, top performers, pass/fail stat