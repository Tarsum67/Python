'''
Homework13
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python" 
'''
def calculate_interest(principalAmount, rate, time):
   total = principalAmount * rate * time 
   total = int(total)
   return total



def compound_interest(principalAmount, rate, n, time):
    total = principalAmount * (1 + rate / n) ** (n * time)
    return round(total - principalAmount, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest13.py'))