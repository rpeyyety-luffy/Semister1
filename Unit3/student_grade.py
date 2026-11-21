# Program: Read marks in percentage and find the grade
#   Above 75%          : Distinction
#   60% to below 75%   : First Class
#   50% to below 60%   : Second Class
#   40% to below 50%   : Pass Class
#   Below 40%          : Failed
# Variation: if...elif...else

marks = float(input("Enter the Marks:"))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
elif marks >= 40:
    print("Pass Class")
else:
    print("Failed")