# Roman Numeral problem

Pass 3 out of 4 tests for credit.

Convert the roman numeral to an integer
i = 1
v = 5
x = 10
L = 50
C = 100
D = 500
M = 100

If the input is not a valid roman numeral, return -1
abc = -1
iiiiiiii = -1

Numbers strung together are added when they go from biggest to smallest.

    iii = 1 + 1 + 1 = 3
    xi = 10 + 1 = 11
    CLx = 100 + 50 + 10 = 160

You are not allowed to write 3 of the same number in a row.

    iiii = 1 + 1 + 1 + 1 = 4 (Not allowed)

However if a smaller number is written before a larger number, you subtract that value

    iv = 5 - 1 = 4
    CM = 1000 - 100 = 900

For complicated numbers, read right to left. If the left value is smaller than the next number,
subtract those numbers before adding to the overall sum

    MCMXCiv = 1000 + (1000 - 100) +   (100-10)   +  (5-1)
                M         CM             XC           iv

Use string indeces to find the value in the string.

    roman_numeral = "IX"
    roman_numeral[0] = "I"
    roman_numeral[1] = "X"
