'''
Homework21
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''
def is_palindrome(string):
     return string == string[::-1]
    
def is_anagram(string1,string2):
  return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))