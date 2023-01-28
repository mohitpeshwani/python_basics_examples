'''
upper() -------------->  to return Uppercase of all the characters
lower() --------------> to return lowercase of all the characters
capitalize() ---------> to Make every character 1st character upper case
swapecase() ----------> Making exact opposite of the original string upper case into lower case and lower case into upper case
count('') ------------> used to count the no of apperances of the following answer
find('')--------------> find the element and return the index no of 1st occurance else not found -1
index('')-----------> Getting the index of character

isupper()-----------> return true if all character is upper
islower()-----------> return true if all character is lower
isalnum()-----------> Return true if string is combination of alphabets and character
isalpha()-----------> return true if string contains alphabets
isnumerical()-------> Return True if the string is a numeric string, False otherwise.
isdigit()-----------> Return True if the string is a digit string, False otherwise.
isascii()-----------> Return True if the string characters contains from ascii charactersets

endswith(' ')------->Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.
startswith(' ')----->Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.
replace('old characters', 'new characters') ---------> replace the old chars with new characters
strip() ------------> remove space from start and end of the string if any.
removeprefix()------>Return a str with the given preffix string removed if present.
removesuffix()------>Return a str with the given suffix string removed if present.




'''
string ="Mohit Peshwani"
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.swapcase())
print(string.count('w'))
print(string.find('Mohit'))
print(string.index('Pesh'))
print(string.isupper())
print(string.islower())
print(string.isalpha())
print(string.isalnum())
print(string.isnumeric())
print(string.isdigit())
print(string.endswith('ani'))
print(string.startswith('ani'))
print(string.replace('Mohit','Sky'))
print(string.lstrip())
print(string.isascii())
print(string.removeprefix("M"))
print(string.removesuffix("i"))
print(string.title())