""" A substring ss of a string is considered to be special if every letter of the alphabet that ss contains
shows up in ss both in lower case and upper case forms. For instance, s = “cdCDD” is special because both lower and upper
case forms of “c” and “d” appears in the string. On the other hand, s = “cdC” is not special (due to missing “D”).
Devise a divide-and-conquer (DC) algorithm with to find the longest substring ss in a given string s. Implement a
recursive Python function named GetLongSpecialSubstring DC() to perform this task. You can assume that
1 ≤ len(s) ≤ 100, and s only contains upper and lower case from English language."""

def is_special(substring):
    lower_alphabetset=set()
    upper_alphabetset=set()
    
    for char in substring:
        if char.islower():
            lower_alphabetset.add(char)
        elif char.isupper():
            upper_alphabetset.add(char)

    return all(char.upper() in upper_alphabetset for char in lower_alphabetset) and all(char.lower() in lower_alphabetset for char in upper_alphabetset)

def longest_special_substring(s):
    n=len(s)
    longest_substring=""

    for i in range(n):
        for j in range(i+1,n+1):
            substring=s[i:j]
            if is_special(substring) and len(substring)> len(longest_substring):
                longest_substring=substring

    return longest_substring

def GetLongSpecialSubstring_DC(s):
    return longest_special_substring(s)

s1 = "FdedDdf"
res1 = GetLongSpecialSubstring_DC(s1)
print(f"Longest special substring in '{s1}' is: '{res1}'")

s2 = "cDCd"
res2 = GetLongSpecialSubstring_DC(s2)
print(f"Longest special substring in '{s2}' is: '{res2}'")

s3="c"
res3=GetLongSpecialSubstring_DC(s3)
print(f"Longest special substring in '{s3}' is: '{res3}'")