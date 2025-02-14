'''
Homework10
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

def find_missing_number(lst):
    # Remove duplicates by converting to a set and back to a list
    lst = list(set(lst))  
    largest = max(lst)  
    missing_numbers = []
    for num in range(0, largest + 1):
        if num not in lst:  
            missing_numbers.append(num)  
    return sorted(missing_numbers)

def even_partition(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    if len(even_numbers) > 0 and sum(even_numbers) > 0:
        return even_numbers
    else:
        return []

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest10.py'))