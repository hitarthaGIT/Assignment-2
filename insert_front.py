# Write a program in python to insert a word into the front of a string.

## in this case lets the string be "My name is Hitartha and I love coding !!"

str1="My name is Hitartha and I love coding !!"
word=input("Enter the word to be inserted : ")
str=str1.split()
str.insert(0,word)
print(str)


'''
Output: 
Enter the word to be inserted : Hello
['Hello', 'My', 'name', 'is', 'Hitartha', 'and', 'I', 'love', 'coding', '!!']

'''