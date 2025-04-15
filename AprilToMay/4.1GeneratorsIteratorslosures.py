'''
4.1: Generators, iterators, and closures
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
# Generator function to produce all possible two-letter combinations
def two_letter_combinations(characters):
   
    for first in characters:
        for second in characters:
            yield first + second  # Yield each two-letter combo

def main():
    
    letters = ['T', 'A', 'R', 'S', 'U']

    print("All two-letter combinations:")
  
    for combo in two_letter_combinations(letters):
        print(combo)


if __name__ == "__main__":
    main()
