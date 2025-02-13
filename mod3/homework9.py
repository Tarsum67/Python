'''
Homework9
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

def bubble_sort(lst):
    # your code here
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True   
        if not swapped:
            break 
    return lst                     
     
    
    

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest9.py'))