

def convert_roman_numeral_to_int(roman_numeral:str) -> int:
    """Convert the roman numeral to an integer
    i = 1
    v = 5
    x = 10
    L = 50
    C = 100
    D = 500
    M = 100

    If the input is not a valid roman numeral, return -1
    
    numbers strung together are added when they go from biggest to smallest. 
    iii = 1 + 1 + 1 = 3
    xi = 10 + 1 = 11
    CLx = 100 + 50 + 10 = 160

    
    You are not allowed to write 3 of the same number in a row. 
    However if a smaller number is written before a larger number, you subtract that value

    iiii = 1 + 1 + 1 + 1 = 4 (Not allowed)

    iv = 5 - 1 = 4 
    CM = 1000 - 100 = 900
    MCMXCiv = 1000 + (1000 - 100) +   (100-10)   +  (5-1) 
                M         CM             XC           iv
    """
    romal_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    total = 0
    
    pass