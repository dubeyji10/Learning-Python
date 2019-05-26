#create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
#You can either enter the text from the keyboard or
# initialise a string variable with the string
print("------ since we are dealing with sets therefore one element occurs one time -------------")
originalText = input(" Type something  : ")

text = set(originalText)

print("-"*40,"\n")
#print(text)
print("-"*40,"\n")

vowels = frozenset("aeiou")
#vowels = {"a","e","i","o","u"}
# print(vowels)
# for vowel in vowels:
#     print(vowel)
text2 = set()
text2=text.difference(vowels)
print(sorted(text2))
print("-"*40,"\n")

