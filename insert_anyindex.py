# Write a program in python to insert a word into a string to index given by the user.

## in this case lets the string be "My name is Hitartha and I love coding !!"
str1="My name is Hitartha and I love coding !!"


word=input("Enter the word to be inserted : ")
index=int(input("Enter the index : "))
str=str1.split()
str.insert(index,word)
print(str)





'''
Output: 
Enter the word to be inserted : yes
Enter the index : 5
['My', 'name', 'is', 'Hitartha', 'and', 'yes', 'I', 'love', 'coding', '!!']

'''