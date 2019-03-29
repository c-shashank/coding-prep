""" We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Input Format

Read y, the year that needs to be checked.

Constraints

Output Format

Output is taken care of by the template. Your function must return a boolean value (True/False)

Sample Input 0

1990

Sample Output 0

False

Explanation 0

1990 is not a multiple of 4 hence it's not a leap year.  """

year = int(raw_input()) #(1) year = 1900
print is_leap(year) #(2) year = 1900 Function Call to is_leap

def is_leap(year): #(3) year= 1900
    leap = False #(4) year= 1900, leap= False
    if year%4==0: #(5) 1900%4==0 so enters the next line , leap= False
        if year%100==0: #(6) 1900%100==0 so enters the next line , leap= False
            leap = False #(7) leap=False 
        elif year%400==0:
            leap=True
    else:
        leap=False
    return leap #(8)
