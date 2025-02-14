'''
Homework11
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''

def count_zeros(lst):
    zero_list = []  
    
    for row in lst:
        for element in row:
            if element == 0: 
                zero_list.append(element)  
   
    return len(zero_list)

def replace_with_zero(lst):
    updated_lst = []  
    
    for row in lst:
        updated_row = []  
        
        for i in range(len(row)): 
            if row[i] < 0: 
                updated_row.append(0)  
            else:
                updated_row.append(row[i])  
        
        updated_lst.append(updated_row) 
    
    return updated_lst  


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest11.py'))