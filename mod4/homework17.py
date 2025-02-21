'''
Homework17
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''


def frequency_counter(lst):
    # your code here
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1
    return frequency

# Step 1: Create the NATO Phonetic Alphabet Dictionary
nato_alphabet = {
    "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot",
    "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
}


# Step 2: Develop the Spelling Program
def translation(english_word):
    
    for letter in english_word.upper(): 
        if letter in nato_alphabet:
            print(nato_alphabet[letter])  
        else:
            print(f"Character '{letter}' does not have a NATO phonetic equivalent.")


def spell_word():
    
    user_word = input("Enter a word to spell: ")
    translation(user_word) 
# Step 3: Define main function
def main():
    
    spell_word()  

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest17.py'))