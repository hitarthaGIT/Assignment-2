# Write a program in python to insert a word to the end of a string .

## in this case lets the string be "My name is Hitartha and I love coding !!"

str1="My name is Hitartha and I love coding !!"
word=input("Enter the word to be inserted : ")
str=str1.split()
str.append(word)
print(str)

'''
Output:
Enter the word to be inserted : Bye!!
['My', 'name', 'is', 'Hitartha', 'and', 'I', 'love', 'coding', '!!','Bye!!']

'''